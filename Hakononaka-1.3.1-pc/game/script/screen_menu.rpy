
init python:

    action_menu = [ ] #行动菜单列下有行动选项

    class Action(object):

        def __init__(self, title):
            self.kind = "action"
            self.title = title

            action_menu.append(self)

    class ActionItem(object):
 
        def __init__(self, label, title):
            self.kind = "choice"
            self.label = label
            self.title = title

            action_menu.append(self)

    Action(_("日常行动"))

    ActionItem("daily_talk",_("对话"))
    ActionItem("daily_feed",_("喂食"))
    ActionItem("daily_bath",_("清洁"))
    ActionItem("daily_pastime",_("娱乐"))
    ActionItem("daily_date",_("外出"))
    ActionItem("daily_none",_("什么都不做"))
    # ActionItem("daily_zuobi",_("作弊码"))

    Action(_("粉红行动"))

    ActionItem("sex_kiss",_("亲吻"))
    ActionItem("sex_fondle",_("爱抚"))
    ActionItem("sex_make_love",_("做爱"))
    

screen action_menu(adj):
    modal True

    frame:
        xsize 640
        xalign .5
        ysize 550
        ypos 40
        padding (20,20)
        background "#7a7a7abc"


        has side "c r b"

        viewport:
            yadjustment adj
            mousewheel True
            draggable True

            vbox:

                spacing 30  # 增大按钮间距，适合触摸
                for i in action_menu:

                    if i.kind == "choice":

                        textbutton i.title:
                            action Return(i)
                            # left_padding 20
                            # xfill True
                            style "navigation_button1"           # 应用按钮样式
                            text_style "navigation_button1_text" # 应用文字样式                            


                    else:

                        # null height 10
                        text i.title alt ""
                        # null height 5

        bar adjustment adj style "vscrollbar"

        textbutton _("月的状态"):
            xfill True
            action Return(False)
            top_margin 15


# This is used to preserve the state of the scrollbar on the selection
# screen.
default action_adjustment = ui.adjustment()

default choice_adjustment = ui.adjustment()

# 状态描述映射表
init python:
    # 饱食度状态
    satiety_descriptions = {
        (0, 20): _("极度饥饿"),
        (21, 40): _("非常饥饿"),
        (41, 60): _("饥饿"),
        (61, 80): _("一般"),
        (81, 100): _("饱腹"),
    }
    
    # 清洁度状态
    clean_descriptions = {
        (0, 20): _("非常肮脏"),
        (21, 40): _("肮脏"),
        (41, 60): _("一般"),
        (61, 100): _("干净"),
    }
    
    # 压力值状态
    stress_descriptions = {
        (0, 30): _("轻松"),
        (31, 40): _("平静"),
        (41, 50): _("不安"),
        (51, 60): _("轻微烦躁"),
        (61, 70): _("焦虑"),
        (71, 80): _("抑郁"),
        (81, 90): _("躁狂"),
        (91, 100): _("精神崩溃")
    }

    # 好感度状态
    affection_descriptions = {
        (0, 10): _("仇恨"),
        (11, 20): _("厌恶"),
        (21, 30): _("反感"),
        (31, 40): _("冷漠"),
        (41, 60): _("普通"),
        (61, 70): _("友好"),
        (71, 80): _("有好感"),
        (81, 100): _("爱慕"),
    }

    # 健康值状态
    health_descriptions = {
        (0, 10): _("濒临死亡"),
        (11, 20): _("生命垂危"),
        (21, 30): _("极度虚弱"),
        (31, 40): _("严重不适"),
        (41, 50): _("身体虚弱"),
        (51, 60): _("状态较差"),
        (61, 70): _("一般"),
        (71, 80): _("状态良好"),
        (81, 100): _("健康"),

    }

    # 状态判断函数
    def get_status_description(value, descriptions):
        for (low, high), desc in descriptions.items():
            if low <= value <= high:
                return desc
        return "未知状态"    

# 角色状态菜单（内联颜色判断，终极版）
screen status():
    modal True
    frame:
        xsize 900
        xalign 0.39
        ysize 650
        ypos 40
        padding (20, 40)
        background "#a0a0a0bc"
        
        vbox:
            spacing 15  # 增加间距，避免进度条拥挤
            text _("当前天数为day[day]")
            text _("目前剩余行动点数:[action_points]")
            
            # 饱食度显示（带进度条）

            hbox:
                text _("饱食度："):
                    min_width 80  # 固定标签宽度，对齐更整齐
                    yalign 0.5
                bar:
                    value AnimatedValue(satiety, satiety_max, 1.0)  # 动画过渡效果
                    xmaximum 200  # 进度条宽度
                    ysize 26      # 进度条高度
                    yalign 0.5
                text " [satiety]/[satiety_max] ([get_status_description(satiety, satiety_descriptions)])":
                    yalign 0.5
                    
            
            # 清洁度显示(带进度条)
          
            hbox:
                text _("清洁度："):
                    min_width 80
                    yalign 0.5
                bar:
                    value AnimatedValue(clean, clean_max, 1.0)
                    xmaximum 200
                    ysize 26
                    yalign 0.5
                text " [clean]/[clean_max] ([get_status_description(clean, clean_descriptions)])":
                    yalign 0.5
                     
            
            # 压力值显示(带进度条)
            hbox:
                text _("压力值："):
                    min_width 80
                    yalign 0.5
                bar:
                    value AnimatedValue(stress, stress_max, 1.0)
                    xmaximum 200
                    ysize 26
                    yalign 0.5
                text " [stress]/[stress_max] ([get_status_description(stress, stress_descriptions)])":
                    yalign 0.5
                     
            
            # 好感度显示(带进度条)
   
            hbox:
                text _("好感度："):
                    min_width 80
                    yalign 0.5
                bar:
                    value AnimatedValue(affection, affection_max, 1.0)
                    xmaximum 200
                    ysize 26
                    yalign 0.5
                text " [affection]/[affection_max] ([get_status_description(affection, affection_descriptions)])":
                    yalign 0.5
                     
            
            # 健康度显示(带进度条)

            hbox:
                text _("健康值："):
                    min_width 80
                    yalign 0.5
                bar:
                    value AnimatedValue(health, health_max, 1.0)
                    xmaximum 200
                    ysize 26
                    yalign 0.5
                text " [health]/[health_max] ([get_status_description(health, health_descriptions)])":
                    yalign 0.5
                
                    
                     
            
            # 体力值显示(带进度条）

            hbox:
                text _("体力值："):
                    min_width 80
                    yalign 0.5
                bar:
                    value AnimatedValue(stamina, stamina_max, 1.0)
                    xmaximum 200
                    ysize 26
                    yalign 0.5
                text " [stamina]/[stamina_max]":
                    yalign 0.5
                     
            
            textbutton _("选择行动"):
                xsize 500
                xalign 0
                action Return(False)
                style "button"

################################################################################
#右上角状态简易菜单常态化
################################################################################
""" default day = 1                 # 当前天数
default action_points = 3         # 每日行动点数
default stamina = 100             #体力值
default stamina_max = 100
default affection = 0             # 好感度 (0 到 100)
default affection_max = 100       
default stress = 35               # 压力值 (0 到 100)
default stress_max = 100          
default health = 100              # 健康度 (0 到 100)
default health_max = 100              
default player_choice = None      # 玩家当前选择
default status_menu_open = False  # 状态菜单是否打开 """

# This screen displays a single stat.
screen single_stat():

    frame:
        xsize 600
        ysize 380
        ypos 40
        xpos 1300
        padding (20, 20)
        background "#c6c6c6bc"

        vbox:
            spacing 5

            hbox:
                text _("天数：[day]" )

            hbox:
                text _("行动点数：[action_points]") 

            hbox:
                text _("体力值："):
                    min_width 40
                    yalign 0.5

                bar:
                    value AnimatedValue(stamina, stamina_max, 1.0)
                    xmaximum 180
                    ysize 26
                    yalign 0.5

                text " [stamina]/[stamina_max]":
                    yalign 0.5

            hbox:
                text _("好感度："):
                    min_width 40
                    yalign 0.5

                bar:
                    value AnimatedValue(affection, affection_max, 1.0)
                    xmaximum 180
                    ysize 26
                    yalign 0.5

                text " [affection]/[affection_max]":
                    yalign 0.5

            hbox:
                text _("压力值："):
                    min_width 40
                    yalign 0.5

                bar:
                    value AnimatedValue(stress, stress_max, 1.0)
                    xmaximum 180
                    ysize 26
                    yalign 0.5

                text " [stress]/[stress_max]":
                    yalign 0.5

            hbox:
                text _("健康值："):
                    min_width 40
                    yalign 0.5

                bar:
                    value AnimatedValue(health, health_max, 1.0)
                    xmaximum 180
                    ysize 26
                    yalign 0.5

                text " [health]/[health_max]":
                    yalign 0.5


# 输入变量
screen stats():
    use single_stat()



# 英文翻译（Python字典格式）
translate english python:
    # 饱食度状态
    satiety_descriptions = {
        (0, 20): "Extremely Hungry",
        (21, 40): "Very Hungry",
        (41, 60): "Hungry",
        (61, 80): "Normal",
        (81, 100): "Full",
    }
    
    # 清洁度状态
    clean_descriptions = {
        (0, 20): "Very Dirty",
        (21, 40): "Dirty",
        (41, 60): "Normal",
        (61, 100): "Clean",
    }
    
    # 压力值状态
    stress_descriptions = {
        (0, 30): "Relaxed",
        (31, 40): "Calm",
        (41, 50): "Uneasy",
        (51, 60): "Slightly Irritable",
        (61, 70): "Anxious",
        (71, 80): "Depressed",
        (81, 90): "Manic",
        (91, 100): "Mentally Collapsed"
    }

    # 好感度状态
    affection_descriptions = {
        (0, 10): "Hatred",
        (11, 20): "Disgust",
        (21, 30): "Antipathy",
        (31, 40): "Indifference",
        (41, 60): "Normal",
        (61, 70): "Friendly",
        (71, 80): "Like",
        (81, 90): "Admiration",
        (91, 100): "Deep Love"
    }

    # 健康值状态
    health_descriptions = {
        (0, 10): "Near Death",
        (11, 20): "Critical Condition",
        (21, 30): "Extremely Weak",
        (31, 40): "Severely Unwell",
        (41, 50): "Physically Weak",
        (51, 60): "Poor Condition",
        (61, 70): "Normal",
        (71, 80): "Good Condition",
        (81, 100): "Healthy",
    }


# 日文翻译（Python字典格式）
translate japanese python:
    # 饱食度状态　
    satiety_descriptions = {
        (0, 20): "極度の空腹",
        (21, 40): "非常に空腹",
        (41, 60): "空腹",
        (61, 80): "普通",
        (81, 100): "満腹",
    }
    
    # 清洁度状态
    clean_descriptions = {
        (0, 20): "非常に汚い",
        (21, 40): "汚い",
        (41, 60): "普通",
        (61, 100): "清潔",
    }
    
    # 压力值状态
    stress_descriptions = {
        (0, 30): "リラックス",
        (31, 40): "平静",
        (41, 50): "不安",
        (51, 60): "少しイライラ",
        (61, 70): "不安",
        (71, 80): "鬱陶しい",
        (81, 90): "躁病",
        (91, 100): "精神崩壊"
    }

    # 好感度状态
    affection_descriptions = {
        (0, 10): "憎しみ",
        (11, 20): "嫌悪",
        (21, 30): "反感",
        (31, 40): "無関心",
        (41, 60): "普通",
        (61, 70): "友好的",
        (71, 80): "好き",
        (81, 90): "愛情",
        (91, 100): "深い愛"
    }

    # 健康值状态
    health_descriptions = {
        (0, 10): "死亡寸前",
        (11, 20): "危篤状態",
        (21, 30): "極度の衰弱",
        (31, 40): "重度の不快感",
        (41, 50): "体が虚弱",
        (51, 60): "状態が悪い",
        (61, 70): "普通",
        (71, 80): "状態が良好",
        (81, 100): "健康",
    }
