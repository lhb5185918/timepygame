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
        """增加游戏时间"""
        total_minutes = self.minute + minutes
        additional_hours = total_minutes // 60
        self.minute = total_minutes % 60
        
        total_hours = self.hour + hours + additional_hours
        additional_days = int(total_hours // 24)
        self.hour = total_hours % 24
        
        if additional_days > 0:
            self.advance_days(additional_days)
    
    def advance_days(self, days):
        """增加天数"""
        self.day += days
        while self.day > self.get_days_in_month():
            self.day -= self.get_days_in_month()
            self.month += 1
            if self.month > 12:
                self.month = 1
                self.year += 1
    
    def get_days_in_month(self):
        """获取当月天数"""
        if self.month in [4, 6, 9, 11]:
            return 30
        elif self.month == 2:
            if self.is_leap_year():
                return 29
            return 28
        else:
            return 31
    
    def is_leap_year(self):
        """判断是否为闰年"""
        return (self.year % 4 == 0 and self.year % 100 != 0) or (self.year % 400 == 0)
    
    def get_current_season(self):
        """获取当前季节"""
        if self.month in [3, 4, 5]:
            return "春季"
        elif self.month in [6, 7, 8]:
            return "夏季"
        elif self.month in [9, 10, 11]:
            return "秋季"
        else:
            return "冬季"
    
    def get_current_month_name(self):
        """获取当前月份名称"""
        month_names = ["一", "二", "三", "四", "五", "六", "七", "八", "九", "十", "十一", "十二"]
        return f"{month_names[self.month - 1]}月"
    
    def get_formatted_time(self):
        """获取格式化的时间字符串 HH:MM"""
        return f"{int(self.hour):02d}:{int(self.minute):02d}"
    
    def get_formatted_full_display(self):
        """获取完整的时间显示，包括季节和日期"""
        return f"{self.get_current_season()} {self.get_current_month_name()}{int(self.day)}日 {self.get_formatted_time()}"
    
    def get_formatted_date(self):
        """获取格式化的日期字符串"""
        return f"{self.year}年{self.get_current_month_name()}{self.day}日"
    
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
        """根据当前时间返回光照条件"""
        hour = int(self.hour)
        if 6 <= hour < 18:  # 白天
            return "day"
        elif 18 <= hour < 20 or 4 <= hour < 6:  # 黎明/黄昏
            return "twilight"
        else:  # 夜晚
            return "night"
    
    def get_total_days(self):
        """获取从游戏开始(2000年1月1日)至今的总天数"""
        # 计算年份贡献的天数
        days = 0
        for y in range(2000, self.year):
            if (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0):
                days += 366  # 闰年
            else:
                days += 365  # 平年
                
        # 计算当年月份贡献的天数
        for m in range(1, self.month):
            days += self.DAYS_IN_MONTH[m]
            # 如果是闰年且已经过了2月
            if m == 2 and self.is_leap_year():
                days += 1
                
        # 加上当月的天数
        days += self.day
        
        return days 