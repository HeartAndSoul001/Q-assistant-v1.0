from PySide6.QtCore import (Signal, QThread)


class handleThread(QThread):
    finished = Signal(str)
    error = Signal(str)  # 新增一个信号用于传递错误信息

    def __init__(self, func, *args, **kwargs):
        super().__init__()
        self.func = func
        self.args = args
        self.kwargs = kwargs

    def run(self):
        try:
            self.result = self.func(*self.args, **self.kwargs)
            self.finished.emit(self.result)
        except Exception as e:
            self.error.emit(str(e))