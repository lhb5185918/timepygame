import pygame
import pygame_gui
import os
from data.collection_data import COLLECTIONS_DATA

def show_collection_interface(screen, manager):
    """显示收藏品界面"""
    # 获取屏幕尺寸
    WIDTH, HEIGHT = screen.get_size()
    
    # 创建半透明背景
    overlay = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
    overlay.fill((0, 0, 0, 180))  # 半透明黑色
    
    # 创建收藏品窗口
    collection_window = pygame_gui.elements.UIPanel(
        relative_rect=pygame.Rect((WIDTH//2 - 400, HEIGHT//2 - 300), (800, 600)),
        manager=manager,
        starting_height=2
    )
    
    # 收藏品标题
    collection_title = pygame_gui.elements.UILabel(
        relative_rect=pygame.Rect((10, 10), (730, 50)),
        text="我的收藏品",
        manager=manager,
        container=collection_window,
        object_id=pygame_gui.core.ObjectID(class_id='@title_labels', object_id='#collection_title')
    )
    
    collection_buttons = []
    y_offset = 70  # 初始纵向偏移
    
    # 使用导入的收藏品数据
    for category, items in COLLECTIONS_DATA.items():
        # 添加分类标题
        category_label = pygame_gui.elements.UILabel(
            relative_rect=pygame.Rect((20, y_offset), (200, 30)),
            text=f"【{category}】",
            manager=manager,
            container=collection_window,
            object_id=pygame_gui.core.ObjectID(class_id='@category_labels')
        )
        y_offset += 40  # 分类标题后的间距
        
        # 添加该分类下的收藏品按钮
        for item in items:
            btn = pygame_gui.elements.UIButton(
                relative_rect=pygame.Rect((40, y_offset), (250, 35)),
                text=item["name"],
                manager=manager,
                container=collection_window,
                object_id=pygame_gui.core.ObjectID(class_id='@buttons', object_id='#collection_button')
            )
            # 将图片信息也添加到按钮数据中
            item_data = (item["name"], item["desc"], btn)
            if "image" in item:
                item_data = (*item_data, item["image"])
            collection_buttons.append(item_data)
            y_offset += 45  # 按钮之间的间距
        
        y_offset += 20  # 分类之间的额外间距
    
    # 关闭按钮
    close_button = pygame_gui.elements.UIButton(
        relative_rect=pygame.Rect((750, 10), (40, 40)),
        text="X",
        manager=manager,
        container=collection_window
    )
    
    # 创建收藏品描述标签
    item_info_label = pygame_gui.elements.UITextBox(
        relative_rect=pygame.Rect((320, 70), (460, 200)),
        html_text="<font size=4>点击左侧收藏品查看详细信息</font>",
        manager=manager,
        container=collection_window,
        object_id=pygame_gui.core.ObjectID(class_id='@collection_description')
    )
    
    # 创建图片显示面板
    image_panel = pygame_gui.elements.UIPanel(
        relative_rect=pygame.Rect((320, 290), (460, 290)),
        manager=manager,
        container=collection_window,
        object_id=pygame_gui.core.ObjectID(class_id='@image_panel')
    )
    image_panel.hide()  # 初始时隐藏图片面板
    
    return close_button, overlay, collection_buttons, item_info_label, collection_window, image_panel 