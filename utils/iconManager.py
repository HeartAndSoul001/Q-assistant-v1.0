from PySide6.QtGui import QIcon
from PySide6.QtCore import QObject
import qtawesome as qta
from pathlib import Path
import logging


class iconManager(QObject):
    _instance = None
    _icons = {}
    _cache_dir = "resources/cache/icons"
    _initialized = False
    _font_css = """
    @font-face {
        font-family: "qtawesome";
        src: url("%(font_path)s");
    }
    """

    
    @classmethod
    def _ensure_initialized(cls):
        """确保类被初始化"""
        if not cls._initialized:
            cls._init_cache_dir()
            cls._icon_map = {
            'IP地址管理': 'mdi6.ip-network-outline',
            '配置处理': 'mdi6.application-edit',
            '工具箱': 'mdi6.tools',
            '子网计算器': 'mdi6.calculator',
            '格式转换': 'mdi6.application-brackets-outline',
            '集合运算': 'mdi6.set-center',
            '配置生成器': 'mdi6.book-plus-multiple-outline',
            '配置提取器': 'mdi6.book-search-outline',
            '复制内容到剪贴板': 'mdi6.content-copy',
            "清除内容": 'mdi6.undo',
            "从剪贴板粘贴": 'mdi6.content-paste',
            "信息查询": 'mdi6.text-search-variant',
            "IP访问信息查询": 'mdi6.file-find-outline',
            "tracert路由跟踪":'mdi6.transit-connection-horizontal',
            "警告提示":'ri.error-warning-line',
            "信息提示":'ri.information-fill',
        }
            cls._initialized = True
    
    @classmethod
    def _init_cache_dir(cls):
        """初始化缓存目录"""
        try:
            cache_path = Path(cls._cache_dir).absolute()
            cache_path.mkdir(parents=True, exist_ok=True)
            logging.info(f"缓存目录完整路径: {cache_path}")
        except Exception as e:
            logging.error(f"创建缓存目录失败: {e}")
    
    @classmethod
    def get_icon(cls, name: str, colo:str=None) -> QIcon:
        """获取图标"""
        cls._ensure_initialized()
        
        if name not in cls._icons:
            cache_path = Path(cls._cache_dir) / f"{name}.png"
            
            if cache_path.exists():
                logging.info(f"从缓存加载图标: {name}")
                cls._icons[name] = QIcon(str(cache_path))
            else:
                logging.info(f"从 qtawesome 加载图标: {name}")
                try:
                    # icon = qta.icon(cls._icon_map.get(name))
                    icon = qta.icon(cls._icon_map.get(name),color=colo)
                    cls._save_icon_to_cache(icon, name)
                    cls._icons[name] = icon
                except Exception as e:
                    logging.error(f"加载图标失败 {name}: {e}")
                    return QIcon()
                
        return cls._icons[name]
    
    @classmethod
    def _save_icon_to_cache(cls, icon: QIcon, name: str):
        """保存图标到缓存（PNG版本）"""
        try:
            cache_path = Path(cls._cache_dir) / f"{name}.png"
            
            # 创建透明背景的pixmap
            pixmap = icon.pixmap(128, 128)
            
            # 保存为PNG文件
            if pixmap.save(str(cache_path), "PNG"):
                logging.info(f"图标已缓存: {cache_path}")
            else:
                logging.error(f"图标缓存失败: {name}")
                
        except Exception as e:
            logging.error(f"保存图标缓存出错: {e}")
            
    @classmethod
    def clear_cache(cls):
        """清除所有缓存的图标"""
        try:
            cache_path = Path(cls._cache_dir)
            if cache_path.exists():
                for file in cache_path.glob("*.png"):
                    file.unlink()
                logging.info("图标缓存已清除")
        except Exception as e:
            logging.error(f"清除缓存失败: {e}")