from PySide6.QtWidgets import (QGraphicsItem, QGraphicsLineItem)
from PySide6.QtCore import (QRectF, QLineF)
from PySide6.QtGui import (QColor, QPen, QFont)

class DeviceNode(QGraphicsItem):  
    def __init__(self, device_name, ip, delays, parent=None):  
        super().__init__(parent)  
        self.device_name = device_name  # 设备名字（用户自定义对应关系）  
        self.ip = ip                    # IP地址  
        self.delays = delays            # 延迟列表 [delay1, delay2, delay3]  
        self.icon = self._load_icon()   # 设备图标（可选，如路由器/交换机图标）  
        self.setFlag(QGraphicsItem.ItemIsSelectable)  # 支持选中  
        self.setToolTip(f"IP: {ip}\n延迟: {delays} ms")  # 悬停显示详情  

    def boundingRect(self):  
        # 定义节点的边界矩形（用于碰撞检测和绘制范围）  
        return QRectF(0, 0, 180, 120)  # 宽180，高120的卡片  

    def paint(self, painter, option, widget):  
        # 绘制节点背景（卡片样式）  
        painter.setBrush(QColor(255, 255, 255))  # 白色背景  
        painter.setPen(QPen(QColor(200, 200, 200), 1))  # 灰色边框  
        painter.drawRoundedRect(self.boundingRect(), 8, 8)  # 圆角矩形  

        # 绘制设备图标（简化示例：用文本代替图标，实际可加载图片）  
        painter.setFont(QFont("Arial", 10, QFont.Bold))  
        painter.drawText(20, 30, "📡 设备")  # 用emoji或QPixmap加载图标  

        # 绘制设备名字（居中）  
        painter.setFont(QFont("Arial", 10))  
        painter.drawText(self.boundingRect().center().x() - 40, 60, self.device_name)  

        # 绘制IP地址  
        painter.setFont(QFont("Arial", 9))  
        painter.drawText(20, 85, f"IP: {self.ip}")  

        # 绘制延迟（用颜色区分延迟状态：绿色正常，红色超时）  
        avg_delay = sum(d for d in self.delays if d != "*") / len(self.delays) if any(d != "*" for d in self.delays) else "*"  
        if avg_delay == "*":  
            color = QColor(255, 0, 0)  # 超时标红  
        elif avg_delay > 100:  
            color = QColor(255, 165, 0)  # 高延迟标橙  
        else:  
            color = QColor(0, 128, 0)  # 正常标绿  
        painter.setPen(QPen(color))  
        painter.drawText(20, 105, f"延迟: {avg_delay:.2f} ms" if avg_delay != "*" else "延迟: 超时")  

    def _load_icon(self):  
        # 实际项目中可加载本地图标（如路由器图标.png）  
        # return QPixmap("router_icon.png").scaled(30, 30)  
        return None  # 简化示例，用文本代替
    
class PathLine(QGraphicsLineItem):  
    def __init__(self, start_node, end_node, delay_status="normal", parent=None):  
        super().__init__(parent)  
        # 连接两个节点的中心（假设节点锚点在左上角，需计算中心坐标）  
        start_pos = start_node.pos() + start_node.boundingRect().center()  
        end_pos = end_node.pos() + end_node.boundingRect().center()  
        self.setLine(QLineF(start_pos, end_pos))  

        # 根据延迟状态设置线条颜色  
        if delay_status == "high":  
            self.setPen(QPen(QColor(255, 0, 0), 2))  # 高延迟红线  
        else:  
            self.setPen(QPen(QColor(150, 150, 150), 1.5))  # 正常灰线  

        # 添加箭头（可选，需重写paint方法）  
        self.setArrowHead()  

    def setArrowHead(self):  
        # 绘制箭头（简化示例，实际需计算箭头角度）  
        pass  # 可参考Qt官方示例添加箭头  