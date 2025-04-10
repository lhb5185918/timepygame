import pygame
import pygame_gui
import sys
import os
import datetime  # 导入日期时间模块
from utils.time_system import GameTimeSystem  # 导入游戏时间系统
from data.book_data import BOOKS_DATA  # 导入书籍数据
from scenes.collection_scene import show_collection_interface  # 导入收藏品界面
from scenes.attributes_scene import show_attributes_interface  # 导入个人属性界面
from data.china_events import CHINA_EVENTS as china_events

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
    """显示电脑交互界面"""
    import pygame
    import pygame_gui
    from utils.image_utils import load_image, load_and_transform_image
    
    # 创建半透明背景
    WIDTH, HEIGHT = screen.get_size()
    computer_overlay = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
    computer_overlay.fill((0, 0, 0, 180))  # 半透明黑色
    
    # 创建界面容器
    computer_window = pygame_gui.elements.UIPanel(
        relative_rect=pygame.Rect((150, 100), (500, 400)),
        manager=manager,
        starting_height=2
    )
    
    # 加载电脑桌面背景图片
    try:
        computer_bg_path = os.path.join('assert', 'images', 'computer_desk.png')
        if os.path.exists(computer_bg_path):
            computer_bg = load_image(computer_bg_path, size=(500, 400))
            computer_window.set_image(computer_bg)
    except Exception as e:
        print(f"加载电脑背景图片时出错：{e}")
    
    # 创建任务栏
    taskbar = pygame_gui.elements.UIPanel(
        relative_rect=pygame.Rect((0, 370), (500, 30)),
        manager=manager,
        container=computer_window,
        starting_height=3
    )
    
    # 设置任务栏颜色
    taskbar_surface = pygame.Surface((500, 30))
    taskbar_surface.fill((0, 0, 128))  # Windows经典蓝色
    taskbar.set_image(taskbar_surface)
    
    # 创建开始按钮
    start_button = pygame_gui.elements.UIButton(
        relative_rect=pygame.Rect((5, 2), (50, 26)),
        text="开始",
        manager=manager,
        container=taskbar,
        object_id=pygame_gui.core.ObjectID(class_id='@buttons', object_id='#start_button')
    )
    
    # 创建时钟显示在任务栏右侧
    taskbar_time = pygame_gui.elements.UILabel(
        relative_rect=pygame.Rect((400, 2), (95, 26)),
        text=f"时间: {game_time.get_formatted_time()}",
        manager=manager,
        container=taskbar
    )
    
    # 创建关闭按钮
    close_button = pygame_gui.elements.UIButton(
        relative_rect=pygame.Rect((460, 10), (30, 30)),
        text="X",
        manager=manager,
        container=computer_window
    )
    
    # 创建程序按钮列表 - 用图标样式排列在桌面上
    programs = [
        {"name": "网页浏览器", "pos": (50, 50), "icon": "ie.png"},
        {"name": "新闻资讯", "pos": (150, 50), "icon": "news.png"},
        {"name": "游戏中心", "pos": (250, 50), "icon": "games.png"},
        {"name": "音乐播放器", "pos": (50, 150), "icon": "music.png"},
        {"name": "办公软件", "pos": (150, 150), "icon": "office.png"},
        {"name": "聊天工具", "pos": (250, 150), "icon": "chat.png"},
    ]
    
    # 创建所有程序按钮
    program_buttons = []
    
    # 创建程序按钮
    for program in programs:
        button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect(program["pos"], (80, 80)),
            text=program["name"],
            manager=manager,
            container=computer_window,
            object_id=pygame_gui.core.ObjectID(class_id='@buttons', object_id='#program_button')
        )
        program_buttons.append(button)
    
    # 创建显示信息的标签
    computer_info_label = pygame_gui.elements.UILabel(
        relative_rect=pygame.Rect((100, 250), (300, 40)),
        text="点击图标启动程序",
        manager=manager,
        container=computer_window
    )
    
    # 创建新闻面板
    news_panel = pygame_gui.elements.UIPanel(
        relative_rect=pygame.Rect((25, 50), (450, 300)),
        manager=manager,
        container=computer_window,
        starting_height=3
    )
    news_panel.hide()
    
    # 创建新闻标题栏
    news_title_bar = pygame_gui.elements.UIPanel(
        relative_rect=pygame.Rect((0, 0), (450, 30)),
        manager=manager,
        container=news_panel,
        starting_height=1
    )
    
    # 设置新闻标题栏颜色
    title_bar_surface = pygame.Surface((450, 30))
    title_bar_surface.fill((0, 0, 128))  # Windows经典蓝色
    news_title_bar.set_image(title_bar_surface)
    
    # 创建新闻标题
    news_title = pygame_gui.elements.UILabel(
        relative_rect=pygame.Rect((10, 5), (350, 20)),
        text="中国大事记 - 新闻资讯",
        manager=manager,
        container=news_title_bar
    )
    
    # 创建新闻关闭按钮
    news_close_button = pygame_gui.elements.UIButton(
        relative_rect=pygame.Rect((420, 5), (20, 20)),
        text="X",
        manager=manager,
        container=news_title_bar
    )
    
    # 创建新闻内容文本框（支持滚动）
    news_content = pygame_gui.elements.UITextBox(
        html_text="<b>加载新闻中...</b>",
        relative_rect=pygame.Rect((10, 40), (430, 250)),
        manager=manager,
        container=news_panel
    )
    
    return computer_window, close_button, program_buttons, computer_info_label, taskbar_time, news_panel, news_content, computer_overlay, news_close_button

def show_bookshelf_interface(screen, manager, attribute_elements=None):
    """显示书架界面"""
    # 获取屏幕尺寸
    WIDTH, HEIGHT = screen.get_size()
    
    # 创建半透明背景
    overlay = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
    overlay.fill((0, 0, 0, 180))  # 半透明黑色
    
    # 创建书架窗口
    bookshelf_window = pygame_gui.elements.UIPanel(
        relative_rect=pygame.Rect((WIDTH//2 - 400, HEIGHT//2 - 300), (800, 600)),
        manager=manager,
        starting_height=2
    )
    
    # 加载书架背景图片
    try:
        bookshelf_bg_path = os.path.join('assert', 'images', 'bookshelf_bg.png')
        if os.path.exists(bookshelf_bg_path):
            bookshelf_bg = pygame.image.load(bookshelf_bg_path).convert_alpha()
            bookshelf_bg = pygame.transform.scale(bookshelf_bg, (800, 600))
            bookshelf_window.set_image(bookshelf_bg)
    except Exception as e:
        print(f"加载书架背景图片时出错：{e}")
        # 如果没有背景图片，设置木质背景色
        panel_surface = pygame.Surface((800, 600))
        panel_surface.fill((139, 69, 19))  # 深棕色
        bookshelf_window.set_image(panel_surface)
    
    # 书架标题
    bookshelf_title = pygame_gui.elements.UILabel(
        relative_rect=pygame.Rect((10, 10), (730, 50)),
        text="我的藏书阁",
        manager=manager,
        container=bookshelf_window,
        object_id=pygame_gui.core.ObjectID(class_id='@title_labels', object_id='#bookshelf_title')
    )
    
    # 创建书籍详情面板
    details_panel = pygame_gui.elements.UIPanel(
        relative_rect=pygame.Rect((320, 70), (460, 510)),
        manager=manager,
        container=bookshelf_window
    )
    
    # 创建书籍描述标签
    book_info_label = pygame_gui.elements.UITextBox(
        relative_rect=pygame.Rect((10, 10), (440, 200)),
        html_text='<font face="simhei" size=4><b>欢迎来到我的藏书阁</b></font><br><br>'
                 '<font face="simhei" size=3>这里收藏着我珍贵的书籍，每一本都承载着独特的记忆。<br><br>'
                 '左边是我收藏的图书分类，点击书名可以查看详细介绍。<br><br>'
                 '让我们一起探索知识的海洋吧！</font>',
        manager=manager,
        container=details_panel
    )
    
    # 创建阅读按钮
    read_button = pygame_gui.elements.UIButton(
        relative_rect=pygame.Rect((10, 220), (440, 40)),
        text="阅读此书 (+0.5小时)",
        manager=manager,
        container=details_panel,
        object_id=pygame_gui.core.ObjectID(class_id='@buttons', object_id='#read_button'),
        visible=False  # 初始时隐藏
    )
    
    # 创建图片显示面板
    image_panel = pygame_gui.elements.UIPanel(
        relative_rect=pygame.Rect((10, 270), (440, 230)),  # 调整位置以适应阅读按钮
        manager=manager,
        container=details_panel
    )
    
    book_buttons = []
    y_offset = 70
    
    # 使用导入的书籍数据
    for category, book_list in BOOKS_DATA.items():
        if book_list:  # 只有当分类下有书籍时才显示分类
            # 添加分类标题
            category_label = pygame_gui.elements.UIPanel(
                relative_rect=pygame.Rect((20, y_offset), (250, 40)),
                manager=manager,
                container=bookshelf_window
            )
            
            # 在面板上添加文本
            category_text = pygame_gui.elements.UILabel(
                relative_rect=pygame.Rect((5, 5), (240, 30)),
                text=f"✦ {category} ✦",
                manager=manager,
                container=category_label,
                object_id=pygame_gui.core.ObjectID(class_id='@category_labels')
            )
            
            y_offset += 50
            
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
                y_offset += 45
            
            y_offset += 20
    
    # 关闭按钮
    close_button = pygame_gui.elements.UIButton(
        relative_rect=pygame.Rect((750, 10), (40, 40)),
        text="×",
        manager=manager,
        container=bookshelf_window
    )
    
    # 预加载三国演义图片
    try:
        image_path = os.path.join('assert', 'images', 'sanguoyanyi.png')
        if os.path.exists(image_path):
            sanguoyanyi_image = pygame.image.load(image_path)
            # 缩放图片以适应面板大小
            sanguoyanyi_image = pygame.transform.scale(sanguoyanyi_image, (440, 280))
            # 转换图片格式
            sanguoyanyi_image = sanguoyanyi_image.convert_alpha()
            image_panel.set_image(sanguoyanyi_image)
            # 初始时隐藏图片
            image_panel.hide()
    except Exception as e:
        print(f"预加载三国演义图片时出错：{e}")
    
    return close_button, overlay, book_buttons, book_info_label, bookshelf_window, image_panel, read_button

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

def show_bedroom_scene(screen, manager, player_info=None, game_time=None, attribute_elements=None):
    """显示卧室场景"""
    from data.china_events import CHINA_EVENTS
    
    # 获取屏幕尺寸
    WIDTH, HEIGHT = screen.get_size()
    
    # 创建UI管理器
    manager = pygame_gui.UIManager((WIDTH, HEIGHT), 'data/themes/theme.json')
    
    # 初始化游戏时间系统（从2000年1月1日上午9点开始）
    game_time = GameTimeSystem(year=2000, month=1, day=1, hour=9, minute=0)
    
    # 根据当前时间加载背景
    background = load_bedroom_background(game_time)
    
    # 创建属性按钮
    attributes_button = pygame_gui.elements.UIButton(
        relative_rect=pygame.Rect(10, 10, 100, 40),
        text="属性",
        manager=manager
    )

    # 创建玩家信息标签，处理player_info为None的情况
    player_info_text = "玩家信息未设置" if player_info is None else f"玩家: {player_info['name']} | {player_info['age']}岁"
    player_info_label = pygame_gui.elements.UILabel(
        relative_rect=pygame.Rect(120, 10, 300, 40),
        text=player_info_text,
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
    
    # 计算按钮的起始位置和间距
    button_start_y = 80  # 减小起始y坐标
    button_spacing = 40   # 减小按钮之间的间距
    button_width = 120    # 按钮宽度
    button_height = 35    # 减小按钮高度
    button_x = 30        # 所有按钮的x坐标
    
    # 创建电脑按钮
    computer_button = pygame_gui.elements.UIButton(
        relative_rect=pygame.Rect((button_x, button_start_y), (button_width, button_height)),
        text="电脑",
        manager=manager,
        object_id=pygame_gui.core.ObjectID(class_id='@buttons', object_id='#item_button')
    )
    interaction_buttons.append(("电脑", computer_button))
    
    # 创建书架按钮
    bookshelf_button = pygame_gui.elements.UIButton(
        relative_rect=pygame.Rect((button_x, button_start_y + button_spacing), (button_width, button_height)),
        text="书架",
        manager=manager,
        object_id=pygame_gui.core.ObjectID(class_id='@buttons', object_id='#item_button')
    )
    interaction_buttons.append(("书架", bookshelf_button))
    
    # 创建书桌按钮
    desk_button = pygame_gui.elements.UIButton(
        relative_rect=pygame.Rect((button_x, button_start_y + button_spacing * 2), (button_width, button_height)),
        text="书桌",
        manager=manager,
        object_id=pygame_gui.core.ObjectID(class_id='@buttons', object_id='#item_button')
    )
    interaction_buttons.append(("书桌", desk_button))
    
    # 创建床铺按钮
    bed_button = pygame_gui.elements.UIButton(
        relative_rect=pygame.Rect((button_x, button_start_y + button_spacing * 3), (button_width, button_height)),
        text="床铺",
        manager=manager,
        object_id=pygame_gui.core.ObjectID(class_id='@buttons', object_id='#item_button')
    )
    interaction_buttons.append(("床", bed_button))
    
    # 创建客厅按钮
    living_room_button = pygame_gui.elements.UIButton(
        relative_rect=pygame.Rect((button_x, button_start_y + button_spacing * 4), (button_width, button_height)),
        text="客厅",
        manager=manager,
        object_id=pygame_gui.core.ObjectID(class_id='@buttons', object_id='#item_button')
    )
    interaction_buttons.append(("客厅", living_room_button))
    
    # 创建收藏品按钮
    collection_button = pygame_gui.elements.UIButton(
        relative_rect=pygame.Rect((button_x, button_start_y + button_spacing * 5), (button_width, button_height)),
        text="收藏品",
        manager=manager,
        object_id=pygame_gui.core.ObjectID(class_id='@buttons', object_id='#item_button')
    )
    interaction_buttons.append(("收藏品", collection_button))
    
    # 创建属性按钮
    attributes_button = pygame_gui.elements.UIButton(
        relative_rect=pygame.Rect((button_x, button_start_y + button_spacing * 6), (button_width, button_height)),
        text="属性",
        manager=manager,
        object_id=pygame_gui.core.ObjectID(class_id='@buttons', object_id='#item_button')
    )
    interaction_buttons.append(("属性", attributes_button))
    
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
    
    # 添加个人属性界面相关变量
    showing_attributes = False
    attributes_close_button = None
    attributes_overlay = None
    attribute_elements = None
    attribute_desc_label = None
    attributes_window = None
    
    # 新闻相关变量
    news_close_button = None
    
    # 在创建属性相关变量时，直接初始化属性数据
    attributes_data = {
        "体力": {"value": 80, "desc": "你的身体状况，影响日常活动和学习效率。"},
        "智力": {"value": 85, "desc": "你的学习能力和知识储备。"},
        "魅力": {"value": 75, "desc": "你的人际交往能力和个人魅力。"},
        "心情": {"value": 70, "desc": "你当前的情绪状态，影响各项活动的表现。"},
        "创造力": {"value": 78, "desc": "你的想象力和创新能力。"},
        "意志力": {"value": 82, "desc": "你的毅力和专注度，影响学习和工作效率。"}
    }
    
    # 初始化状态变量
    showing_bookshelf = False
    showing_computer = False
    showing_desk = False
    showing_attributes = False
    is_reading = False  # 添加阅读状态
    showing_complete = False  # 添加完成提示状态
    reading_dots_timer = 0  # 添加动画计时器
    current_time = 0  # 添加当前时间
    
    # 初始化闪烁效果变量
    blink_timer = 0
    blink_state = True
    
    # 初始化阅读相关变量
    animation_window = None
    animation_label = None
    complete_window = None
    complete_text = None
    confirm_button = None
    reading_animation_start_time = 0
    reading_dots = 0
    
    # 创建时钟控制帧率
    clock = pygame.time.Clock()
    
    # 主循环
    running = True
    while running:
        time_delta = clock.tick(60)/1000.0  # 控制帧率为60fps
        current_time += time_delta  # 更新当前时间
        
        # 处理阅读动画
        if is_reading:
            # 更新动画点
            reading_dots_timer += time_delta
            if reading_dots_timer >= 0.5:  # 每0.5秒更新一次
                reading_dots = (reading_dots + 1) % 4
                dots = "." * reading_dots
                animation_label.html_text = f'<font face="simhei" size=5><b>正在阅读中{dots}</b></font><br><br><font face="simhei" size=4>请稍候，正在汲取知识的精华。</font>'
                animation_label.rebuild()
                reading_dots_timer = 0
            
            # 检查是否完成阅读（2秒后）
            if current_time - reading_animation_start_time >= 2:
                # 清理动画窗口
                animation_window.kill()
                is_reading = False
                
                # 显示完成提示
                complete_window, complete_text, confirm_button = show_reading_complete(screen, manager)
                showing_complete = True
        
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
                        info_label.set_text(f"你查看了{item_name}：{items_info.get(item_name, '这里显示你的个人属性')}")
                        info_label.show()
                        
                        # 特殊处理：点击电脑按钮打开电脑界面
                        if item_name == "电脑" and not showing_computer:
                            showing_computer = True
                            computer_window, close_button, program_buttons, computer_info_label, taskbar_time, news_panel, news_content, computer_overlay, news_close_button = show_computer_interface(screen, manager, player_info, game_time)
                        
                        # 特殊处理：点击书架按钮打开书架界面
                        elif item_name == "书架" and not showing_bookshelf:
                            showing_bookshelf = True
                            bookshelf_close_button, bookshelf_overlay, book_buttons, book_info_label, bookshelf_window, book_image_panel, read_button = show_bookshelf_interface(screen, manager, attribute_elements)
                        
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
                        
                        # 特殊处理：点击个人属性按钮打开属性界面
                        elif item_name == "属性" and not showing_attributes:
                            showing_attributes = True
                            attributes_close_button, attributes_overlay, attribute_elements, attribute_desc_label, attributes_window = show_attributes_interface(screen, manager, attributes_data)
                
                # 如果显示电脑界面，处理电脑界面的按钮点击
                if showing_computer:
                    if event.ui_element == close_button:
                        showing_computer = False
                        if computer_window:
                            computer_window.kill()
                            program_buttons = []
                            close_button = None
                            computer_info_label = None
                            taskbar_time = None
                            computer_window = None
                    elif event.ui_element == news_close_button:
                        # 隐藏新闻面板
                        news_panel.hide()
                        computer_info_label.set_text("已关闭新闻资讯")
                        computer_info_label.show()
                    
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
                            read_button = None
                            bookshelf_window = None
                    elif event.ui_element == read_button:
                        # 显示阅读动画
                        animation_window, animation_label = show_reading_animation(screen, manager)
                        reading_animation_start_time = current_time
                        is_reading = True
                        reading_dots = 0
                        reading_dots_timer = 0
                    elif event.ui_element == confirm_button and showing_complete:
                        # 清理完成提示窗口
                        complete_window.kill()
                        showing_complete = False
                        
                        # 更新游戏时间和属性
                        game_time.advance_time(hours=0.5)
                        clock_label.set_text(game_time.get_formatted_full_display())
                        
                        # 更新智力属性
                        for attr in attributes_data:
                            if attr == "智力":
                                # 更新属性数据中的值
                                attributes_data[attr]["value"] = min(attributes_data[attr]["value"] + 0.01, 100)
                                # 如果属性界面已经打开，也更新显示
                                if attribute_elements:
                                    for element in attribute_elements:
                                        if element['name'] == "智力":
                                            element['value'] = attributes_data[attr]["value"]
                                            # 更新进度条
                                            progress_bar_surface = pygame.Surface((200, 30))
                                            progress_bar_bg = pygame.image.load("assert/images/tiao.png").convert_alpha()
                                            progress_bar_bg = pygame.transform.scale(progress_bar_bg, (200, 30))
                                            progress_bar_surface.blit(progress_bar_bg, (0, 0))
                                            
                                            # 计算填充宽度
                                            fill_width = int((element['value'] / 100.0) * 196)
                                            if fill_width > 0:
                                                pygame.draw.rect(progress_bar_surface, (0, 255, 0), (2, 2, fill_width, 26))
                                            
                                            # 更新属性值显示
                                            element['progress_panel'].set_image(progress_bar_surface)
                                            element['value_label'].set_text(f"{element['value']:.2f}/100")
                                            break
                                break
                    elif book_buttons:
                        # 处理书籍按钮点击
                        for book_data in book_buttons:
                            if len(book_data) == 4:  # 如果包含图片信息
                                book_name, book_desc, book_btn, book_image = book_data
                                if event.ui_element == book_btn:
                                    if book_info_label:
                                        desc_with_breaks = book_desc.replace("\n", "<br>")
                                        formatted_text = f'<font face="simhei" size=4><b>{book_name}</b></font><br><br><font face="simhei" size=3>{desc_with_breaks}</font>'
                                        book_info_label.html_text = formatted_text
                                        book_info_label.rebuild()
                                    # 显示阅读按钮
                                    read_button.show()
                                    # 显示图片
                                    if book_name == "《三国演义》" and book_image_panel:
                                        book_image_panel.show()
                            else:  # 没有图片信息的书籍
                                book_name, book_desc, book_btn = book_data
                                if event.ui_element == book_btn:
                                    if book_info_label:
                                        desc_with_breaks = book_desc.replace("\n", "<br>")
                                        formatted_text = f'<font face="simhei" size=4><b>{book_name}</b></font><br><br><font face="simhei" size=3>{desc_with_breaks}</font>'
                                        book_info_label.html_text = formatted_text
                                        book_info_label.rebuild()
                                    # 显示阅读按钮
                                    read_button.show()
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
                
                # 处理个人属性界面的按钮点击
                if showing_attributes:
                    if event.ui_element == attributes_close_button:
                        showing_attributes = False
                        if attributes_window:
                            attributes_window.kill()
                            attribute_elements = None
                            attributes_close_button = None
                            attribute_desc_label = None
                            attributes_window = None
                    elif attribute_elements:
                        # 处理属性按钮点击
                        for attr in attribute_elements:
                            if event.ui_element == attr['button']:
                                if attribute_desc_label:
                                    formatted_text = (f'<font face="simhei" size=4><b>{attr["name"]}</b></font><br><br>'
                                                   f'<font face="simhei" size=3>{attr["desc"]}</font>')
                                    attribute_desc_label.html_text = formatted_text
                                    attribute_desc_label.rebuild()
                                    
                                    # 更新进度条显示
                                    if 'progress_panel' in attr:
                                        # 创建新的surface来绘制进度条
                                        progress_surface = pygame.Surface((250, 30), pygame.SRCALPHA)
                                        # 加载并绘制背景图片
                                        try:
                                            progress_bar_bg = pygame.image.load('assert/images/tiao.png').convert_alpha()
                                            progress_bar_bg = pygame.transform.scale(progress_bar_bg, (250, 30))
                                            progress_surface.blit(progress_bar_bg, (0, 0))
                                            # 计算并绘制填充部分（使用更紧凑的边距）
                                            fill_width = int((attr['value'] / 100.0) * 246)  # 只留2像素的边距
                                            if fill_width > 0:
                                                pygame.draw.rect(progress_surface, (0, 255, 0, 200), (2, 2, fill_width, 26))  # 减少边距，增加高度
                                            # 更新进度条显示
                                            attr['progress_panel'].set_image(progress_surface)
                                        except Exception as e:
                                            print(f"更新进度条时出错：{e}")
                                    
                                    # 更新数值标签
                                    attr['value_label'].set_text(f"{attr['value']}/100")
            
            # 处理自定义UI事件
            if event.type == pygame_gui.UI_BUTTON_PRESSED:
                # 如果电脑界面已显示，处理电脑程序按钮点击
                if showing_computer and event.ui_element in program_buttons:
                    # 获取按钮文本
                    button_text = event.ui_element.text
                    
                    # 处理新闻按钮点击
                    if button_text == "新闻资讯":
                        # 显示新闻面板
                        news_panel.show()
                        
                        # 获取当前游戏年份
                        current_year = game_time.year
                        current_day = game_time.get_total_days()
                        
                        # 构建新闻内容HTML，添加样式
                        news_html = """
                        <style>
                        .news-title {
                            color: #0078d7;
                            font-size: 16px;
                            font-weight: bold;
                            margin-bottom: 10px;
                        }
                        .year-title {
                            color: #ffffff;
                            background-color: #0078d7;
                            padding: 3px;
                            font-size: 14px;
                            font-weight: bold;
                            margin-top: 10px;
                        }
                        .event-title {
                            color: #000000;
                            font-weight: bold;
                        }
                        .event-date {
                            color: #666666;
                            font-style: italic;
                        }
                        .event-desc {
                            color: #333333;
                            margin-left: 20px;
                            margin-bottom: 8px;
                        }
                        </style>
                        <div class="news-title">中华人民共和国大事记</div>
                        """
                        
                        # 收集当前年份之前及当前年份的事件
                        events_found = False
                        for year_str in sorted(china_events.keys()):
                            # 从"1990年"格式中提取年份数字
                            year = int(year_str.replace("年", ""))
                            if year <= current_year:
                                year_events = china_events[year_str]
                                news_html += f'<div class="year-title">{year_str}</div>'
                                
                                for news_event in year_events:
                                    # 处理不同格式的事件
                                    if isinstance(news_event, dict):
                                        # 如果是字典格式，则获取title和desc
                                        title = news_event.get('title', '')
                                        desc = news_event.get('desc', '')
                                        date = news_event.get('date', '')
                                        
                                        # 格式化日期和标题
                                        if date:
                                            news_html += f'<div class="event-title">• {title} <span class="event-date">({date})</span></div>'
                                        else:
                                            news_html += f'<div class="event-title">• {title}</div>'
                                            
                                        # 添加描述
                                        if desc:
                                            news_html += f'<div class="event-desc">{desc}</div>'
                                    else:  # 字符串格式
                                        news_html += f'<div class="event-title">• {news_event}</div>'
                                
                                events_found = True
                        
                        if not events_found:
                            news_html += '<div style="color: #666666; text-align: center; margin-top: 30px;">暂无历史事件数据</div>'
                        
                        # 更新新闻内容
                        news_content.html_text = news_html
                        news_content.rebuild()
                        
                        # 更新信息标签
                        computer_info_label.set_text("正在浏览国家大事新闻")
                        computer_info_label.show()
                    else:
                        # 隐藏新闻面板
                        news_panel.hide()
                        computer_info_label.set_text(f"正在使用{button_text}")
                        computer_info_label.show()
            
            # 将事件传递给UI管理器
            manager.process_events(event)
        
        # 更新时间闪烁效果
        blink_timer += time_delta
        if blink_timer >= 0.5:  # 每0.5秒切换一次状态
            blink_timer = 0
            blink_state = not blink_state
        
        # 如果显示电脑界面，更新时间显示
        if showing_computer and taskbar_time:
            formatted_time = game_time.get_formatted_time()
            blink_char = "|" if blink_state else " "
            time_str = f"时间: {formatted_time} {blink_char}"
            taskbar_time.set_text(time_str)
        
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
        
        # 如果显示个人属性界面，绘制半透明遮罩
        if showing_attributes and attributes_overlay:
            screen.blit(attributes_overlay, (0, 0))
        
        # 绘制UI
        manager.draw_ui(screen)
        
        # 更新显示
        pygame.display.update()
    
    return "back_to_menu" 

def show_reading_animation(screen, manager):
    """显示阅读动画界面"""
    WIDTH, HEIGHT = screen.get_size()
    
    # 创建动画窗口
    animation_window = pygame_gui.elements.UIPanel(
        relative_rect=pygame.Rect((WIDTH//2 - 200, HEIGHT//2 - 150), (400, 300)),
        manager=manager,
        starting_height=10  # 增加层级值，确保显示在最上层
    )
    
    # 创建动画标签，使用html格式确保中文显示正确
    animation_label = pygame_gui.elements.UITextBox(
        relative_rect=pygame.Rect((20, 20), (360, 260)),
        html_text='<font face="simhei" size=5><b>正在阅读中...</b></font><br><br>'
                 '<font face="simhei" size=4>请稍候，正在汲取知识的精华。</font>',
        manager=manager,
        container=animation_window
    )
    
    return animation_window, animation_label

def show_reading_complete(screen, manager):
    """显示阅读完成提示"""
    WIDTH, HEIGHT = screen.get_size()
    
    # 创建完成提示窗口
    complete_window = pygame_gui.elements.UIPanel(
        relative_rect=pygame.Rect((WIDTH//2 - 200, HEIGHT//2 - 150), (400, 300)),
        manager=manager,
        starting_height=10  # 增加层级值，确保显示在最上层
    )
    
    # 创建完成提示文本
    complete_text = pygame_gui.elements.UITextBox(
        relative_rect=pygame.Rect((20, 20), (360, 220)),
        html_text='<font face="simhei" size=4><b>阅读完成！</b></font><br><br>'
                 '<font face="simhei" size=3>你仔细阅读了这本书，获得了新的知识。<br><br>'
                 '智力 +0.01<br>'
                 '时间 +0.5小时</font>',
        manager=manager,
        container=complete_window
    )
    
    # 创建确认按钮，使用Object ID确保使用正确的字体显示中文
    confirm_button = pygame_gui.elements.UIButton(
        relative_rect=pygame.Rect((150, 250), (100, 30)),
        text="确定",
        manager=manager,
        container=complete_window,
        object_id=pygame_gui.core.ObjectID(class_id='@buttons', object_id='#confirm_button')
    )
    
    return complete_window, complete_text, confirm_button 