import pygame
import pygame_gui
import sys
import os
import datetime  # 导入日期时间模块
from utils.time_system import GameTimeSystem  # 导入游戏时间系统
from data.book_data import BOOKS_DATA  # 导入书籍数据
from scenes.collection_scene import show_collection_interface  # 导入收藏品界面

def load_bedroom_background(game_time=None):
    """加载卧室场景背景图片，根据时间显示不同的光照效果"""
    light_condition = "twilight"  # 默认为黎明/黄昏效果
    
    # 根据时间判断加载哪张背景图片
    if game_time is not None:
        light_condition = game_time.get_light_condition()
    
    # 根据光照条件选择背景图片
    if light_condition == "night":
        bg_path = os.path.join('assert', 'images', 'home_loft_night.png')  # 夜间亮灯版本
    elif light_condition == "day":
        bg_path = os.path.join('assert', 'images', 'home_loft_day.png')  # 正午全亮版本
    else:  # twilight
        bg_path = os.path.join('assert', 'images', 'home_loft_picture.png')  # 默认版本
        
    # 检查指定的图片是否存在，不存在则使用默认图片
    if not os.path.exists(bg_path):
        print(f"警告：找不到背景图片 {bg_path}，使用默认背景")
        bg_path = os.path.join('assert', 'images', 'home_loft_picture.png')
        # 如果默认图片也不存在，则返回None
        if not os.path.exists(bg_path):
            print(f"警告：找不到默认背景图片 {bg_path}")
            return None
            
    # 加载背景图片
    background = pygame.image.load(bg_path)
    # 缩放到屏幕大小
    width, height = pygame.display.get_surface().get_size()
    background = pygame.transform.scale(background, (width, height))
    return background

def show_computer_interface(screen, manager, player_info, game_time):
    """显示电脑界面"""
    # 获取屏幕尺寸
    WIDTH, HEIGHT = screen.get_size()
    
    # 创建半透明背景
    overlay = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
    overlay.fill((0, 0, 0, 180))  # 半透明黑色
    
    # 加载电脑桌面背景图片
    computer_desk_path = os.path.join('assert', 'images', 'computer_desk.png')
    if os.path.exists(computer_desk_path):
        try:
            # 加载背景图片
            computer_desk = pygame.image.load(computer_desk_path).convert_alpha()
            computer_desk = pygame.transform.scale(computer_desk, (600, 400))
            # 创建一个带背景图的面板
            panel_surface = pygame.Surface((600, 400))
            panel_surface.blit(computer_desk, (0, 0))
        except Exception as e:
            print(f"加载电脑桌面图片时出错：{e}")
            panel_surface = pygame.Surface((600, 400))
            panel_surface.fill((40, 40, 40))  # 深灰色背景
    else:
        panel_surface = pygame.Surface((600, 400))
        panel_surface.fill((40, 40, 40))  # 深灰色背景
    
    # 创建电脑窗口
    computer_window = pygame_gui.elements.UIPanel(
        relative_rect=pygame.Rect((WIDTH//2 - 300, HEIGHT//2 - 200), (600, 400)),
        manager=manager,
        starting_height=2
    )
    
    # 设置面板背景
    computer_window.set_image(panel_surface)
    
    # 电脑标题
    computer_title = pygame_gui.elements.UILabel(
        relative_rect=pygame.Rect((10, 10), (580, 50)),
        text="90年代小霸王电脑",
        manager=manager,
        container=computer_window,
        object_id=pygame_gui.core.ObjectID(class_id='@title_labels', object_id='#computer_title')
    )
    
    # 创建时间显示标签 - 使用游戏内时间
    formatted_time = game_time.get_formatted_time()
    blink_char = "|"  # 初始闪烁字符
    
    time_label = pygame_gui.elements.UILabel(
        relative_rect=pygame.Rect((10, 60), (200, 30)),
        text=f"时间: {formatted_time} {blink_char}",
        manager=manager,
        container=computer_window
    )
    
    # 添加一些电脑程序按钮
    programs = [
        {"name": "扫雷游戏", "pos": (450, 100)},
        {"name": "画图工具", "pos": (450, 140)},
        {"name": "记事本", "pos": (450, 180)},
        {"name": "QQ聊天", "pos": (450, 220)},
        {"name": "红色警戒", "pos": (450, 260)},
        {"name": "仙剑奇侠传", "pos": (450, 300)},
        {"name": "魔兽争霸", "pos": (450, 340)},
        {"name": "金山打字通", "pos": (450, 380)}
    ]
    
    program_buttons = []
    for program in programs:
        btn = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect(program["pos"], (130, 25)),
            text=program["name"],
            manager=manager,
            container=computer_window,
            object_id=pygame_gui.core.ObjectID(class_id='@buttons', object_id='#item_button')
        )
        program_buttons.append(btn)
    
    # 关闭按钮
    close_button = pygame_gui.elements.UIButton(
        relative_rect=pygame.Rect((550, 10), (40, 40)),
        text="X",
        manager=manager,
        container=computer_window
    )
    
    # 创建信息标签 - 增加宽度确保更长的文本能显示
    info_label = pygame_gui.elements.UILabel(
        relative_rect=pygame.Rect((150, 350), (280, 30)),
        text="",
        manager=manager,
        container=computer_window,
        visible=0
    )
    
    # 返回创建的元素
    return close_button, overlay, program_buttons, info_label, computer_window, time_label

def show_bookshelf_interface(screen, manager):
    """显示书架界面"""
    # 获取屏幕尺寸
    WIDTH, HEIGHT = screen.get_size()
    
    # 创建半透明背景
    overlay = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
    overlay.fill((0, 0, 0, 180))  # 半透明黑色
    
    # 创建书架窗口 - 调整窗口大小
    bookshelf_window = pygame_gui.elements.UIPanel(
        relative_rect=pygame.Rect((WIDTH//2 - 400, HEIGHT//2 - 300), (800, 600)),
        manager=manager,
        starting_height=2
    )
    
    # 书架标题
    bookshelf_title = pygame_gui.elements.UILabel(
        relative_rect=pygame.Rect((10, 10), (730, 50)),
        text="我的书架",
        manager=manager,
        container=bookshelf_window,
        object_id=pygame_gui.core.ObjectID(class_id='@title_labels', object_id='#bookshelf_title')
    )
    
    book_buttons = []
    y_offset = 70  # 初始纵向偏移
    
    # 使用导入的书籍数据
    for category, book_list in BOOKS_DATA.items():
        # 添加分类标题
        category_label = pygame_gui.elements.UILabel(
            relative_rect=pygame.Rect((20, y_offset), (200, 30)),
            text=f"【{category}】",
            manager=manager,
            container=bookshelf_window,
            object_id=pygame_gui.core.ObjectID(class_id='@category_labels')
        )
        y_offset += 40  # 分类标题后的间距
        
        # 添加该分类下的书籍按钮
        for book in book_list:
            btn = pygame_gui.elements.UIButton(
                relative_rect=pygame.Rect((40, y_offset), (250, 35)),
                text=book["name"],
                manager=manager,
                container=bookshelf_window,
                object_id=pygame_gui.core.ObjectID(class_id='@buttons', object_id='#book_button')
            )
            # 将图片信息也添加到按钮数据中
            book_data = (book["name"], book["desc"], btn)
            if "image" in book:
                book_data = (*book_data, book["image"])
            book_buttons.append(book_data)
            y_offset += 45  # 按钮之间的间距
        
        y_offset += 20  # 分类之间的额外间距
    
    # 关闭按钮
    close_button = pygame_gui.elements.UIButton(
        relative_rect=pygame.Rect((750, 10), (40, 40)),
        text="X",
        manager=manager,
        container=bookshelf_window
    )
    
    # 创建书籍描述标签 - 调整位置和大小，放在右上方
    book_info_label = pygame_gui.elements.UITextBox(
        relative_rect=pygame.Rect((320, 70), (460, 200)),
        html_text="<font size=4>点击左侧书籍查看详细信息</font>",
        manager=manager,
        container=bookshelf_window,
        object_id=pygame_gui.core.ObjectID(class_id='@book_description')
    )
    
    # 创建图片显示面板 - 放在右下方
    image_panel = pygame_gui.elements.UIPanel(
        relative_rect=pygame.Rect((320, 290), (460, 290)),  # 调整位置和大小
        manager=manager,
        container=bookshelf_window,
        object_id=pygame_gui.core.ObjectID(class_id='@image_panel')
    )
    
    # 预加载三国演义图片
    try:
        image_path = os.path.join('assert', 'images', 'sanguoyanyi.png')
        if os.path.exists(image_path):
            sanguoyanyi_image = pygame.image.load(image_path)
            # 缩放图片以适应面板大小
            sanguoyanyi_image = pygame.transform.scale(sanguoyanyi_image, (460, 290))
            # 转换图片格式
            sanguoyanyi_image = sanguoyanyi_image.convert_alpha()
            image_panel.set_image(sanguoyanyi_image)
            # 初始时隐藏图片
            image_panel.hide()
    except Exception as e:
        print(f"预加载三国演义图片时出错：{e}")
    
    return close_button, overlay, book_buttons, book_info_label, bookshelf_window, image_panel

def show_desk_interface(screen, manager):
    """显示书桌界面"""
    # 获取屏幕尺寸
    WIDTH, HEIGHT = screen.get_size()
    
    # 创建半透明背景
    overlay = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
    overlay.fill((0, 0, 0, 180))  # 半透明黑色
    
    # 创建书桌窗口
    desk_window = pygame_gui.elements.UIPanel(
        relative_rect=pygame.Rect((WIDTH//2 - 300, HEIGHT//2 - 200), (600, 400)),
        manager=manager,
        starting_height=2
    )
    
    # 书桌标题
    desk_title = pygame_gui.elements.UILabel(
        relative_rect=pygame.Rect((10, 10), (530, 50)),
        text="我的书桌",
        manager=manager,
        container=desk_window,
        object_id=pygame_gui.core.ObjectID(class_id='@title_labels', object_id='#desk_title')
    )
    
    # 添加书桌物品列表
    desk_items = [
        {"name": "台灯", "desc": "一盏可调节亮度的LED台灯，照明效果很好。"},
        {"name": "笔筒", "desc": "里面放着各种笔：铅笔、钢笔、圆珠笔等。"},
        {"name": "课本", "desc": "整齐摆放的各科课本，等待被翻开。"},
        {"name": "笔记本", "desc": "记录学习心得的笔记本，写满了重要知识点。"},
        {"name": "计算器", "desc": "一个科学计算器，解决数学问题的好帮手。"},
        {"name": "文具盒", "desc": "装满了橡皮、尺子、圆规等文具。"},
        {"name": "相框", "desc": "放着一张全家福，温馨的回忆。"},
        {"name": "小闹钟", "desc": "帮助按时起床的好伙伴。"}
    ]
    
    desk_item_buttons = []
    for i, item in enumerate(desk_items):
        btn = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect((20, 70 + i * 40), (200, 30)),
            text=item["name"],
            manager=manager,
            container=desk_window,
            object_id=pygame_gui.core.ObjectID(class_id='@buttons', object_id='#desk_item_button')
        )
        desk_item_buttons.append((item["name"], item["desc"], btn))
    
    # 关闭按钮
    close_button = pygame_gui.elements.UIButton(
        relative_rect=pygame.Rect((550, 10), (40, 40)),
        text="X",
        manager=manager,
        container=desk_window
    )
    
    # 创建物品描述标签
    item_info_label = pygame_gui.elements.UILabel(
        relative_rect=pygame.Rect((250, 70), (330, 300)),
        text="点击左侧物品查看详细信息",
        manager=manager,
        container=desk_window
    )
    
    return close_button, overlay, desk_item_buttons, item_info_label, desk_window

def show_bed_interface(screen, manager, game_time):
    """显示床铺界面"""
    # 获取屏幕尺寸
    WIDTH, HEIGHT = screen.get_size()
    
    # 创建半透明背景
    overlay = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
    overlay.fill((0, 0, 0, 180))  # 半透明黑色
    
    # 创建床铺窗口
    bed_window = pygame_gui.elements.UIPanel(
        relative_rect=pygame.Rect((WIDTH//2 - 200, HEIGHT//2 - 150), (400, 300)),
        manager=manager,
        starting_height=2
    )
    
    # 床铺标题
    bed_title = pygame_gui.elements.UILabel(
        relative_rect=pygame.Rect((10, 10), (330, 50)),
        text="休息时间",
        manager=manager,
        container=bed_window,
        object_id=pygame_gui.core.ObjectID(class_id='@title_labels', object_id='#bed_title')
    )
    
    # 当前时间显示
    current_time_label = pygame_gui.elements.UILabel(
        relative_rect=pygame.Rect((10, 70), (330, 30)),
        text=f"当前时间：{game_time.get_formatted_time()}",
        manager=manager,
        container=bed_window
    )
    
    # 小睡按钮
    nap_button = pygame_gui.elements.UIButton(
        relative_rect=pygame.Rect((50, 120), (300, 50)),
        text="小睡一下 (消耗2小时)",
        manager=manager,
        container=bed_window,
        object_id=pygame_gui.core.ObjectID(class_id='@buttons', object_id='#nap_button')
    )
    
    # 正常睡眠按钮
    sleep_button = pygame_gui.elements.UIButton(
        relative_rect=pygame.Rect((50, 180), (300, 50)),
        text="正常睡觉 (消耗8小时)",
        manager=manager,
        container=bed_window,
        object_id=pygame_gui.core.ObjectID(class_id='@buttons', object_id='#sleep_button')
    )
    
    # 关闭按钮
    close_button = pygame_gui.elements.UIButton(
        relative_rect=pygame.Rect((350, 10), (40, 40)),
        text="X",
        manager=manager,
        container=bed_window
    )
    
    # 创建睡眠结果标签
    sleep_info_label = pygame_gui.elements.UILabel(
        relative_rect=pygame.Rect((20, 240), (360, 50)),
        text="",
        manager=manager,
        container=bed_window,
        visible=0
    )
    
    return close_button, overlay, nap_button, sleep_button, current_time_label, sleep_info_label, bed_window

def show_bedroom_scene(screen, player_info):
    """显示卧室场景"""
    # 获取屏幕尺寸
    WIDTH, HEIGHT = screen.get_size()
    
    # 创建UI管理器
    manager = pygame_gui.UIManager((WIDTH, HEIGHT), 'data/themes/theme.json')
    
    # 初始化游戏时间系统（从2000年1月1日上午9点开始）
    game_time = GameTimeSystem(year=2000, month=1, day=1, hour=9, minute=0)
    
    # 根据当前时间加载背景
    background = load_bedroom_background(game_time)
    
    # 显示玩家信息 - 增加宽度以适应更长的名字
    player_info_label = pygame_gui.elements.UILabel(
        relative_rect=pygame.Rect((20, 20), (250, 30)),
        text=f"玩家: {player_info['name']} | {player_info['age']}岁",
        manager=manager
    )
    
    # 创建返回主菜单按钮
    back_button = pygame_gui.elements.UIButton(
        relative_rect=pygame.Rect((WIDTH - 150, 20), (130, 40)),
        text="返回主菜单",
        manager=manager,
        object_id=pygame_gui.core.ObjectID(class_id='@buttons', object_id='#back_button')
    )
    
    # 创建时钟显示 - 包含季节、月份、日期和时间
    clock_label = pygame_gui.elements.UILabel(
        relative_rect=pygame.Rect((WIDTH - 350, 70), (320, 40)),
        text=game_time.get_formatted_full_display(),
        manager=manager,
        object_id=pygame_gui.core.ObjectID(class_id='@title_labels', object_id='#clock_label')
    )
    
    # 创建探索按钮
    explore_button = pygame_gui.elements.UIButton(
        relative_rect=pygame.Rect((WIDTH - 180, 120), (150, 40)),
        text="探索 (+1小时)",
        manager=manager,
        object_id=pygame_gui.core.ObjectID(class_id='@buttons', object_id='#explore_button')
    )
    
    # 创建信息标签
    info_label = pygame_gui.elements.UILabel(
        relative_rect=pygame.Rect((WIDTH//2 - 300, HEIGHT - 100), (600, 50)),
        text="",
        manager=manager,
        visible=0
    )
    
    # 卧室中可交互物品的描述信息
    items_info = {
        "电脑": "这是90年代的小霸王电脑，陪伴了许多90后的童年。",
        "床": "舒适的单人床，红色的被子看起来很温暖。",
        "书桌": "一张木质书桌，上面放着各种学习和娱乐用品。",
        "书架": "满是各种书籍和杂志的书架，知识的宝库。",
        "客厅": "通往客厅的门。"
    }
    
    # 创建明确的交互按钮，而不是透明按钮
    interaction_buttons = []
    
    # 创建电脑按钮 - 将按钮放置在左侧，垂直排列
    computer_button = pygame_gui.elements.UIButton(
        relative_rect=pygame.Rect((30, 150), (120, 40)),
        text="电脑",
        manager=manager,
        object_id=pygame_gui.core.ObjectID(class_id='@buttons', object_id='#item_button')
    )
    interaction_buttons.append(("电脑", computer_button))
    
    # 创建书架按钮
    bookshelf_button = pygame_gui.elements.UIButton(
        relative_rect=pygame.Rect((30, 200), (120, 40)),
        text="书架",
        manager=manager,
        object_id=pygame_gui.core.ObjectID(class_id='@buttons', object_id='#item_button')
    )
    interaction_buttons.append(("书架", bookshelf_button))
    
    # 创建书桌按钮
    desk_button = pygame_gui.elements.UIButton(
        relative_rect=pygame.Rect((30, 250), (120, 40)),
        text="书桌",
        manager=manager,
        object_id=pygame_gui.core.ObjectID(class_id='@buttons', object_id='#item_button')
    )
    interaction_buttons.append(("书桌", desk_button))
    
    # 创建床按钮
    bed_button = pygame_gui.elements.UIButton(
        relative_rect=pygame.Rect((30, 300), (120, 40)),
        text="床",
        manager=manager,
        object_id=pygame_gui.core.ObjectID(class_id='@buttons', object_id='#item_button')
    )
    interaction_buttons.append(("床", bed_button))

    # 创建客厅按钮
    living_room_button = pygame_gui.elements.UIButton(
        relative_rect=pygame.Rect((30, 350), (120, 40)),
        text="客厅",
        manager=manager,
        object_id=pygame_gui.core.ObjectID(class_id='@buttons', object_id='#item_button')
    )
    interaction_buttons.append(("客厅", living_room_button))
    
    # 创建收藏品按钮
    collection_button = pygame_gui.elements.UIButton(
        relative_rect=pygame.Rect((30, 400), (120, 40)),
        text="收藏品",
        manager=manager,
        object_id=pygame_gui.core.ObjectID(class_id='@buttons', object_id='#item_button')
    )
    interaction_buttons.append(("收藏品", collection_button))
    
    # 电脑界面元素初始化为None
    close_button = None
    computer_overlay = None
    program_buttons = None
    computer_info_label = None
    computer_window = None
    time_label = None
    
    # 在running = True之前添加书架界面相关变量
    showing_bookshelf = False
    bookshelf_close_button = None
    bookshelf_overlay = None
    book_buttons = None
    book_info_label = None
    bookshelf_window = None
    book_image_panel = None  # 添加图片面板变量
    
    # 在电脑和书架界面变量初始化后添加书桌界面变量
    showing_desk = False
    desk_close_button = None
    desk_overlay = None
    desk_item_buttons = None
    desk_info_label = None
    desk_window = None
    
    # 在其他界面变量初始化后添加床铺界面变量
    showing_bed = False
    bed_close_button = None
    bed_overlay = None
    nap_button = None
    sleep_button = None
    current_time_label = None
    sleep_info_label = None
    bed_window = None
    
    # 添加收藏品界面相关变量
    showing_collection = False
    collection_close_button = None
    collection_overlay = None
    collection_buttons = None
    collection_info_label = None
    collection_window = None
    collection_image_panel = None
    
    # 创建时钟控制帧率
    clock = pygame.time.Clock()
    
    running = True
    showing_computer = False
    
    # 用于时间闪烁效果的变量
    blink_timer = 0
    blink_state = True
    
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
                if event.ui_element == back_button:
                    return "back_to_menu"
                
                # 处理探索按钮点击
                if event.ui_element == explore_button:
                    # 增加游戏内时间1小时
                    game_time.advance_time(hours=1)
                    
                    # 更新时钟显示
                    clock_label.set_text(game_time.get_formatted_full_display())
                    
                    # 添加探索信息提示
                    formatted_time = game_time.get_formatted_time()
                    info_label.set_text(f"你花了1小时探索卧室，现在是{formatted_time}")
                    info_label.show()
                    
                    # 根据新的时间更新背景
                    background = load_bedroom_background(game_time)
                
                # 检查是否点击了交互按钮
                for item_name, button in interaction_buttons:
                    if event.ui_element == button:
                        # 显示物品描述
                        info_label.set_text(f"你查看了{item_name}：{items_info.get(item_name, '这是你珍藏的物品集')}")
                        info_label.show()
                        
                        # 特殊处理：点击电脑按钮打开电脑界面
                        if item_name == "电脑" and not showing_computer:
                            showing_computer = True
                            close_button, computer_overlay, program_buttons, computer_info_label, computer_window, time_label = show_computer_interface(screen, manager, player_info, game_time)
                        
                        # 特殊处理：点击书架按钮打开书架界面
                        elif item_name == "书架" and not showing_bookshelf:
                            showing_bookshelf = True
                            bookshelf_close_button, bookshelf_overlay, book_buttons, book_info_label, bookshelf_window, book_image_panel = show_bookshelf_interface(screen, manager)
                        
                        # 特殊处理：点击书桌按钮打开书桌界面
                        elif item_name == "书桌" and not showing_desk:
                            showing_desk = True
                            desk_close_button, desk_overlay, desk_item_buttons, desk_info_label, desk_window = show_desk_interface(screen, manager)
                        
                        # 特殊处理：点击床按钮打开床铺界面
                        elif item_name == "床" and not showing_bed:
                            showing_bed = True
                            bed_close_button, bed_overlay, nap_button, sleep_button, current_time_label, sleep_info_label, bed_window = show_bed_interface(screen, manager, game_time)
                        
                        # 特殊处理：点击客厅按钮跳转到客厅场景
                        elif item_name == "客厅":
                            return "go_to_living_room"
                        
                        # 特殊处理：点击收藏品按钮打开收藏品界面
                        elif item_name == "收藏品" and not showing_collection:
                            showing_collection = True
                            collection_close_button, collection_overlay, collection_buttons, collection_info_label, collection_window, collection_image_panel = show_collection_interface(screen, manager)
                
                # 如果显示电脑界面，处理电脑界面的按钮点击
                if showing_computer:
                    if event.ui_element == close_button:
                        showing_computer = False
                        if computer_window:
                            computer_window.kill()
                            program_buttons = []
                            close_button = None
                            computer_info_label = None
                            time_label = None
                            computer_window = None
                    
                    # 处理程序按钮点击
                    if program_buttons:
                        for i, prog_btn in enumerate(program_buttons):
                            if event.ui_element == prog_btn:
                                if computer_info_label:
                                    computer_info_label.set_text(f"你点击了{prog_btn.text}，这个功能正在开发中...")
                                    computer_info_label.show()
                
                # 处理书架界面的按钮点击
                if showing_bookshelf:
                    if event.ui_element == bookshelf_close_button:
                        showing_bookshelf = False
                        if bookshelf_window:
                            bookshelf_window.kill()
                            book_buttons = None
                            bookshelf_close_button = None
                            book_info_label = None
                            book_image_panel = None
                            bookshelf_window = None
                    elif book_buttons:
                        # 处理书籍按钮点击
                        for book_data in book_buttons:
                            if len(book_data) == 4:  # 如果包含图片信息
                                book_name, book_desc, book_btn, book_image = book_data
                                if event.ui_element == book_btn:
                                    if book_info_label:
                                        # 将换行符转换为HTML换行标签
                                        desc_with_breaks = book_desc.replace("\n", "<br>")
                                        formatted_text = f'<font face="simhei" size=4><b>{book_name}</b></font><br><br><font face="simhei" size=3>{desc_with_breaks}</font>'
                                        book_info_label.html_text = formatted_text
                                        book_info_label.rebuild()
                                    # 显示图片
                                    if book_name == "《三国演义》" and book_image_panel:
                                        book_image_panel.show()
                            else:  # 没有图片信息的书籍
                                book_name, book_desc, book_btn = book_data
                                if event.ui_element == book_btn:
                                    if book_info_label:
                                        # 将换行符转换为HTML换行标签
                                        desc_with_breaks = book_desc.replace("\n", "<br>")
                                        formatted_text = f'<font face="simhei" size=4><b>{book_name}</b></font><br><br><font face="simhei" size=3>{desc_with_breaks}</font>'
                                        book_info_label.html_text = formatted_text
                                        book_info_label.rebuild()
                                    # 隐藏图片面板
                                    if book_image_panel:
                                        book_image_panel.hide()
                
                # 处理书桌界面的按钮点击
                if showing_desk:
                    if event.ui_element == desk_close_button:
                        showing_desk = False
                        if desk_window:
                            desk_window.kill()
                            desk_item_buttons = None
                            desk_close_button = None
                            desk_info_label = None
                            desk_window = None
                    elif desk_item_buttons:
                        # 处理物品按钮点击
                        for item_name, item_desc, item_btn in desk_item_buttons:
                            if event.ui_element == item_btn and desk_info_label:
                                desk_info_label.set_text(f"{item_name}\n\n{item_desc}")
                
                # 处理床铺界面的按钮点击
                if showing_bed:
                    if event.ui_element == bed_close_button:
                        showing_bed = False
                        if bed_window:
                            bed_window.kill()
                            nap_button = None
                            sleep_button = None
                            current_time_label = None
                            sleep_info_label = None
                            bed_window = None
                    elif event.ui_element == nap_button:
                        # 小睡一下，增加2小时
                        game_time.advance_time(hours=2)
                        # 更新时钟显示
                        clock_label.set_text(game_time.get_formatted_full_display())
                        # 更新当前时间显示
                        if current_time_label:
                            current_time_label.set_text(f"当前时间：{game_time.get_formatted_time()}")
                        # 显示睡眠信息
                        if sleep_info_label:
                            sleep_info_label.set_text("你小睡了2小时，感觉精神了一些！")
                            sleep_info_label.show()
                        # 更新背景
                        background = load_bedroom_background(game_time)
                    elif event.ui_element == sleep_button:
                        # 正常睡眠，增加8小时
                        game_time.advance_time(hours=8)
                        # 更新时钟显示
                        clock_label.set_text(game_time.get_formatted_full_display())
                        # 更新当前时间显示
                        if current_time_label:
                            current_time_label.set_text(f"当前时间：{game_time.get_formatted_time()}")
                        # 显示睡眠信息
                        if sleep_info_label:
                            sleep_info_label.set_text("你睡了一个好觉，精力充沛！")
                            sleep_info_label.show()
                        # 更新背景
                        background = load_bedroom_background(game_time)
                
                # 处理收藏品界面的按钮点击
                if showing_collection:
                    if event.ui_element == collection_close_button:
                        showing_collection = False
                        if collection_window:
                            collection_window.kill()
                            collection_buttons = None
                            collection_close_button = None
                            collection_info_label = None
                            collection_image_panel = None
                            collection_window = None
                    elif collection_buttons:
                        # 处理收藏品按钮点击
                        for item_data in collection_buttons:
                            if len(item_data) == 4:  # 如果包含图片信息
                                item_name, item_desc, item_btn, item_image = item_data
                                if event.ui_element == item_btn:
                                    if collection_info_label:
                                        # 将换行符转换为HTML换行标签
                                        desc_with_breaks = item_desc.replace("\n", "<br>")
                                        formatted_text = f'<font face="simhei" size=4><b>{item_name}</b></font><br><br><font face="simhei" size=3>{desc_with_breaks}</font>'
                                        collection_info_label.html_text = formatted_text
                                        collection_info_label.rebuild()
                                    # 显示图片
                                    if collection_image_panel:
                                        try:
                                            image_path = os.path.join('assert', 'images', item_image)
                                            if os.path.exists(image_path):
                                                item_image_surface = pygame.image.load(image_path)
                                                item_image_surface = pygame.transform.scale(item_image_surface, (460, 290))
                                                collection_image_panel.set_image(item_image_surface)
                                                collection_image_panel.show()
                                        except Exception as e:
                                            print(f"加载收藏品图片时出错：{e}")
                                            collection_image_panel.hide()
                            else:  # 没有图片信息的收藏品
                                item_name, item_desc, item_btn = item_data
                                if event.ui_element == item_btn:
                                    if collection_info_label:
                                        # 将换行符转换为HTML换行标签
                                        desc_with_breaks = item_desc.replace("\n", "<br>")
                                        formatted_text = f'<font face="simhei" size=4><b>{item_name}</b></font><br><br><font face="simhei" size=3>{desc_with_breaks}</font>'
                                        collection_info_label.html_text = formatted_text
                                        collection_info_label.rebuild()
                                    # 隐藏图片面板
                                    if collection_image_panel:
                                        collection_image_panel.hide()
            
            # 将事件传递给UI管理器
            manager.process_events(event)
        
        # 更新时间闪烁效果
        blink_timer += time_delta
        if blink_timer >= 0.5:  # 每0.5秒切换一次状态
            blink_timer = 0
            blink_state = not blink_state
        
        # 如果显示电脑界面，更新时间显示
        if showing_computer and time_label:
            formatted_time = game_time.get_formatted_time()
            blink_char = "|" if blink_state else " "
            time_str = f"时间: {formatted_time} {blink_char}"
            time_label.set_text(time_str)
        
        # 更新UI
        manager.update(time_delta)
        
        # 清屏
        screen.fill((0, 0, 0))
        
        # 绘制背景图片
        if background:
            screen.blit(background, (0, 0))
        
        # 如果显示电脑界面，先绘制半透明遮罩
        if showing_computer and computer_overlay:
            screen.blit(computer_overlay, (0, 0))
        
        # 如果显示书架界面，绘制半透明遮罩
        if showing_bookshelf and bookshelf_overlay:
            screen.blit(bookshelf_overlay, (0, 0))
        
        # 如果显示书桌界面，绘制半透明遮罩
        if showing_desk and desk_overlay:
            screen.blit(desk_overlay, (0, 0))
        
        # 如果显示床铺界面，绘制半透明遮罩
        if showing_bed and bed_overlay:
            screen.blit(bed_overlay, (0, 0))
        
        # 如果显示收藏品界面，绘制半透明遮罩
        if showing_collection and collection_overlay:
            screen.blit(collection_overlay, (0, 0))
        
        # 绘制UI
        manager.draw_ui(screen)
        
        # 更新显示
        pygame.display.update()
    
    return "back_to_menu" 