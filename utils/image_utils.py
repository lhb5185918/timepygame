import pygame
import os

def load_image(image_path, size=None, convert_alpha=True):
    """
    加载图片并可选地调整大小
    
    参数:
        image_path: 图片路径
        size: 可选的大小元组 (宽, 高)
        convert_alpha: 是否转换为带Alpha通道的格式
        
    返回:
        加载的pygame Surface对象
    """
    # 检查文件是否存在
    if not os.path.exists(image_path):
        print(f"警告: 找不到图片文件 {image_path}")
        # 创建一个空白的surface作为替代
        if size:
            surface = pygame.Surface(size, pygame.SRCALPHA)
            surface.fill((200, 200, 200, 128))  # 使用灰色半透明填充
        else:
            surface = pygame.Surface((100, 100), pygame.SRCALPHA)
            surface.fill((200, 200, 200, 128))
        return surface
    
    try:
        # 加载图片
        if convert_alpha:
            image = pygame.image.load(image_path).convert_alpha()
        else:
            image = pygame.image.load(image_path).convert()
        
        # 如果指定了大小，则调整图片大小
        if size:
            image = pygame.transform.scale(image, size)
        
        return image
    except Exception as e:
        print(f"加载图片时出错: {e}")
        # 创建一个空白的surface作为替代
        if size:
            surface = pygame.Surface(size, pygame.SRCALPHA)
        else:
            surface = pygame.Surface((100, 100), pygame.SRCALPHA)
        surface.fill((255, 0, 0, 128))  # 使用红色半透明填充表示错误
        return surface

def load_and_transform_image(image_path, size=None, rotation=0, flip_x=False, flip_y=False):
    """
    加载图片并应用变换（调整大小、旋转、翻转）
    
    参数:
        image_path: 图片路径
        size: 可选的大小元组 (宽, 高)
        rotation: 旋转角度（度）
        flip_x: 是否水平翻转
        flip_y: 是否垂直翻转
        
    返回:
        变换后的pygame Surface对象
    """
    # 先加载图片
    image = load_image(image_path)
    
    # 应用翻转
    if flip_x or flip_y:
        image = pygame.transform.flip(image, flip_x, flip_y)
    
    # 应用旋转
    if rotation != 0:
        image = pygame.transform.rotate(image, rotation)
    
    # 调整大小（放在最后以保持旋转后的比例）
    if size:
        image = pygame.transform.scale(image, size)
    
    return image 