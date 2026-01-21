from PySide6.QtWidgets import (QWidget, QPlainTextEdit, QTextEdit)
from PySide6.QtGui import (QPainter, QColor, QTextFormat, QTextCursor, QFont, QSyntaxHighlighter, QTextCharFormat)
from PySide6.QtCore import (QRect, Qt, QRegularExpression, QSize)

class linenumberArea(QWidget):
    def __init__(self, editor):
        super().__init__(editor)
        self.editor = editor

    def sizeHint(self):
        return QSize(self.editor.lineNumberAreaWidth(), 0)

    def paintEvent(self, event):
        self.editor.lineNumberAreaPaintEvent(event)

class mySyntaxHighlighter(QSyntaxHighlighter):
    def __init__(self, parent, format:dict):
        super(mySyntaxHighlighter,self).__init__(parent)
        self.format = format

    def highlightBlock(self, text: str) -> None:
        highlighterFormat = QTextCharFormat()
        highlighterFormat.setFontWeight(QFont.Bold)
        highlighterFormat.setForeground(Qt.darkMagenta)
        expression = QRegularExpression(self.format[0]["regularExpression"])
        i = expression.globalMatch(text)
        while (i.hasNext()):
            match = i.next()
            self.setFormat(match.capturedStart(), match.capturedLength(), highlighterFormat)

class codeEditor(QPlainTextEdit):
    def __init__(self, placeholderStr:str, syntax_high_lighter=None):
        super().__init__()
        self.lineNumberArea = linenumberArea(self)
        self.currentLineNumber = None
        self.currentLineColor = QColor(173, 216, 230)
        self.placeholderStr = placeholderStr
        self.setPlaceholderText(self.placeholderStr)


        self.blockCountChanged.connect(self.updateLineNumberAreaWidth)
        self.updateRequest.connect(self.updateLineNumberArea)
        self.cursorPositionChanged.connect(self.highlightCurrentLine)

        if syntax_high_lighter is not None:
            self.highlighter = mySyntaxHighlighter(self.document(), syntax_high_lighter)

        self.updateLineNumberAreaWidth(0)

    def focusInEvent(self, event):
        super().focusInEvent(event)
        self.setPlaceholderText("")

    
    def focusOutEvent(self, event):
        super().focusOutEvent(event)
        self.currentLineNumber = None
        self.setExtraSelections([])
        self.setPlaceholderText(self.placeholderStr)   

    def lineNumberAreaWidth(self):
        digits = 1
        max_ = max(1, self.blockCount())
        while max_ >= 10:
            max_ //= 10
            digits += 1
        space = 3 + self.fontMetrics().horizontalAdvance('9') * digits
        return space

    def updateLineNumberAreaWidth(self, _):
        self.setViewportMargins(self.lineNumberAreaWidth(), 0, 0, 0)

    def updateLineNumberArea(self, rect, dy):
        if dy:
            self.lineNumberArea.scroll(0, dy)
        else:
            self.lineNumberArea.update(0, rect.y(), self.lineNumberArea.width(), rect.height())

        if rect.contains(self.viewport().rect()):
            self.updateLineNumberAreaWidth(0)

    def resizeEvent(self, event):
        super().resizeEvent(event)
        cr = self.contentsRect()
        self.lineNumberArea.setGeometry(QRect(cr.left(), cr.top(), self.lineNumberAreaWidth(), cr.height()))

    def lineNumberAreaPaintEvent(self, event):
        painter = QPainter(self.lineNumberArea)
        # painter.fillRect(event.rect(), Qt.lightGray)

        block = self.firstVisibleBlock()
        blockNumber = block.blockNumber()
        top = self.blockBoundingGeometry(block).translated(self.contentOffset()).top()
        bottom = top + self.blockBoundingRect(block).height()

        while block.isValid() and top <= event.rect().bottom():
            if block.isVisible() and bottom >= event.rect().top():
                number = str(blockNumber + 1)
                painter.setPen(Qt.black)
                painter.drawText(0, top, self.lineNumberArea.width(), self.fontMetrics().height(), Qt.AlignRight, number)

            block = block.next()
            top = bottom
            bottom = top + self.blockBoundingRect(block).height()
            blockNumber += 1

    def mousePressEvent(self, event):
        super().mousePressEvent(event)
        cursor = self.cursorForPosition(event.pos())
        block = cursor.block()
        blockNumber = block.blockNumber()
        self.currentLineNumber = blockNumber
        self.highlightCurrentLine()

    def keyPressEvent(self, event):
        super().keyPressEvent(event)
        cursor = self.textCursor()
        self.currentLineNumber = cursor.blockNumber()
        self.highlightCurrentLine()

    def highlightCurrentLine(self):
        extraSelections = []

        if self.currentLineNumber is not None:
            selection = QTextEdit.ExtraSelection()

            lineColor = self.currentLineColor

            selection.format.setBackground(lineColor)
            selection.format.setProperty(QTextFormat.FullWidthSelection, True)
            cursor = self.textCursor()
            cursor.movePosition(QTextCursor.Start)
            cursor.movePosition(QTextCursor.Down, QTextCursor.MoveAnchor, self.currentLineNumber)
            cursor.clearSelection()
            selection.cursor = cursor
            extraSelections.append(selection)

        self.setExtraSelections(extraSelections)
