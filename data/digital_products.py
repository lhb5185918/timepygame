"""
中国数码产品变迁史（1996-2010）
记录普通民众数码产品使用习惯和年度时髦商品变化
"""

DIGITAL_PRODUCTS_HISTORY = {
    "手机行业": {
        "初步普及阶段(1996-2000)": [
            {
                "title": "大哥大到功能机",
                "period": "1996-1997",
                "desc": "国产GSM手机科健KCH-2000诞生(1996)，但价格昂贵，普通家庭仍以座机、传呼机为主；诺基亚8110等机型因耐用性风靡，手机开始成为'身份象征'(1997)。",
                "popular_products": ["摩托罗拉3200", "诺基亚8110", "科健KCH-2000"]
            },
            {
                "title": "国产手机崛起",
                "period": "1998-1999",
                "desc": "波导RC818上市(1998)，广告词'手机中的战斗机'家喻户晓，国产手机初露锋芒；摩托罗拉'掌中宝'328C开启折叠手机潮流(1999)，轻薄设计颠覆传统'大哥大'形象。",
                "popular_products": ["波导RC818", "摩托罗拉328C", "摩托罗拉8900"]
            },
            {
                "title": "功能机繁荣",
                "period": "2000",
                "desc": "外资品牌如诺基亚、摩托罗拉、爱立信占据市场主流，手机逐渐从商务人士扩展到普通白领，手机尺寸不断缩小，设计更加美观。",
                "popular_products": ["诺基亚3310", "摩托罗拉V8088", "爱立信T28"]
            }
        ],
        "彩屏手机时代(2001-2005)": [
            {
                "title": "彩屏手机登场",
                "period": "2001-2002",
                "desc": "爱立信T68成为首款256色彩屏手机(2001)，手机从黑白迈向彩色；诺基亚7650推出首款内置摄像头的智能手机(2002)，拍照功能引发热议；UT斯达康小灵通因低廉话费迅速普及。",
                "popular_products": ["爱立信T68", "诺基亚7650", "小灵通"]
            },
            {
                "title": "国产手机份额超外资",
                "period": "2003-2004",
                "desc": "波导、TCL销量超越摩托罗拉(2003)，国产手机市占率突破50%；MP3手机兴起，音乐功能成为新卖点；摩托罗拉V3'刀锋'超薄手机引领设计潮流。",
                "popular_products": ["摩托罗拉V3", "波导手机", "TCL手机"]
            },
            {
                "title": "多媒体功能集成",
                "period": "2005",
                "desc": "手机整合MP3、相机、游戏等多种功能，诺基亚N系列推出，塞班智能系统逐渐普及；山寨机开始崛起，以超低价格和丰富功能吸引低端市场。",
                "popular_products": ["诺基亚N70", "索尼爱立信K750", "摩托罗拉E680"]
            }
        ],
        "智能手机萌芽(2006-2010)": [
            {
                "title": "功能机巅峰与山寨机爆发",
                "period": "2006-2007",
                "desc": "华强北山寨机以低价+LED跑马灯设计抢占市场(2006)，占国内份额30%；iPhone发布(2007)，触屏设计颠覆传统按键手机，但国内仍以诺基亚N95等塞班系统手机为主流。",
                "popular_products": ["诺基亚N95", "山寨机", "iPhone初代"]
            },
            {
                "title": "触屏手机普及",
                "period": "2008-2009",
                "desc": "中国发放3G牌照(2008)，诺基亚5800XM支持触控+3G上网，成为年轻人'街机'；诺基亚N97mini、摩托罗拉A1200E搭载触控系统，智能手机开始试水市场。",
                "popular_products": ["诺基亚5800XM", "iPhone 3GS", "魅族M8"]
            },
            {
                "title": "智能手机市场格局初现",
                "period": "2010",
                "desc": "华为终端业务转型，开始布局高端市场；三星Galaxy S等Android手机崭露头角；iPhone 4引领高端时尚，中华酷联依托运营商资源抢占中端市场。",
                "popular_products": ["iPhone 4", "三星Galaxy S", "HTC Desire"]
            }
        ]
    },
    "个人电脑": {
        "家庭初步普及(1996-2000)": [
            {
                "title": "品牌机与组装机并存",
                "period": "1996-1998",
                "desc": "国外品牌如IBM、康柏占据高端市场，价格高昂，普通家庭难以承受；中关村等电子市场兴起，组装机性价比高，成为入门用户首选；CPU从486向奔腾升级。",
                "popular_products": ["IBM PC", "组装电脑", "奔腾处理器"]
            },
            {
                "title": "电脑进入家庭",
                "period": "1999-2000",
                "desc": "联想天禧系列电脑上市(1999)，价格降至万元以下，中产家庭开始购置台式机；Windows 98系统普及，游戏和多媒体应用丰富；长城、方正品牌机开始进入政府和学校。",
                "popular_products": ["联想天禧系列", "长城电脑", "Windows 98"]
            }
        ],
        "互联网普及与电脑多元化(2001-2005)": [
            {
                "title": "家庭电脑普及",
                "period": "2001-2003",
                "desc": "联想品牌机+Windows XP系统进入普通家庭(2003)，拨号上网'猫'的嗞嗞声成一代人记忆；台式电脑价格降至5000元以下，大学生群体开始拥有个人电脑。",
                "popular_products": ["联想天骄系列", "Windows XP", "56K调制解调器"]
            },
            {
                "title": "品牌竞争与网络应用",
                "period": "2004-2005",
                "desc": "戴尔、惠普进入中国家用电脑市场，价格战促使电脑进一步普及；即时通讯软件QQ成为杀手级应用，网吧文化兴起；网络游戏如《魔兽世界》带动硬件升级需求。",
                "popular_products": ["戴尔灵越系列", "QQ软件", "《魔兽世界》"]
            }
        ],
        "笔记本与多元设备时代(2006-2010)": [
            {
                "title": "笔记本电脑普及",
                "period": "2006-2007",
                "desc": "神舟电脑推出低价笔记本(2006)，学生群体开始使用便携设备；联想收购IBM个人电脑业务后，ThinkPad品牌在中国市场开始走向大众；双核处理器成为主流。",
                "popular_products": ["神舟笔记本", "ThinkPad T系列", "英特尔酷睿双核"]
            },
            {
                "title": "上网本热潮",
                "period": "2008-2009",
                "desc": "华硕EeePC等上网本凭借低价和小巧引发热潮，便携电脑开始从商务人士扩展到学生和家庭用户；Windows Vista发布但口碑不佳；网络视频和在线购物成为普及应用。",
                "popular_products": ["华硕EeePC", "宏基Aspire One", "惠普Mini系列"]
            },
            {
                "title": "平板电脑兴起",
                "period": "2010",
                "desc": "苹果iPad上市，开启移动娱乐新场景，国内售价高达499美元；上网本逐渐被平板和轻薄笔记本取代；固态硬盘开始进入消费市场，大幅提升响应速度。",
                "popular_products": ["iPad", "MacBook Air", "华硕变形本"]
            }
        ]
    },
    "其他数码产品": {
        "家电数字化": [
            {
                "title": "彩电普及与价格战",
                "period": "1996-1999",
                "desc": "国产彩电通过降价抢占市场，长虹、海尔崛起，29寸彩电成为家庭标配；VCD播放机普及，成为家庭娱乐中心；家用录像机被DVD播放机逐渐取代。",
                "popular_products": ["长虹彩电", "康佳彩电", "熊猫VCD"]
            },
            {
                "title": "液晶电视革命",
                "period": "2003-2006",
                "desc": "液晶电视开始进入家庭，价格从两万元迅速降至万元以内；DVD播放机全面普及，碟片租赁店兴起；家用投影仪逐渐普及，家庭影院概念兴起。",
                "popular_products": ["创维液晶电视", "先锋DVD", "爱普生投影仪"]
            },
            {
                "title": "高清时代",
                "period": "2007-2010",
                "desc": "56寸液晶电视取代厚重'大背投'(2008)，3D功能初现；蓝光播放机进入高端市场；高清机顶盒开始普及，数字电视逐渐取代模拟信号。",
                "popular_products": ["三星LED电视", "索尼蓝光播放机", "数字电视机顶盒"]
            }
        ],
        "个人音频设备": [
            {
                "title": "CD随身听时代",
                "period": "1996-2000",
                "desc": "索尼、爱华等品牌的CD随身听是90年代后期主流音乐播放设备，价格从几百到上千元不等，带有防震功能的高端型号备受追捧；录音磁带仍广泛使用。",
                "popular_products": ["索尼Walkman", "爱华CD随身听", "松下收录机"]
            },
            {
                "title": "MP3播放器兴起",
                "period": "2001-2004",
                "desc": "基于闪存的MP3播放器逐渐普及，纽曼、魅族MP3成年轻人标配(2004)，替代随身听和磁带；容量从8MB到几GB不等，价格随着闪存成本下降而快速降低。",
                "popular_products": ["纽曼MP3", "魅族MP3", "爱国者MP3"]
            },
            {
                "title": "iPod时代与手机音乐",
                "period": "2005-2010",
                "desc": "苹果iPod系列在中国流行，尤其是2005年推出的iPod nano和2007年的iPod touch；智能手机开始整合音乐功能，逐渐取代独立MP3播放器；耳机品质成为关注焦点。",
                "popular_products": ["iPod nano", "iPod touch", "森海塞尔耳机"]
            }
        ],
        "数码影像": [
            {
                "title": "胶片到数码转变",
                "period": "1996-2002",
                "desc": "1996-2000年间，胶片相机仍是主流，柯达、富士等品牌占据市场；2000年后佳能、尼康等品牌的消费级数码相机开始进入中国家庭，但价格昂贵，像素较低。",
                "popular_products": ["柯达胶卷", "富士相机", "佳能IXUS系列"]
            },
            {
                "title": "数码相机普及",
                "period": "2003-2007",
                "desc": "索尼、三星等品牌推出千元级数码相机，像素提升至500万以上，带动普通家庭摄影热潮；卡片机成为记录家庭生活的主要工具，冲印店开始提供数码冲印服务。",
                "popular_products": ["索尼Cyber-shot", "三星数码相机", "佳能IXUS系列"]
            },
            {
                "title": "数码影像多元化",
                "period": "2008-2010",
                "desc": "入门级单反相机价格下探至5千元以下，佳能450D、尼康D90等成为摄影爱好者首选；2010年数码相机普及率在北京、上海达88%；DV摄像机家用市场兴起；微单相机开始出现。",
                "popular_products": ["佳能450D", "尼康D90", "索尼NEX微单"]
            }
        ],
        "游戏设备": [
            {
                "title": "红白机与掌机",
                "period": "1996-2000",
                "desc": "小霸王学习机（红白机改版）在中国家庭普及；任天堂GameBoy系列在中国非官方市场流行，带动盗版游戏卡带产业；街机厅在城市中广泛存在。",
                "popular_products": ["小霸王学习机", "GameBoy", "街机"]
            },
            {
                "title": "家用游戏机发展",
                "period": "2001-2006",
                "desc": "索尼PlayStation 2虽未正式进入中国，但通过水货和改装机在中国获得大量用户；任天堂GBA掌机流行；国产盗版游戏机市场繁荣。",
                "popular_products": ["PlayStation 2", "GameBoy Advance", "小霸王游戏机"]
            },
            {
                "title": "手机与网络游戏兴起",
                "period": "2007-2010",
                "desc": "随着手机性能提升，诺基亚N-Gage等将游戏功能作为卖点；网络游戏如《魔兽世界》、《征途》成为主流娱乐形式，网吧成为游戏社交中心；PSP掌机在学生群体流行。",
                "popular_products": ["PSP", "诺基亚N-Gage", "网络游戏"]
            }
        ]
    },
    "通信与互联网": {
        "互联网普及阶段": [
            {
                "title": "拨号上网初期",
                "period": "1996-2000",
                "desc": "56K调制解调器是主要上网设备，'嘟嘟嘟'的拨号声成为标志；上网费用按时计费，每小时约2-8元；网民主要集中在城市知识分子和大学生群体；电子邮件和BBS是主要应用。",
                "popular_products": ["56K调制解调器", "网易163邮箱", "新浪网"]
            },
            {
                "title": "宽带起步与网吧文化",
                "period": "2001-2005",
                "desc": "ADSL宽带服务开始进入家庭，但月租费仍较高；网吧成为年轻人上网主要场所，网络游戏带动产业发展；QQ即时通讯软件普及，网络社交雏形出现。",
                "popular_products": ["QQ", "网吧", "电信宽带"]
            },
            {
                "title": "宽带普及与Web2.0",
                "period": "2006-2008",
                "desc": "家庭宽带普及率提高，月租费降至百元左右；视频网站如优酷、土豆兴起；博客成为自我表达平台；网络游戏产业蓬勃发展。",
                "popular_products": ["优酷", "百度", "网易博客"]
            },
            {
                "title": "3G与移动互联网起步",
                "period": "2009-2010",
                "desc": "2009年1月中国发放3G牌照，手机上网速度提升；微博等社交媒体兴起；智能手机开始普及，手机应用商店出现；电子商务进入快速发展期。",
                "popular_products": ["新浪微博", "3G上网卡", "手机应用"]
            }
        ],
        "电子商务演变": [
            {
                "title": "电子商务萌芽",
                "period": "1996-2000",
                "desc": "1996年成立的阿里巴巴专注于B2B贸易；1998年8848、易趣网等电商平台出现，但受限于支付和物流系统落后，规模有限；网上订票等服务开始试点。",
                "popular_products": ["阿里巴巴", "8848", "易趣网"]
            },
            {
                "title": "C2C平台发展",
                "period": "2001-2005",
                "desc": "2003年淘宝网成立对抗eBay易趣；2004年支付宝推出解决信任问题；网购在大学生群体中开始流行；电脑配件、图书成为早期网购主力商品。",
                "popular_products": ["淘宝网", "支付宝", "当当网"]
            },
            {
                "title": "电商生态形成",
                "period": "2006-2010",
                "desc": "2008年金融危机促使线下商家向线上转移；京东从3C数码起家逐步扩展品类；2009年'双11'促销首次举办，创下5000万销售额；物流配送体系逐步完善。",
                "popular_products": ["京东商城", "双11购物节", "淘宝商城"]
            }
        ],
        "数字生活演变": [
            {
                "title": "数字产品初步普及",
                "period": "1996-2002",
                "desc": "数码产品从奢侈品逐步走向普及；外资品牌主导高端市场，国产品牌追赶；彩电、VCD等家电普及率提高；手机从'大哥大'向小型化方向发展。",
                "popular_products": ["彩电", "大哥大", "VCD播放机"]
            },
            {
                "title": "数字娱乐兴起",
                "period": "2003-2007",
                "desc": "MP3播放器、数码相机成为记录生活的工具；电脑和互联网在家庭中的地位提升；网络游戏和在线聊天成为主要娱乐方式；手机由通话工具向多功能设备转变。",
                "popular_products": ["MP3播放器", "数码相机", "网络游戏"]
            },
            {
                "title": "移动互联融入生活",
                "period": "2008-2010",
                "desc": "智能手机开始改变人们的生活方式；社交网络成为人际交往新平台；电子商务改变消费习惯；数字产品从'身份象征'变为日常工具，推动消费升级和数字化生活方式。",
                "popular_products": ["智能手机", "社交媒体", "电子商务"]
            }
        ]
    }
}


def get_products_by_category(category):
    """获取指定类别的数码产品历史"""
    if category in DIGITAL_PRODUCTS_HISTORY:
        return DIGITAL_PRODUCTS_HISTORY[category]
    return None


def get_all_categories():
    """获取所有数码产品类别"""
    return list(DIGITAL_PRODUCTS_HISTORY.keys())


def get_popular_products_by_year(year):
    """获取特定年份的流行数码产品"""
    results = {}
    for category, subcategories in DIGITAL_PRODUCTS_HISTORY.items():
        category_results = []

        # 处理嵌套结构
        for subcategory, items in subcategories.items() if isinstance(subcategories, dict) else [
            (category, subcategories)]:
            for item in items:
                # 检查年份是否在产品时期范围内
                if "period" in item:
                    period = item["period"]
                    years_range = period.split("-")
                    if len(years_range) == 2:
                        start_year = int(years_range[0])
                        end_year = int(years_range[1])
                        if start_year <= year <= end_year:
                            if "popular_products" in item:
                                for product in item["popular_products"]:
                                    category_results.append({
                                        "name": product,
                                        "category": subcategory if isinstance(subcategories, dict) else category,
                                        "period": period,
                                        "desc": item["title"]
                                    })

        if category_results:
            results[category] = category_results

    return results


def get_products_by_year(year):
    """获取特定年份的数码产品发展情况"""
    results = {}
    for category, subcategories in DIGITAL_PRODUCTS_HISTORY.items():
        category_results = []
        
        # 处理嵌套结构
        if isinstance(subcategories, dict):
            # 如果是字典，遍历子类别
            for subcategory, items in subcategories.items():
                for item in items:
                    # 检查年份是否在产品时期范围内
                    if "period" in item:
                        period = item["period"]
                        years_range = period.split("-")
                        if len(years_range) == 2:
                            start_year = int(years_range[0])
                            end_year = int(years_range[1])
                            if start_year <= year <= end_year:
                                category_results.append(item)
        else:
            # 如果不是字典，直接处理项目列表
            for item in subcategories:
                if "period" in item:
                    period = item["period"]
                    years_range = period.split("-")
                    if len(years_range) == 2:
                        start_year = int(years_range[0])
                        end_year = int(years_range[1])
                        if start_year <= year <= end_year:
                            category_results.append(item)
        
        if category_results:
            results[category] = category_results
    
    return results

# 数码产品剧情相关文案
DIGITAL_STORIES = {
    "手机体验": [
        {
            "title": "寻呼机时代的约定",
            "year_range": "1996-1998",
            "content": "小李收到BP机显示8868的呼叫，立刻找到公共电话亭回拨。那个年代，约定朋友多是靠BP机发暗号，一组数字包含许多含义。与此同时，街头巷尾'大哥大'的出现总会引来众人羡慕的目光。",
            "choices": [
                {"text": "花2万元购买摩托罗拉大哥大", "effect": {"money": -20000, "social": +15}},
                {"text": "购买600元的BP机", "effect": {"money": -600, "social": +5}},
                {"text": "继续使用公共电话", "effect": {"money": -100, "social": -5}}
            ]
        },
        {
            "title": "第一台手机",
            "year_range": "1998-2000",
            "content": "经过几个月的攒钱，终于能买一台属于自己的手机了。柜台前，诺基亚3210、摩托罗拉328c和国产波导的价格差异很大，但各有特色。销售员介绍说：'诺基亚续航好，摩托罗拉时尚，波导最便宜。'",
            "choices": [
                {"text": "选择诺基亚3210", "effect": {"money": -2800, "tech": +10, "social": +8}},
                {"text": "选择摩托罗拉328c翻盖机", "effect": {"money": -3200, "tech": +8, "social": +12}},
                {"text": "选择国产波导手机", "effect": {"money": -1600, "tech": +5, "social": +3}}
            ]
        },
        {
            "title": "手机铃声和彩信",
            "year_range": "2001-2003",
            "content": "李老师买了新手机，支持和弦铃声。周末，他花了一下午时间用手机键盘一个音符一个音符地编辑《两只老虎》当铃声。不久后，班上同学们开始互相发送彩信，有人炫耀刚下载的《老鼠爱大米》和手机主题。",
            "choices": [
                {"text": "订阅每月5元的彩铃服务", "effect": {"money": -60, "happiness": +5}},
                {"text": "购买第三方软件DIY铃声", "effect": {"money": -30, "tech": +5}},
                {"text": "继续使用默认铃声", "effect": {"money": 0, "social": -3}}
            ]
        },
        {
            "title": "拍照手机的诱惑",
            "year_range": "2003-2005",
            "content": "办公室里，同事们围着小张的新手机啧啧称奇：'这么小的手机竟然还能拍照！'虽然只有30万像素，但大家还是被这个新功能深深吸引。小王看着自己的黑白屏诺基亚，有些心动。",
            "choices": [
                {"text": "换购索尼爱立信拍照手机", "effect": {"money": -3000, "tech": +10, "social": +5}},
                {"text": "购买单独的数码相机", "effect": {"money": -1500, "tech": +8}},
                {"text": "继续使用现有手机", "effect": {"money": 0, "social": -3}}
            ]
        },
        {
            "title": "智能手机的选择",
            "year_range": "2007-2010",
            "content": "在手机卖场，王先生正在货比三家。一边是诺基亚N97，塞班系统成熟稳定；另一边是刚上市的iPhone，全触屏设计前卫但昂贵；还有一款国产山寨智能机，功能号称一应俱全但质量存疑。",
            "choices": [
                {"text": "选择iPhone", "effect": {"money": -5000, "tech": +15, "social": +10}},
                {"text": "选择诺基亚N97", "effect": {"money": -3500, "tech": +8, "social": +5}},
                {"text": "选择国产山寨智能机", "effect": {"money": -800, "tech": -5, "happiness": -10}}
            ]
        }
    ],
    "电脑变革": [
        {
            "title": "第一台家用电脑",
            "year_range": "1996-1999",
            "content": "刚刚大学毕业的张工程师决定买一台电脑。中关村电子市场人头攒动，一边是整机销售的柜台，IBM、康柏品牌机价格高昂；另一边是电脑配件市场，可以自己组装一台性价比更高的机器。",
            "choices": [
                {"text": "购买IBM品牌机", "effect": {"money": -15000, "tech": +10, "happiness": +5}},
                {"text": "在中关村组装一台电脑", "effect": {"money": -8000, "tech": +15, "intelligence": +5}},
                {"text": "去网吧使用电脑", "effect": {"money": -500, "social": +3}}
            ]
        },
        {
            "title": "Windows 98与游戏",
            "year_range": "1998-2000",
            "content": "小区物业开始提供宽带接入服务，每月298元。李先生刚装上了Windows 98系统，孩子们已经迫不及待地想玩《红色警戒》和《暗黑破坏神》。周末，几个孩子轮流使用这台电脑，成为家庭娱乐的中心。",
            "choices": [
                {"text": "安装游戏并限制孩子使用时间", "effect": {"tech": +5, "happiness": +8, "intelligence": -3}},
                {"text": "主要用于工作和学习", "effect": {"intelligence": +10, "happiness": -5}},
                {"text": "组织家庭局域网游戏", "effect": {"money": -1000, "tech": +10, "social": +5}}
            ]
        },
        {
            "title": "互联网咖啡",
            "year_range": "2001-2004",
            "content": "王大学生每天放学后会去学校旁的网吧，5块钱一小时。他熟练地打开QQ和网易，与远方的朋友聊天，浏览新闻，偶尔玩一会儿《传奇》。拨号上网在家里太贵了，而网吧已经是年轻人社交的重要场所。",
            "choices": [
                {"text": "经常去网吧上网", "effect": {"money": -300, "social": +8, "intelligence": -3}},
                {"text": "在家安装拨号上网", "effect": {"money": -600, "tech": +5}},
                {"text": "主要使用学校电脑室", "effect": {"money": -50, "intelligence": +5}}
            ]
        },
        {
            "title": "笔记本的诱惑",
            "year_range": "2005-2007",
            "content": "研究生小陈看着同学新买的ThinkPad笔记本羡慕不已。便携的设计意味着可以随时随地工作学习，但价格却是台式机的两倍多。另一个选择是神舟等国产品牌，价格更亲民但配置和质量略逊一筹。",
            "choices": [
                {"text": "购买ThinkPad笔记本", "effect": {"money": -12000, "tech": +10, "social": +8}},
                {"text": "购买神舟笔记本", "effect": {"money": -5000, "tech": +5, "happiness": -3}},
                {"text": "继续使用台式电脑", "effect": {"money": 0, "tech": -5}}
            ]
        },
        {
            "title": "上网本与iPad",
            "year_range": "2008-2010",
            "content": "2010年，苹果iPad在中国上市，引发了新一轮数码产品热潮。张女士正在考虑是选择轻便的上网本，还是购买时尚但昂贵的iPad。销售员介绍说：'上网本适合基础办公，iPad更适合娱乐和创意工作。'",
            "choices": [
                {"text": "购买iPad", "effect": {"money": -4000, "tech": +12, "social": +10}},
                {"text": "购买华硕上网本", "effect": {"money": -2500, "tech": +5, "intelligence": +5}},
                {"text": "等待技术更成熟再购买", "effect": {"money": 0, "tech": -5}}
            ]
        }
    ],
    "数码娱乐": [
        {
            "title": "CD与MP3的革命",
            "year_range": "1996-2001",
            "content": "小明攒了三个月的零花钱，终于可以买一台CD随身听了。商店里，索尼与爱华的产品让他眼花缭乱，但一位戴着耳机的大学生告诉他：'等等吧，听说MP3播放器要流行了，可以存几十首歌呢！'",
            "choices": [
                {"text": "购买索尼CD随身听", "effect": {"money": -800, "happiness": +10}},
                {"text": "等待购买MP3播放器", "effect": {"money": 0, "happiness": -5, "tech": +5}},
                {"text": "用随身录音机录制电台音乐", "effect": {"money": -200, "creativity": +5}}
            ]
        },
        {
            "title": "游戏机的选择",
            "year_range": "2000-2003",
            "content": "李家的小朋友吵着要买游戏机。爸爸带他去电子市场，那里有各种选择：小霸王学习机号称寓教于乐，水货PlayStation 2游戏效果好但价格高，GBA掌机则可以随身携带。",
            "choices": [
                {"text": "购买小霸王学习机", "effect": {"money": -400, "happiness": +5, "intelligence": +3}},
                {"text": "购买水货PlayStation 2", "effect": {"money": -2000, "happiness": +15, "intelligence": -5}},
                {"text": "购买GBA掌机", "effect": {"money": -800, "happiness": +10}}
            ]
        },
        {
            "title": "数码相机记录生活",
            "year_range": "2003-2005",
            "content": "张先生计划全家出游，想要购买一台数码相机记录珍贵时刻。以前都是用胶卷相机，冲洗照片既费时又费钱。电器城里，佳能、索尼和国产相机价格相差很大，但使用体验也有明显差异。",
            "choices": [
                {"text": "购买索尼数码相机", "effect": {"money": -3000, "happiness": +8, "creativity": +5}},
                {"text": "购买国产数码相机", "effect": {"money": -1000, "happiness": +3, "creativity": +3}},
                {"text": "继续使用胶卷相机", "effect": {"money": -300, "happiness": -3}}
            ]
        },
        {
            "title": "音乐播放器的革新",
            "year_range": "2005-2007",
            "content": "大学校园里，iPod成为时尚的象征。小赵看着同学雪白的iPod nano和转盘操作，再看看自己的国产MP3播放器，虽然功能相似，但时尚感和品质有明显差距。是否值得为品牌和设计多花几倍的价钱？",
            "choices": [
                {"text": "购买iPod nano", "effect": {"money": -1500, "happiness": +10, "social": +8}},
                {"text": "继续使用国产MP3", "effect": {"money": 0, "happiness": -3}},
                {"text": "购买带收音功能的MP4", "effect": {"money": -400, "happiness": +5}}
            ]
        },
        {
            "title": "高清影音体验",
            "year_range": "2008-2010",
            "content": "李家刚搬进新房，计划配置一套家庭影院系统。电器城导购介绍道：'现在液晶电视已经全面普及，您可以考虑46寸的LED电视，搭配家庭影院和高清播放机，观影效果堪比电影院。'",
            "choices": [
                {"text": "购置全套家庭影院", "effect": {"money": -15000, "happiness": +15, "social": +10}},
                {"text": "只购买液晶电视", "effect": {"money": -5000, "happiness": +8}},
                {"text": "继续使用老式电视", "effect": {"money": 0, "happiness": -5, "social": -5}}
            ]
        }
    ],
    "互联网生活": [
        {
            "title": "拨号上网初体验",
            "year_range": "1996-2000",
            "content": "李工程师办理了中国电信的163上网卡，每次上网前都要先断开电话，然后听着调制解调器发出'嘟嘟嘟'的拨号声。家人常抱怨：'你上网的时候，别人打不进电话来！'而每小时7元的费用也让人心疼。",
            "choices": [
                {"text": "节制使用，每周上网2小时", "effect": {"money": -56, "tech": +3, "happiness": -3}},
                {"text": "经常上网，探索互联网世界", "effect": {"money": -280, "tech": +10, "intelligence": +5}},
                {"text": "去图书馆了解互联网知识", "effect": {"money": -10, "intelligence": +8}}
            ]
        },
        {
            "title": "网络社交的开始",
            "year_range": "2001-2003",
            "content": "小张注册了QQ号码，惊喜地发现可以和远方的朋友实时聊天。很快，QQ表情、QQ秀和各种社交功能让人着迷。班级里同学们开始交换QQ号，网络社交逐渐成为日常生活的一部分。",
            "choices": [
                {"text": "积极使用QQ社交", "effect": {"money": -100, "social": +10, "happiness": +5}},
                {"text": "保持适度距离，主要与现实朋友联系", "effect": {"money": -30, "social": +3}},
                {"text": "不参与网络社交", "effect": {"money": 0, "social": -8}}
            ]
        },
        {
            "title": "网购初体验",
            "year_range": "2003-2005",
            "content": "大学生小李在淘宝网看中了一件T恤，价格比实体店便宜30%。但朋友警告说：'网购可能收到假货，或者根本收不到货！'另一个同学则分享了支付宝的担保交易经验，让他稍微安心了一些。",
            "choices": [
                {"text": "尝试淘宝网购", "effect": {"money": +100, "happiness": +5, "tech": +5}},
                {"text": "坚持实体店购物", "effect": {"money": -100, "happiness": -3}},
                {"text": "向有经验的朋友请教后再决定", "effect": {"intelligence": +5, "social": +3}}
            ]
        },
        {
            "title": "博客时代",
            "year_range": "2005-2007",
            "content": "张小姐听说博客很流行，注册了一个网易博客账号。她开始记录日常生活、分享想法，并关注一些知名博主。一篇关于城市生活的随笔意外获得了上百条评论，让她体验到了互联网的魅力。",
            "choices": [
                {"text": "定期更新博客", "effect": {"creativity": +10, "social": +8, "intelligence": +5}},
                {"text": "只阅读他人博客", "effect": {"intelligence": +5, "creativity": +3}},
                {"text": "放弃博客，回归传统日记", "effect": {"creativity": +3, "social": -5}}
            ]
        },
        {
            "title": "微博与移动互联",
            "year_range": "2009-2010",
            "content": "新浪微博上线后，140字的简短表达方式迅速吸引了大量用户。王先生发现许多名人都开通了微博账号，信息传播速度远超传统媒体。同时，手机上网的便利性也让社交媒体随时随地可以访问。",
            "choices": [
                {"text": "开通微博并积极参与讨论", "effect": {"social": +10, "intelligence": +5, "happiness": +5}},
                {"text": "注册账号但主要用来获取信息", "effect": {"intelligence": +8, "social": +3}},
                {"text": "对社交媒体保持距离", "effect": {"happiness": -3, "social": -5}}
            ]
        }
    ]
}

def get_digital_stories(year, category=None):
    """获取特定年份和类别的数码产品相关剧情"""
    stories = []
    
    # 筛选故事集合
    story_collections = DIGITAL_STORIES
    if category and category in DIGITAL_STORIES:
        story_collections = {category: DIGITAL_STORIES[category]}
    
    # 遍历所有故事类别
    for category, story_list in story_collections.items():
        for story in story_list:
            # 检查年份范围
            year_range = story["year_range"]
            years = year_range.split("-")
            start_year = int(years[0])
            end_year = int(years[1])
            
            if start_year <= year <= end_year:
                stories.append({
                    "category": category,
                    "story": story
                })
    
    return stories

def get_random_digital_event(year):
    """获取特定年份的随机数码产品相关事件"""
    import random
    
    # 获取该年份的所有产品
    year_products = get_products_by_year(year)
    
    # 随机事件模板
    event_templates = [
        "你在商场看到了新上市的{product}，售价{price}元，犹豫是否购买。",
        "朋友刚买了{product}，向你炫耀其{feature}功能，让你十分心动。",
        "单位发奖金，你考虑买一台{product}，提升自己的生活品质。",
        "电视广告里{product}的广告语'{slogan}'让你印象深刻，考虑尝试。",
        "科技杂志评测{product}获得了极高评价，称其{feature}领先同行。"
    ]
    
    # 随机广告语
    slogans = {
        "手机行业": ["科技以人为本", "为你而来", "非同凡想", "享受沟通", "科技让生活更简单"],
        "个人电脑": ["极速体验", "创新改变世界", "就是要你爽", "为梦想插上翅膀", "信息时代的伙伴"],
        "其他数码产品": ["定格精彩瞬间", "音乐改变生活", "娱乐无极限", "品质生活从此开始", "创意无限"],
        "通信与互联网": ["随时随地在线", "沟通从此不同", "网络无极限", "连接你我", "信息时代的桥梁"]
    }
    
    # 随机特性
    features = {
        "手机行业": ["超长待机", "高清拍照", "时尚外观", "强劲性能", "人性化操作"],
        "个人电脑": ["快速处理", "大屏显示", "轻薄便携", "游戏性能", "多媒体功能"],
        "其他数码产品": ["高清画质", "音质出众", "便携设计", "功能丰富", "时尚外观"],
        "通信与互联网": ["高速连接", "安全稳定", "智能推荐", "互动体验", "便捷服务"]
    }
    
    # 确保有产品可用
    if not year_products:
        return None
    
    # 随机选择一个类别和产品
    categories = list(year_products.keys())
    if not categories:
        return None
        
    category = random.choice(categories)
    category_products = year_products[category]
    
    if not category_products:
        return None
        
    product_info = random.choice(category_products)
    
    # 随机价格范围（根据类别调整）
    price_ranges = {
        "手机行业": (1000, 5000),
        "个人电脑": (3000, 12000),
        "其他数码产品": (500, 3000),
        "通信与互联网": (100, 1000)
    }
    
    price_range = price_ranges.get(category, (500, 5000))
    price = random.randint(price_range[0], price_range[1])
    
    # 随机选择一个特性和广告语
    feature = random.choice(features.get(category, features["其他数码产品"]))
    slogan = random.choice(slogans.get(category, slogans["其他数码产品"]))
    
    # 随机选择一个模板并填充
    template = random.choice(event_templates)
    
    # 获取产品名称
    product_name = ""
    if isinstance(product_info, dict):
        if "popular_products" in product_info and product_info["popular_products"]:
            product_name = random.choice(product_info["popular_products"])
        elif "title" in product_info:
            product_name = product_info["title"]
    
    # 如果没有找到产品名称，使用默认值
    if not product_name:
        default_products = {
            "手机行业": ["时尚手机", "智能手机", "功能机"],
            "个人电脑": ["新款电脑", "笔记本电脑", "台式机"],
            "其他数码产品": ["数码相机", "MP3播放器", "液晶电视"],
            "通信与互联网": ["上网设备", "通信工具", "网络应用"]
        }
        product_name = random.choice(default_products.get(category, ["数码产品"]))
    
    # 构建事件
    event = template.format(
        product=product_name,
        price=price,
        feature=feature,
        slogan=slogan
    )
    
    return {
        "event": event,
        "category": category,
        "product": product_name,
        "price": price,
        "year": year
    }

def generate_personal_digital_story(player_name, gender, year, category=None):
    """
    根据玩家信息生成个人化的数码产品体验故事
    
    参数:
    player_name: 玩家姓名
    gender: 性别 ('男'/'女')
    year: 年份
    category: 可选类别
    
    返回:
    包含标题、内容和选择的个人化故事
    """
    import random
    
    # 获取该年份的数码产品故事
    stories = get_digital_stories(year, category)
    
    # 如果没有找到故事，返回一个通用故事
    if not stories:
        return {
            "title": f"{year}年的数码记忆",
            "content": f"{player_name}对那个时代的数码产品记忆已经有些模糊了。或许是时候去电子市场看看，了解一下当时流行的产品。",
            "choices": [
                {"text": "去中关村电子市场逛逛", "effect": {"tech": +3, "intelligence": +2}},
                {"text": "翻阅电脑杂志了解信息", "effect": {"intelligence": +5}},
                {"text": "询问朋友关于流行数码产品", "effect": {"social": +3, "tech": +1}}
            ]
        }
    
    # 随机选择一个故事
    story_data = random.choice(stories)
    original_story = story_data["story"]
    
    # 根据玩家性别选择称谓
    player_title = "小伙子" if gender == "男" else "姑娘"
    
    # 性别相关词汇
    gender_words = {
        "男": {
            "friends": ["哥们", "同学", "室友", "同事"],
            "actions": ["研究", "把玩", "折腾", "组装"],
            "feelings": ["兴奋", "好奇", "跃跃欲试", "心动"]
        },
        "女": {
            "friends": ["闺蜜", "同学", "室友", "同事"],
            "actions": ["尝试", "体验", "探索", "学习"],
            "feelings": ["惊喜", "憧憬", "期待", "心动"]
        }
    }
    
    # 随机选择词汇
    friend = random.choice(gender_words[gender]["friends"])
    action = random.choice(gender_words[gender]["actions"])
    feeling = random.choice(gender_words[gender]["feelings"])
    
    # 根据原始故事改写个人化内容
    title = original_story["title"]
    
    # 构建个性化故事内容
    content = original_story["content"]
    
    # 替换故事中的通用名称为玩家名称和相关称谓
    content = content.replace("小李", player_name)
    content = content.replace("小王", player_name)
    content = content.replace("小张", player_name)
    content = content.replace("王先生", player_name)
    content = content.replace("李先生", player_name)
    content = content.replace("张先生", player_name)
    
    # 添加个人化元素
    personalized_content = f"{content}\n\n作为一个{player_title}，{player_name}感到十分{feeling}，迫不及待地想与{friend}分享这个新奇的体验，准备一起{action}一番。"
    
    # 保留原始选择
    choices = original_story["choices"]
    
    return {
        "title": title,
        "content": personalized_content,
        "choices": choices,
        "year": year,
        "category": story_data["category"]
    }

def generate_player_digital_memory(player_name, gender, year):
    """
    生成玩家在特定年份的数码产品回忆
    
    参数:
    player_name: 玩家姓名
    gender: 性别 ('男'/'女')
    year: 年份
    
    返回:
    回忆文本
    """
    import random
    
    # 获取该年份的流行产品
    popular_products = get_popular_products_by_year(year)
    
    if not popular_products:
        return f"{year}年，{player_name}对数码产品的记忆已经模糊。那是一个科技快速发展的年代，每个人都在适应日新月异的变化。"
    
    # 从各个类别中随机选择产品
    selected_products = []
    for category, products in popular_products.items():
        if products and len(products) > 0:
            selected_products.append(random.choice(products))
    
    if not selected_products:
        return f"{year}年，{player_name}对数码产品的记忆已经模糊。那是一个科技快速发展的年代，每个人都在适应日新月异的变化。"
    
    # 随机选择一个产品作为核心记忆
    main_product = random.choice(selected_products)
    
    # 性别相关词汇
    gender_words = {
        "男": {
            "activities": ["研究", "拆解", "组装", "玩游戏", "上网冲浪"],
            "places": ["网吧", "电子市场", "电脑城", "学校机房", "朋友家"],
            "emotions": ["兴奋", "好奇", "沉迷", "着迷", "满足"]
        },
        "女": {
            "activities": ["探索", "尝试", "聊天", "拍照", "听音乐"],
            "places": ["商场", "校园", "咖啡厅", "图书馆", "朋友家"],
            "emotions": ["惊喜", "好奇", "愉悦", "满足", "向往"]
        }
    }
    
    activity = random.choice(gender_words[gender]["activities"])
    place = random.choice(gender_words[gender]["places"])
    emotion = random.choice(gender_words[gender]["emotions"])
    
    # 构建记忆模板
    memory_templates = [
        f"{year}年，{player_name}还记得第一次见到{main_product['name']}时的{emotion}。那时候在{place}{activity}成了日常，这段数码产品初体验的记忆至今难忘。",
        
        f"{year}年的某个周末，{player_name}在{place}看到了刚上市的{main_product['name']}，当时就被深深吸引住了。攒了好几个月的零花钱才买下来，拿到手后整晚都在{activity}，感到无比{emotion}。",
        
        f"{main_product['name']}是{player_name}在{year}年接触的第一款{main_product['category']}产品。那时候，大家都在谈论这个新奇的玩意，{player_name}也跟着潮流，花了不少时间在{place}{activity}，体验那种{emotion}的感觉。",
        
        f"{year}年，{player_name}的朋友圈里都在讨论{main_product['name']}。看着别人用得那么开心，{player_name}也忍不住去{place}一探究竟。第一次{activity}的经历让{player_name}感到非常{emotion}，从此爱上了这类数码产品。",
        
        f"在{year}年那个科技快速发展的年代，{player_name}印象最深的就是{main_product['name']}了。每次在{place}{activity}时，总会引来旁人羡慕的目光。那种{emotion}的感觉，现在想起来仍然记忆犹新。"
    ]
    
    memory = random.choice(memory_templates)
    
    # 添加额外产品的提及
    if len(selected_products) > 1:
        extra_product = random.choice([p for p in selected_products if p != main_product])
        extra_templates = [
            f"除此之外，{player_name}还记得当时{extra_product['name']}也很流行，虽然没有亲自使用过，但经常在广告和朋友谈话中听说。",
            
            f"同一时期，{player_name}的朋友也在使用{extra_product['name']}，两人经常比较哪个更好用，争论不休。",
            
            f"那时候，市场上{extra_product['name']}和{main_product['name']}是竞争产品，{player_name}选择了后者，但时常好奇另一个选择会带来怎样不同的体验。"
        ]
        
        memory += " " + random.choice(extra_templates)
    
    return memory

def generate_digital_life_event(player_name, gender, year):
    """
    生成玩家在特定年份的数码生活事件
    
    参数:
    player_name: 玩家姓名
    gender: 性别 ('男'/'女')
    year: 年份
    
    返回:
    事件描述和选择
    """
    import random
    
    # 获取该年份的随机数码事件
    basic_event = get_random_digital_event(year)
    
    if not basic_event:
        # 如果没有找到事件，创建一个通用事件
        return {
            "event": f"{year}年，数码产品逐渐改变着{player_name}的生活，但具体是哪些产品，记忆已经有些模糊。",
            "choices": [
                {"text": "翻看老照片回忆当时的数码产品", "effect": {"happiness": +3, "intelligence": +2}},
                {"text": "询问老朋友当时流行什么", "effect": {"social": +5}},
                {"text": "上网查询那个年代的科技产品", "effect": {"tech": +3, "intelligence": +3}}
            ]
        }
    
    # 性别相关词汇
    gender_pronouns = "他" if gender == "男" else "她"
    gender_titles = {
        "男": ["大学生", "年轻人", "职场新人", "技术宅", "学生"],
        "女": ["大学生", "年轻人", "职场新人", "时尚达人", "学生"]
    }
    
    title = random.choice(gender_titles[gender])
    
    # 生成个人化事件
    event_templates = [
        f"{player_name}是一名{title}，{year}年的一天，{gender_pronouns}在商场看到了新上市的{basic_event['product']}，售价{basic_event['price']}元。看着展示柜里闪闪发光的产品，{gender_pronouns}犹豫着是否要购买。",
        
        f"{year}年，{player_name}的同学买了一台{basic_event['product']}，在聚会上向大家炫耀。作为一个{title}，{player_name}也很心动，但{basic_event['price']}元的价格让{gender_pronouns}有些踌躇。",
        
        f"作为一个热爱科技的{title}，{player_name}在{year}年一直关注着{basic_event['product']}的评测。杂志上说它'{basic_event['category']}领域的革命性产品'，{basic_event['price']}元的价格虽然不菲，但{gender_pronouns}还是很想拥有。",
        
        f"{year}年，{player_name}的生日快到了。作为一个{title}，{gender_pronouns}最想要的礼物就是当时热门的{basic_event['product']}。虽然售价高达{basic_event['price']}元，但这代表着那个时代年轻人的向往。",
        
        f"在{year}年的科技展上，{player_name}被一台{basic_event['product']}深深吸引。作为一个对数码产品充满好奇的{title}，{gender_pronouns}站在展台前许久，思考着是否值得花{basic_event['price']}元购买这个新玩意。"
    ]
    
    personalized_event = random.choice(event_templates)
    
    # 生成选择
    choices = [
        {"text": f"咬牙购买{basic_event['product']}", "effect": {"money": -basic_event['price'], "happiness": +10, "tech": +5}},
        {"text": f"暂时放弃，等价格下降再考虑", "effect": {"money": 0, "happiness": -3, "intelligence": +3}},
        {"text": f"购买功能类似但更便宜的替代品", "effect": {"money": -int(basic_event['price'] * 0.5), "happiness": +5, "tech": +3}}
    ]
    
    # 根据产品类别添加特殊选择
    special_choices = {
        "手机行业": {"text": f"向亲友借用体验几天再决定", "effect": {"social": +5, "tech": +3, "money": 0}},
        "个人电脑": {"text": f"自学电脑知识，组装一台性价比更高的", "effect": {"intelligence": +8, "tech": +10, "money": -int(basic_event['price'] * 0.7)}},
        "其他数码产品": {"text": f"在二手市场寻找品相好的二手产品", "effect": {"intelligence": +5, "money": -int(basic_event['price'] * 0.5), "happiness": +3}},
        "通信与互联网": {"text": f"找朋友合用，分摊费用", "effect": {"social": +8, "money": -int(basic_event['price'] * 0.3), "happiness": +2}}
    }
    
    if basic_event['category'] in special_choices:
        choices.append(special_choices[basic_event['category']])
    
    return {
        "title": f"{year}年的数码选择",
        "event": personalized_event,
        "choices": choices,
        "year": year,
        "product": basic_event['product'],
        "price": basic_event['price'],
        "category": basic_event['category']
    }

def generate_complete_digital_story_set(player_name, gender, birth_year=1980):
    """
    生成完整的90年代数码产品故事集
    
    参数:
    player_name: 玩家姓名
    gender: 性别 ('男'/'女')
    birth_year: 出生年份，用于计算玩家在特定年份的年龄
    
    返回:
    包含1996-2010年间玩家数码产品体验的故事集
    """
    stories = {}
    
    for year in range(1996, 2011):
        player_age = year - birth_year
        
        # 根据玩家年龄选择合适的故事类型
        if player_age < 10:  # 儿童
            category_weights = {
                "游戏设备": 0.5,
                "电脑变革": 0.3,
                "数码娱乐": 0.2
            }
        elif player_age < 18:  # 青少年
            category_weights = {
                "游戏设备": 0.3,
                "手机体验": 0.2,
                "电脑变革": 0.3,
                "数码娱乐": 0.2
            }
        elif player_age < 25:  # 大学/刚工作
            category_weights = {
                "手机体验": 0.3,
                "电脑变革": 0.3,
                "互联网生活": 0.3,
                "数码娱乐": 0.1
            }
        else:  # 成年
            category_weights = {
                "手机体验": 0.3,
                "电脑变革": 0.2,
                "互联网生活": 0.3,
                "其他数码产品": 0.2
            }
        
        # 创建年份故事集
        year_stories = {
            "personal_story": generate_personal_digital_story(player_name, gender, year),
            "memory": generate_player_digital_memory(player_name, gender, year),
            "life_event": generate_digital_life_event(player_name, gender, year),
            "player_age": player_age,
            "year": year
        }
        
        stories[year] = year_stories
    
    return stories
