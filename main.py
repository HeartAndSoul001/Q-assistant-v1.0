import sys
from PySide6.QtWidgets import QApplication
from controllers import mainController
from utils import (qssLoader,iconManager)


def main():
    app = QApplication(sys.argv)

    # 初始化主页面控制器
    Controller = mainController()

    # 图标缓存对象
    iconManager()._ensure_initialized()

    # 异步加载样式表
    signal = qssLoader.async_load("resources/style.qss")
    # 连接信号，应用样式表
    signal.connect(lambda style: (
        app.setStyleSheet(style),
        Controller.show()
        ))
    


    sys.exit(app.exec())


if __name__ == '__main__':
    main()