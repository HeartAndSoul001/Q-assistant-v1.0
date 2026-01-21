from pathlib import Path
from PySide6.QtCore import QObject, Signal, QTimer

class StyleSignals(QObject):
    """样式加载信号类"""
    loaded = Signal(str)  # 样式加载完成信号


class qssLoader:
    """QSS 样式表加载器"""
    _style_cache = {}  # 类级别的样式缓存
    _signals = StyleSignals()
    _fallback_style = """
        QWidget {
            background-color: #f0f0f0;
            color: #333333;
        }
    """

    def __init__(self, path: str) -> None:
        """
        初始化 QSSLoader
        :param path: 样式表文件路径
        """
        self.path = Path(path)

    def _process_qss(self, content: str) -> str:
        """
        预处理 QSS 内容，移除注释和多余空白
        :param content: 原始 QSS 内容
        :return: 处理后的 QSS 内容
        """
        import re
        # 移除注释
        content = re.sub(r'/\*[\s\S]*?\*/', '', content)  # 多行注释
        content = re.sub(r'//.*?\n', '\n', content)       # 单行注释
        # 压缩空白字符
        return ' '.join(line.strip() for line in content.splitlines() if line.strip())

    def load(self) -> str:
        """
        加载并处理样式表
        :return: 加载的样式表内容
        """
        try:
            # 检查缓存
            if str(self.path) in self._style_cache:
                return self._style_cache[str(self.path)]

            # 检查文件是否存在
            if not self.path.exists():
                print(f"样式表文件不存在: {self.path}")
                return self._fallback_style

            # 读取并处理样式表
            with open(self.path, 'r', encoding='utf-8') as f:
                style = self._process_qss(f.read())
                self._style_cache[str(self.path)] = style  # 缓存样式表
                return style

        except Exception as e:
            print(f"加载样式表失败: {e}")
            return self._fallback_style

    @classmethod
    def async_load(cls, path: str):
        """
        异步加载样式表
        :param path: 样式表文件路径
        :return: 样式加载完成信号
        """
        def _load():
            try:
                style = cls(path).load()
                cls._signals.loaded.emit(style)
            except Exception as e:
                print(f"异步加载样式表失败: {e}")
                cls._signals.loaded.emit(cls._fallback_style)

        QTimer.singleShot(0, _load)
        return cls._signals.loaded

    @staticmethod
    def apply_stylesheet(widget, stylesheet: str):
        """
        应用样式表到指定的 QWidget
        :param widget: 目标 QWidget
        :param stylesheet: 样式表内容
        """
        widget.setStyleSheet(stylesheet)

    @classmethod
    def clear_cache(cls):
        """
        清空样式表缓存
        """
        cls._style_cache.clear()