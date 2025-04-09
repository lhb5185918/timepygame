import pygame
import pygame_gui
import sys
import os

def show_living_room_scene(screen, player_info):
    """显示客厅场景"""
    # 获取屏幕尺寸
    WIDTH, HEIGHT = screen.get_size()
    
    # 创建UI管理器
    manager = pygame_gui.UIManager((WIDTH, HEIGHT), 'data/themes/theme.json')
    
    # 加载客厅背景图片
    bg_path = os.path.join('assert', 'images', 'home.png')
    if os.path.exists(bg_path):
        background = pygame.image.load(bg_path)
        background = pygame.transform.scale(background, (WIDTH, HEIGHT))
    else:
        print(f"警告：找不到客厅背景图片 {bg_path}")
        background = pygame.Surface((WIDTH, HEIGHT))
        background.fill((100, 100, 100))  # 灰色背景作为后备
    
    # 显示玩家信息
    player_info_label = pygame_gui.elements.UILabel(
        relative_rect=pygame.Rect((20, 20), (250, 30)),
        text=f"玩家: {player_info['name']} | {player_info['age']}岁",
        manager=manager
    )
    
    # 创建返回卧室按钮
    back_button = pygame_gui.elements.UIButton(
        relative_rect=pygame.Rect((30, 150), (120, 40)),
        text="返回卧室",
        manager=manager,
        object_id=pygame_gui.core.ObjectID(class_id='@buttons', object_id='#item_button')
    )
    
    # 创建时钟显示 - 包含季节、月份、日期和时间
    clock_label = pygame_gui.elements.UILabel(
        relative_rect=pygame.Rect((WIDTH - 350, 70), (320, 40)),
        text="冬季 一月1日 09:00",
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
    
    # 客厅中可交互物品的描述信息
    items_info = {
        "电视": "这是一台老式的电视机，还能看到雪花屏。",
        "沙发": "舒适的布艺沙发，是休息的好地方。",
        "茶几": "一张木质茶几，上面摆着一些零食和遥控器。",
        "窗户": "透过窗户可以看到外面的风景。",
        "卧室": "通往卧室的门。"
    }
    
    # 创建交互按钮
    interaction_buttons = []
    
    # 创建电视按钮
    tv_button = pygame_gui.elements.UIButton(
        relative_rect=pygame.Rect((WIDTH - 150, 200), (120, 40)),
        text="电视",
        manager=manager,
        object_id=pygame_gui.core.ObjectID(class_id='@buttons', object_id='#item_button')
    )
    interaction_buttons.append(("电视", tv_button))
    
    # 创建沙发按钮
    sofa_button = pygame_gui.elements.UIButton(
        relative_rect=pygame.Rect((WIDTH - 150, 250), (120, 40)),
        text="沙发",
        manager=manager,
        object_id=pygame_gui.core.ObjectID(class_id='@buttons', object_id='#item_button')
    )
    interaction_buttons.append(("沙发", sofa_button))
    
    # 创建茶几按钮
    table_button = pygame_gui.elements.UIButton(
        relative_rect=pygame.Rect((WIDTH - 150, 300), (120, 40)),
        text="茶几",
        manager=manager,
        object_id=pygame_gui.core.ObjectID(class_id='@buttons', object_id='#item_button')
    )
    interaction_buttons.append(("茶几", table_button))
    
    # 创建窗户按钮
    window_button = pygame_gui.elements.UIButton(
        relative_rect=pygame.Rect((WIDTH - 150, 350), (120, 40)),
        text="窗户",
        manager=manager,
        object_id=pygame_gui.core.ObjectID(class_id='@buttons', object_id='#item_button')
    )
    interaction_buttons.append(("窗户", window_button))
    
    # 创建卧室按钮
    bedroom_button = pygame_gui.elements.UIButton(
        relative_rect=pygame.Rect((WIDTH - 150, 400), (120, 40)),
        text="卧室",
        manager=manager,
        object_id=pygame_gui.core.ObjectID(class_id='@buttons', object_id='#item_button')
    )
    interaction_buttons.append(("卧室", bedroom_button))
    
    # 创建提示标签（初始隐藏）
    info_label = pygame_gui.elements.UILabel(
        relative_rect=pygame.Rect((WIDTH//2 - 300, HEIGHT - 100), (600, 50)),
        text="",
        manager=manager,
        visible=0
    )
    
    # 创建时钟控制帧率
    clock = pygame.time.Clock()
    
    running = True
    while running:
        time_delta = clock.tick(60)/1000.0
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            if event.type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == back_button:
                    return "back_to_bedroom"
                
                # 处理探索按钮点击
                if event.ui_element == explore_button:
                    info_label.set_text("你花了1小时探索客厅，发现了一些有趣的东西。")
                    info_label.show()
                
                # 检查是否点击了交互按钮
                for item_name, button in interaction_buttons:
                    if event.ui_element == button:
                        # 显示物品描述
                        info_label.set_text(f"你查看了{item_name}：{items_info[item_name]}")
                        info_label.show()
                        
                        # 特殊处理：点击卧室按钮返回卧室场景
                        if item_name == "卧室":
                            return "back_to_bedroom"
            
            manager.process_events(event)
        
        manager.update(time_delta)
        
        # 绘制背景
        screen.blit(background, (0, 0))
        
        # 绘制UI
        manager.draw_ui(screen)
        
        pygame.display.update()
    
    return "back_to_bedroom" 