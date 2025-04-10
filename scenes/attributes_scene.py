import pygame
import pygame_gui
from pygame_gui.elements import UIWindow, UIButton, UILabel, UITextBox, UIProgressBar
from data.player_attributes import ATTRIBUTES_DATA

def show_attributes_interface(screen, manager, attributes_data):
    """显示个人属性界面"""
    # 获取屏幕尺寸
    WIDTH, HEIGHT = screen.get_size()
    
    # 创建半透明背景
    overlay = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
    overlay.fill((0, 0, 0, 180))  # 半透明黑色
    
    # 创建属性窗口
    attributes_window = pygame_gui.elements.UIPanel(
        relative_rect=pygame.Rect((WIDTH//2 - 400, HEIGHT//2 - 300), (800, 600)),
        manager=manager,
        starting_height=2
    )
    
    # 属性标题
    attributes_title = pygame_gui.elements.UILabel(
        relative_rect=pygame.Rect((10, 10), (730, 50)),
        text="个人属性",
        manager=manager,
        container=attributes_window,
        object_id=pygame_gui.core.ObjectID(class_id='@title_labels', object_id='#attributes_title')
    )
    
    # 创建属性描述标签（调整位置到右侧）
    attribute_desc_label = pygame_gui.elements.UITextBox(
        relative_rect=pygame.Rect((450, 70), (330, 510)),  # 调整宽度和位置
        html_text='<font face="simhei" size=4><b>个人属性面板</b></font><br><br>'
                 '<font face="simhei" size=3>这里显示了你的各项属性数值。<br><br>'
                 '点击左侧属性名称可以查看详细说明。<br><br>'
                 '通过各种活动来提升属性值吧！</font>',
        manager=manager,
        container=attributes_window
    )
    
    # 创建属性元素列表
    attribute_elements = []
    y_offset = 70
    
    for attr_name, attr_data in attributes_data.items():
        # 创建属性按钮（调整位置）
        attr_button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect((20, y_offset), (100, 30)),  # 减小按钮宽度
            text=attr_name,
            manager=manager,
            container=attributes_window,
            object_id=pygame_gui.core.ObjectID(class_id='@buttons', object_id='#attribute_button')
        )
        
        # 创建进度条面板（调整位置）
        progress_bar_rect = pygame.Rect((130, y_offset), (200, 30))  # 调整进度条宽度和位置
        progress_panel = pygame_gui.elements.UIPanel(
            relative_rect=progress_bar_rect,
            manager=manager,
            container=attributes_window
        )
        
        # 创建进度条
        progress_bar_surface = pygame.Surface((200, 30))  # 调整surface大小
        try:
            # 加载进度条背景图片
            progress_bar_bg = pygame.image.load("assert/images/tiao.png").convert_alpha()
            progress_bar_bg = pygame.transform.scale(progress_bar_bg, (200, 30))  # 调整背景图片大小
            progress_bar_surface.blit(progress_bar_bg, (0, 0))
            
            # 计算填充宽度并绘制
            value = attr_data["value"]
            fill_width = int((value / 100.0) * 196)  # 调整填充宽度计算
            if fill_width > 0:
                pygame.draw.rect(progress_bar_surface, (0, 255, 0), (2, 2, fill_width, 26))
            
            # 设置进度条图像
            progress_panel.set_image(progress_bar_surface)
        except Exception as e:
            print(f"加载进度条背景图片时出错：{e}")
        
        # 创建属性值标签（调整位置）
        value_label = pygame_gui.elements.UILabel(
            relative_rect=pygame.Rect((progress_bar_rect.right + 10, y_offset), (80, 30)),  # 调整标签宽度
            text=f"{attr_data['value']:.2f}/100",
            manager=manager,
            container=attributes_window
        )
        
        # 将属性元素添加到列表
        attribute_elements.append({
            'name': attr_name,
            'value': attr_data["value"],
            'desc': attr_data["desc"],
            'button': attr_button,
            'progress_panel': progress_panel,
            'value_label': value_label
        })
        
        y_offset += 45  # 增加间距
    
    # 关闭按钮
    close_button = pygame_gui.elements.UIButton(
        relative_rect=pygame.Rect((750, 10), (40, 40)),
        text="×",
        manager=manager,
        container=attributes_window
    )
    
    return close_button, overlay, attribute_elements, attribute_desc_label, attributes_window

def update_attribute_value(attribute_elements, attr_name, new_value):
    """更新指定属性的值"""
    for attr in attribute_elements:
        if attr['name'] == attr_name:
            attr['value'] = min(100, new_value)  # 确保不超过100
            
            # 更新进度条显示
            if 'progress_panel' in attr:
                # 创建新的surface来绘制进度条
                progress_surface = pygame.Surface((200, 30), pygame.SRCALPHA)
                try:
                    # 加载并绘制背景图片
                    progress_bar_bg = pygame.image.load('assert/images/tiao.png').convert_alpha()
                    progress_bar_bg = pygame.transform.scale(progress_bar_bg, (200, 30))
                    progress_surface.blit(progress_bar_bg, (0, 0))
                    # 计算并绘制填充部分
                    fill_width = int((attr['value'] / 100.0) * 196)
                    if fill_width > 0:
                        pygame.draw.rect(progress_surface, (0, 255, 0, 200), (2, 2, fill_width, 26))
                    # 更新进度条显示
                    attr['progress_panel'].set_image(progress_surface)
                except Exception as e:
                    print(f"更新进度条时出错：{e}")
            
            # 更新数值标签
            attr['value_label'].set_text(f"{attr['value']:.2f}/100")
            break 