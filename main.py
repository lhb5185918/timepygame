import pygame
import pygame_gui
import sys
import os
import shutil

# 初始化pygame
pygame.init()

# 屏幕设置
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("90后回忆游戏")

# 颜色定义
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

# 加载背景图片
def load_background():
    bg_path = os.path.join('assert', 'images', 'back_ground_picture.png')
    if os.path.exists(bg_path):
        # 加载背景图片
        background = pygame.image.load(bg_path)
        # 缩放到屏幕大小
        background = pygame.transform.scale(background, (WIDTH, HEIGHT))
        return background
    else:
        print(f"警告：找不到背景图片 {bg_path}")
        return None

def show_menu(screen):
    # 加载背景图片
    background = load_background()
    
    # 创建UI管理器
    manager = pygame_gui.UIManager((WIDTH, HEIGHT), 'data/themes/theme.json')
    
    # 创建标题标签
    title_label = pygame_gui.elements.UILabel(
        relative_rect=pygame.Rect((WIDTH//2 - 200, HEIGHT//4 - 40), (400, 80)),
        text="90后回忆游戏",
        manager=manager,
        object_id=pygame_gui.core.ObjectID(class_id='@title_labels', object_id='#title_label')
    )
    
    # 创建按钮
    start_button = pygame_gui.elements.UIButton(
        relative_rect=pygame.Rect((WIDTH//2 - 100, HEIGHT//2), (200, 50)),
        text="开始游戏",
        manager=manager,
        object_id=pygame_gui.core.ObjectID(class_id='@buttons', object_id='#start_button')
    )
    
    exit_button = pygame_gui.elements.UIButton(
        relative_rect=pygame.Rect((WIDTH//2 - 100, HEIGHT//2 + 80), (200, 50)),
        text="退出游戏",
        manager=manager,
        object_id=pygame_gui.core.ObjectID(class_id='@buttons', object_id='#exit_button')
    )
    
    # 创建时钟控制帧率
    clock = pygame.time.Clock()
    
    running = True
    while running:
        # 计算时间增量
        time_delta = clock.tick(60)/1000.0
        
        # 处理事件
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                
            # 处理UI事件
            if event.type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == start_button:
                    return "start_game"
                if event.ui_element == exit_button:
                    return "quit"
            
            # 将事件传递给UI管理器
            manager.process_events(event)
        
        # 更新UI
        manager.update(time_delta)
        
        # 清屏
        screen.fill(BLACK)
        
        # 绘制背景图片
        if background:
            screen.blit(background, (0, 0))
        
        # 绘制UI
        manager.draw_ui(screen)
        
        # 更新显示
        pygame.display.update()

def show_input_form(screen):
    # 加载背景图片
    background = load_background()
    
    # 加载新的背景图 - 90年代计算机和游戏背景
    form_bg_path = os.path.join('assert', 'images', 'back_ground_picture.png')
    if os.path.exists(form_bg_path):
        form_background = pygame.image.load(form_bg_path)
        form_background = pygame.transform.scale(form_background, (WIDTH, HEIGHT))
    else:
        form_background = background
    
    # 创建UI管理器
    manager = pygame_gui.UIManager((WIDTH, HEIGHT), 'data/themes/theme.json')
    
    # 创建表单标题
    form_title = pygame_gui.elements.UILabel(
        relative_rect=pygame.Rect((WIDTH//2 - 200, HEIGHT//4 - 40), (400, 60)),
        text="请输入您的信息",
        manager=manager,
        object_id=pygame_gui.core.ObjectID(class_id='@title_labels', object_id='#form_title')
    )
    
    # 创建姓名标签和输入框
    name_label = pygame_gui.elements.UILabel(
        relative_rect=pygame.Rect((WIDTH//2 - 200, HEIGHT//2 - 60), (100, 30)),
        text="姓名:",
        manager=manager
    )
    
    # 添加默认提示文本
    name_entry = pygame_gui.elements.UITextEntryLine(
        relative_rect=pygame.Rect((WIDTH//2 - 90, HEIGHT//2 - 60), (250, 30)),
        manager=manager,
        initial_text="请输入您的姓名"
    )
    
    # 创建年龄标签和输入框
    age_label = pygame_gui.elements.UILabel(
        relative_rect=pygame.Rect((WIDTH//2 - 200, HEIGHT//2 - 10), (100, 30)),
        text="年龄:",
        manager=manager
    )
    
    # 添加默认提示文本
    age_entry = pygame_gui.elements.UITextEntryLine(
        relative_rect=pygame.Rect((WIDTH//2 - 90, HEIGHT//2 - 10), (250, 30)),
        manager=manager,
        initial_text="请输入您的年龄"
    )
    
    # 限制年龄输入只能是数字
    age_entry.set_allowed_characters('numbers')
    
    # 创建确认按钮
    confirm_button = pygame_gui.elements.UIButton(
        relative_rect=pygame.Rect((WIDTH//2 - 100, HEIGHT//2 + 60), (200, 50)),
        text="开始",
        manager=manager,
        object_id=pygame_gui.core.ObjectID(class_id='@buttons', object_id='#confirm_button')
    )
    
    # 创建返回按钮
    back_button = pygame_gui.elements.UIButton(
        relative_rect=pygame.Rect((WIDTH//2 - 100, HEIGHT//2 + 130), (200, 50)),
        text="返回",
        manager=manager,
        object_id=pygame_gui.core.ObjectID(class_id='@buttons', object_id='#back_button')
    )
    
    # 创建提示信息标签（初始隐藏）
    info_label = pygame_gui.elements.UILabel(
        relative_rect=pygame.Rect((WIDTH//2 - 200, HEIGHT//2 + 30), (400, 25)),
        text="",
        manager=manager,
        visible=0
    )
    
    # 创建时钟控制帧率
    clock = pygame.time.Clock()
    
    running = True
    player_info = {"name": "", "age": 0}
    name_already_clicked = False
    age_already_clicked = False
    
    while running:
        # 计算时间增量
        time_delta = clock.tick(60)/1000.0
        
        # 处理事件
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                
            # 处理文本框获取焦点时，清除默认文本
            if event.type == pygame.MOUSEBUTTONDOWN:
                # 点击姓名输入框时，如果是第一次点击且内容是默认提示，则清空
                if name_entry.rect.collidepoint(event.pos):
                    if not name_already_clicked and name_entry.get_text() == "请输入您的姓名":
                        name_entry.set_text("")
                        name_already_clicked = True
                # 点击年龄输入框时，如果是第一次点击且内容是默认提示，则清空
                elif age_entry.rect.collidepoint(event.pos):
                    if not age_already_clicked and age_entry.get_text() == "请输入您的年龄":
                        age_entry.set_text("")
                        age_already_clicked = True
            
            # 处理UI事件
            if event.type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == confirm_button:
                    # 获取输入的姓名和年龄
                    name = name_entry.get_text()
                    age = age_entry.get_text()
                    
                    # 如果姓名是默认提示，视为未输入
                    if name == "请输入您的姓名":
                        name = ""
                    # 如果年龄是默认提示，视为未输入
                    if age == "请输入您的年龄":
                        age = ""
                    
                    # 验证输入
                    if not name:
                        info_label.set_text("请输入姓名")
                        info_label.show()
                    elif not age:
                        info_label.set_text("请输入年龄")
                        info_label.show()
                    else:
                        # 保存玩家信息
                        player_info["name"] = name
                        player_info["age"] = int(age)
                        # 进入卧室场景
                        return player_info
                
                if event.ui_element == back_button:
                    return None
            
            # 将事件传递给UI管理器
            manager.process_events(event)
        
        # 更新UI
        manager.update(time_delta)
        
        # 清屏
        screen.fill(BLACK)
        
        # 绘制背景图片
        if form_background:
            screen.blit(form_background, (0, 0))
        
        # 绘制UI
        manager.draw_ui(screen)
        
        # 更新显示
        pygame.display.update()

def start_game(player_info):
    # 导入卧室场景模块
    from bedroom_scene import show_bedroom_scene
    # 导入客厅场景模块
    from living_room_scene import show_living_room_scene
    
    # 显示卧室场景
    result = show_bedroom_scene(screen, player_info)
    return result

def setup_fonts():
    # 创建字体目录
    os.makedirs('data/fonts', exist_ok=True)
    
    # 获取系统字体
    system_fonts_dir = None
    if os.name == 'nt':  # Windows
        system_fonts_dir = os.path.join(os.environ['WINDIR'], 'Fonts')
    
    if system_fonts_dir and os.path.exists(system_fonts_dir):
        # 尝试复制黑体（简体中文Windows通常有）
        try:
            simhei_path = os.path.join(system_fonts_dir, 'simhei.ttf')
            if os.path.exists(simhei_path):
                try:
                    shutil.copy2(simhei_path, 'data/fonts/simhei.ttf')
                    print(f"复制字体成功: {simhei_path} -> data/fonts/simhei.ttf")
                except Exception as e:
                    print(f"复制字体出错: {e}")
                    # 如果复制失败，但文件已存在，则继续执行
                    if not os.path.exists('data/fonts/simhei.ttf'):
                        print("警告：字体文件无法复制，游戏文字可能显示异常")
            else:
                print(f"找不到字体文件: {simhei_path}")
                
            # 备用方案：复制其他可能支持中文的字体
            msyh_path = os.path.join(system_fonts_dir, 'msyh.ttc')  # 微软雅黑
            if os.path.exists(msyh_path):
                try:
                    shutil.copy2(msyh_path, 'data/fonts/msyh.ttc')
                    print(f"复制备用字体成功: {msyh_path} -> data/fonts/msyh.ttc")
                except Exception as e:
                    print(f"复制备用字体出错: {e}")
                    # 如果复制失败，但文件已存在，则继续执行
                    if not os.path.exists('data/fonts/msyh.ttc'):
                        print("警告：备用字体无法复制，游戏文字可能显示异常")
        except Exception as e:
            print(f"字体处理过程中出错: {e}")
            print("继续执行游戏，但文字可能显示异常")

def create_theme_file():
    # 确保data/themes目录存在
    os.makedirs('data/themes', exist_ok=True)
    
    # 获取可用的中文字体路径
    font_path = 'data/fonts/simhei.ttf'
    if not os.path.exists(font_path):
        # 尝试备用字体
        font_path = 'data/fonts/msyh.ttc'
        if not os.path.exists(font_path):
            # 如果没有中文字体，则使用系统默认字体
            font_path = None
    
    # 使用字体名称
    font_name = 'simhei' if 'simhei' in str(font_path) else 'msyh' if font_path and 'msyh' in str(font_path) else 'freesans'
    
    # 创建主题文件
    theme_json = f'''{{
        "defaults":
        {{
            "colours":
            {{
                "normal_bg": "#3B88C3",
                "hovered_bg": "#5C9BD1",
                "disabled_bg": "#25567B",
                "selected_bg": "#25567B",
                "active_bg": "#193754",
                "normal_text": "#FFFFFF",
                "hovered_text": "#FFFFFF",
                "selected_text": "#FFFFFF",
                "disabled_text": "#6d736f",
                "active_text": "#FFFFFF",
                "normal_border": "#FFFFFF",
                "hovered_border": "#FFFFFF",
                "disabled_border": "#FFFFFF",
                "selected_border": "#FFFFFF",
                "active_border": "#FFFFFF"
            }},
            "font":
            {{
                "name": "{font_name}",
                "size": "24",
                "bold": "0",
                "italic": "0"
                {f',"regular_path": "{font_path}"' if font_path else ''}
            }}
        }},
        "@title_labels":
        {{
            "colours":
            {{
                "normal_text": "#FFFFFF",
                "dark_bg": "#00000000"
            }},
            "font":
            {{
                "name": "{font_name}",
                "size": "42",
                "bold": "1",
                "italic": "0"
                {f',"regular_path": "{font_path}"' if font_path else ''}
            }}
        }},
        "@buttons":
        {{
            "misc":
            {{
                "shape": "rounded_rectangle",
                "shape_corner_radius": "10",
                "border_width": "2"
            }},
            "font":
            {{
                "name": "{font_name}",
                "size": "24",
                "bold": "1",
                "italic": "0"
                {f',"regular_path": "{font_path}"' if font_path else ''}
            }}
        }},
        "@transparent_buttons":
        {{
            "colours":
            {{
                "normal_bg": "#00000000",
                "hovered_bg": "#FFFFFF33",
                "disabled_bg": "#00000000",
                "selected_bg": "#FFFFFF44",
                "active_bg": "#FFFFFF22",
                "normal_text": "#FFFFFF00",
                "hovered_text": "#FFFFFF",
                "selected_text": "#FFFFFF",
                "disabled_text": "#6d736f",
                "active_text": "#FFFFFF",
                "normal_border": "#FFFFFF00",
                "hovered_border": "#FFFFFF77",
                "disabled_border": "#FFFFFF00",
                "selected_border": "#FFFFFFAA",
                "active_border": "#FFFFFF88"
            }},
            "misc":
            {{
                "shape": "rounded_rectangle",
                "shape_corner_radius": "10",
                "border_width": "1",
                "shadow_width": "0"
            }},
            "font":
            {{
                "name": "{font_name}",
                "size": "24",
                "bold": "0",
                "italic": "0"
                {f',"regular_path": "{font_path}"' if font_path else ''}
            }}
        }},
        "#item_button":
        {{
            "colours":
            {{
                "normal_bg": "#555577",
                "hovered_bg": "#7777AA",
                "disabled_bg": "#25567B",
                "selected_bg": "#25567B",
                "active_bg": "#193754",
                "normal_text": "#FFFFFF",
                "hovered_text": "#FFFFFF",
                "selected_text": "#FFFFFF",
                "disabled_text": "#6d736f",
                "active_text": "#FFFFFF",
                "normal_border": "#AAAAFF",
                "hovered_border": "#FFFFFF",
                "disabled_border": "#FFFFFF",
                "selected_border": "#FFFFFF",
                "active_border": "#FFFFFF"
            }},
            "misc":
            {{
                "shape": "rounded_rectangle",
                "shape_corner_radius": "5",
                "border_width": "1",
                "shadow_width": "1"
            }},
            "font":
            {{
                "name": "{font_name}",
                "size": "20",
                "bold": "1",
                "italic": "0"
                {f',"regular_path": "{font_path}"' if font_path else ''}
            }}
        }},
        "#clock_label":
        {{
            "colours":
            {{
                "normal_text": "#FFCC00",
                "dark_bg": "#00000000"
            }},
            "font":
            {{
                "name": "{font_name}",
                "size": "26",
                "bold": "1",
                "italic": "0"
                {f',"regular_path": "{font_path}"' if font_path else ''}
            }}
        }},
        "#explore_button":
        {{
            "colours":
            {{
                "normal_bg": "#008800",
                "hovered_bg": "#00AA00",
                "disabled_bg": "#25567B",
                "selected_bg": "#25567B",
                "active_bg": "#006600",
                "normal_text": "#FFFFFF",
                "hovered_text": "#FFFFFF",
                "selected_text": "#FFFFFF",
                "disabled_text": "#6d736f",
                "active_text": "#FFFFFF",
                "normal_border": "#00FF00",
                "hovered_border": "#FFFFFF",
                "disabled_border": "#FFFFFF",
                "selected_border": "#FFFFFF",
                "active_border": "#FFFFFF"
            }},
            "misc":
            {{
                "shape": "rounded_rectangle",
                "shape_corner_radius": "5",
                "border_width": "1",
                "shadow_width": "1"
            }},
            "font":
            {{
                "name": "{font_name}",
                "size": "18",
                "bold": "1",
                "italic": "0"
                {f',"regular_path": "{font_path}"' if font_path else ''}
            }}
        }},
        "#text_entry_line":
        {{
            "colours":
            {{
                "dark_bg": "#222222",
                "normal_text": "#BBBBBB"
            }},
            "font":
            {{
                "name": "{font_name}",
                "size": "20",
                "bold": "0",
                "italic": "0"
                {f',"regular_path": "{font_path}"' if font_path else ''}
            }}
        }},
        "#start_button":
        {{
            "colours":
            {{
                "normal_bg": "#0066CC",
                "hovered_bg": "#FFCC00",
                "disabled_bg": "#25567B",
                "selected_bg": "#25567B",
                "active_bg": "#193754"
            }},
            "font":
            {{
                "name": "{font_name}",
                "size": "24",
                "bold": "1",
                "italic": "0"
                {f',"regular_path": "{font_path}"' if font_path else ''}
            }}
        }},
        "#exit_button":
        {{
            "colours":
            {{
                "normal_bg": "#CC0000",
                "hovered_bg": "#FFCC00",
                "disabled_bg": "#25567B",
                "selected_bg": "#25567B",
                "active_bg": "#193754"
            }},
            "font":
            {{
                "name": "{font_name}",
                "size": "24",
                "bold": "1",
                "italic": "0"
                {f',"regular_path": "{font_path}"' if font_path else ''}
            }}
        }},
        "#confirm_button":
        {{
            "colours":
            {{
                "normal_bg": "#33CC33",
                "hovered_bg": "#FFCC00",
                "disabled_bg": "#25567B",
                "selected_bg": "#25567B",
                "active_bg": "#193754"
            }},
            "font":
            {{
                "name": "{font_name}",
                "size": "24",
                "bold": "1",
                "italic": "0"
                {f',"regular_path": "{font_path}"' if font_path else ''}
            }}
        }},
        "#back_button":
        {{
            "colours":
            {{
                "normal_bg": "#CC6600",
                "hovered_bg": "#FFCC00",
                "disabled_bg": "#25567B",
                "selected_bg": "#25567B",
                "active_bg": "#193754"
            }},
            "font":
            {{
                "name": "{font_name}",
                "size": "24",
                "bold": "1",
                "italic": "0"
                {f',"regular_path": "{font_path}"' if font_path else ''}
            }}
        }},
        "#computer_title":
        {{
            "font":
            {{
                "name": "{font_name}",
                "size": "32",
                "bold": "1",
                "italic": "0"
                {f',"regular_path": "{font_path}"' if font_path else ''}
            }}
        }}
    }}'''
    
    with open('data/themes/theme.json', 'w', encoding='utf-8') as file:
        file.write(theme_json)

def main():
    # 设置字体
    setup_fonts()
    
    # 创建主题文件
    create_theme_file()
    
    # 游戏主循环
    current_scene = "menu"
    running = True
    while running:
        if current_scene == "menu":
            result = show_menu(screen)
            if result == "start_game":
                current_scene = "input_form"
            elif result == "quit":
                running = False
                
        elif current_scene == "input_form":
            player_info = show_input_form(screen)
            if player_info:
                current_scene = "bedroom"
            else:
                current_scene = "menu"
                
        elif current_scene == "bedroom":
            from bedroom_scene import show_bedroom_scene
            result = show_bedroom_scene(screen, player_info)
            if result == "back_to_menu":
                current_scene = "menu"
            elif result == "go_to_living_room":
                current_scene = "living_room"
                
        elif current_scene == "living_room":
            from living_room_scene import show_living_room_scene
            result = show_living_room_scene(screen, player_info)
            if result == "back_to_bedroom":
                current_scene = "bedroom"
            elif result == "back_to_menu":
                current_scene = "menu"

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main() 