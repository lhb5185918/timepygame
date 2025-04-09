"""
游戏时间系统模块
处理游戏内的时间流逝、季节变化及相关显示
"""

class GameTimeSystem:
    """游戏时间系统类，用于管理游戏内的时间流逝"""
    
    # 月份天数映射（注意二月是28天）
    DAYS_IN_MONTH = {
        1: 31,  # 一月
        2: 28,  # 二月
        3: 31,  # 三月
        4: 30,  # 四月
        5: 31,  # 五月
        6: 30,  # 六月
        7: 31,  # 七月
        8: 31,  # 八月
        9: 30,  # 九月
        10: 31, # 十月
        11: 30, # 十一月
        12: 31  # 十二月
    }
    
    # 季节映射
    SEASONS = {
        1: "冬季",  # 一月
        2: "冬季",  # 二月
        3: "春季",  # 三月
        4: "春季",  # 四月
        5: "春季",  # 五月
        6: "夏季",  # 六月
        7: "夏季",  # 七月
        8: "夏季",  # 八月
        9: "秋季",  # 九月
        10: "秋季", # 十月
        11: "秋季", # 十一月
        12: "冬季"  # 十二月
    }
    
    # 月份名称
    MONTH_NAMES = {
        1: "一月",
        2: "二月",
        3: "三月",
        4: "四月",
        5: "五月",
        6: "六月",
        7: "七月",
        8: "八月",
        9: "九月",
        10: "十月",
        11: "十一月",
        12: "十二月"
    }
    
    def __init__(self, year=2000, month=1, day=1, hour=9, minute=0):
        """初始化时间系统"""
        self.year = year
        self.month = month
        self.day = day
        self.hour = hour
        self.minute = minute
    
    def advance_time(self, hours=0, minutes=0):
        """
        推进时间
        :param hours: 增加的小时数
        :param minutes: 增加的分钟数
        :return: 无
        """
        # 处理分钟增加
        self.minute += minutes
        self.hour += self.minute // 60
        self.minute %= 60
        
        # 处理小时增加
        self.hour += hours
        self.day += self.hour // 24
        self.hour %= 24
        
        # 处理日期溢出
        while self.day > self.get_days_in_current_month():
            self.day -= self.get_days_in_current_month()
            self.month += 1
            if self.month > 12:
                self.month = 1
                self.year += 1
    
    def get_days_in_current_month(self):
        """获取当前月份的天数"""
        return self.DAYS_IN_MONTH[self.month]
    
    def get_current_season(self):
        """获取当前季节"""
        return self.SEASONS[self.month]
    
    def get_current_month_name(self):
        """获取当前月份名称"""
        return self.MONTH_NAMES[self.month]
    
    def get_formatted_date(self):
        """获取格式化的日期字符串"""
        return f"{self.year}年{self.get_current_month_name()}{self.day}日"
    
    def get_formatted_time(self):
        """获取格式化的时间字符串"""
        return f"{self.hour:02d}:{self.minute:02d}"
    
    def get_formatted_date_time(self):
        """获取完整格式化的日期时间字符串"""
        return f"{self.get_current_season()} {self.get_formatted_date()} {self.get_formatted_time()}"
    
    def get_formatted_clock_time(self):
        """获取简洁的时钟显示格式"""
        return f"时间: {self.get_formatted_time()}"
    
    def get_formatted_full_display(self):
        """获取完整的时间显示格式，适合UI显示"""
        return f"{self.get_current_season()} {self.get_current_month_name()}{self.day}日 {self.get_formatted_time()}"
    
    def get_time_data(self):
        """获取时间数据字典，方便传递给其他函数"""
        return {
            "year": self.year,
            "month": self.month,
            "day": self.day,
            "hour": self.hour,
            "minute": self.minute,
            "season": self.get_current_season(),
            "month_name": self.get_current_month_name()
        }
    
    def get_light_condition(self):
        """
        获取当前的光照条件，用于确定背景图片
        返回值:
        - "night": 夜晚 (18:00-6:00)
        - "day": 白天 (10:00-16:00)
        - "twilight": 黎明/黄昏 (6:00-10:00 或 16:00-18:00)
        """
        if self.hour >= 18 or self.hour < 6:
            return "night"
        elif 10 <= self.hour < 16:
            return "day"
        else:
            return "twilight" 