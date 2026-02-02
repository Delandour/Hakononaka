default showing_effect = False
default effect_type = ""
default effect_timer = 0.0
default Light_room_state = 0
default daily_gift_count = 0
default Light_watch = False
default Light_photo = False
default Light_mirror = False
default Light_brush = False
default Light_light = False
default Light_sexbang = False
default Light_flower = False
default Light_book = False
default Light_cake = False
default Light_cookie = False
default Light_newspaper = False

default flower_points = 0
default flower_days = 0
default cookie_days = 0

default Light_room_points = 0

init python:
    def randomize_Light_state():
        if unlock_the_handcuffs == False:
            store.Light_room_state = random.randint(0, 5)
        else:
            store.Light_room_state = random.randint(0, 6) 

    def hide_all_light_effects():
        """隐藏所有月的房间效果图片"""
        renpy.hide("Y_lay_1")
        renpy.hide("Y_lay_2")
        renpy.hide("Y_lay_3")
        renpy.hide("Y_sleep_1")
        renpy.hide("Y_sleep_2")
        renpy.hide("Y_sleep_3")
        renpy.hide("Y_sit_1")
        renpy.hide("Y_sit_2")
        renpy.hide("Y_sit_3")
        renpy.hide("Y_stand_1")
        renpy.hide("Y_stand_2")
        renpy.hide("Y_stand_3")
        renpy.hide("Y_chair_1")
        renpy.hide("Y_chair_2")
        renpy.hide("Y_chair_3")
        renpy.hide("Y_sit2_1")
        renpy.hide("Y_sit2_2")
        renpy.hide("Y_sit2_3")
        renpy.hide("Y_sleep2_1")
        renpy.hide("Y_sleep2_2")
        renpy.hide("Y_sleep2_3")
        renpy.hide("LY_book_1")
        renpy.hide("LY_book_2")
        renpy.hide("LY_chess")
        renpy.hide("LY_sex")
    
    def reset_light_room():
        """重置月的房间状态"""
        store.showing_effect = False
        store.effect_timer = 0.0
        store.effect_type = ""
        hide_all_light_effects()

    def get_affection_suffix():
        """根据好感度返回对应的表情后缀"""
        if affection < 50:
            return "_1"  # 烦
        elif affection < 70:
            return "_2"  # 乐
        else:
            return "_3"  # 心

    def show_Light_effect(state):
        """显示月的效果图片"""
        # 先清理可能存在的旧效果
        hide_all_light_effects()
        
        store.showing_effect = True
        store.effect_type = state
        store.effect_timer = 3.0
        
        # 获取好感度对应的表情后缀
        affection_suffix = get_affection_suffix()
        
        # 显示对应的效果图片
        if state == "lay":
            renpy.show("Y_lay" + affection_suffix, at_list=[fade_in_out])
        elif state == "sleep":
            renpy.show("Y_sleep" + affection_suffix, at_list=[fade_in_out])
        elif state == "sit":
            renpy.show("Y_sit" + affection_suffix, at_list=[fade_in_out])
        elif state == "stand":
            renpy.show("Y_stand" + affection_suffix, at_list=[fade_in_out])
        elif state == "chair":
            renpy.show("Y_chair" + affection_suffix, at_list=[fade_in_out])
        elif state == "sit2":
            renpy.show("Y_sit2" + affection_suffix, at_list=[fade_in_out])
        elif state == "sleep2":
            renpy.show("Y_sleep2" + affection_suffix, at_list=[fade_in_out])


screen Light_room():
    $ Light_room_points += 1

    zorder 90  # 确保在其他屏幕之上
    modal True   # 阻止其他交互

    # 屏幕隐藏时自动清理
    on "hide" action Function(reset_light_room)
    
    # 效果显示控制
    if showing_effect:
        timer 0.1 repeat True action If(
            effect_timer > 0,
            SetVariable("effect_timer", effect_timer - 0.1),
            SetVariable("showing_effect", False)
        )    

    # 房间内容
    fixed:
        # 房间背景
        if Light_room_state in [1, 3, 5]:
            add "Light_room_2"
        elif Light_room_state == 4:
            add "Light room_chess"
        else:
            add "Light_room_1"

        if Light_room_state in [0, 1, 2, 3, 5 ,6]:
            if Light_flower:
                add "gift_flower_a"
            if Light_cake:
                add "gift_cake_a"
            if Light_newspaper:
                add "gift_newspaper_a"
            if Light_light:
                add "gift_light_a"

        if Light_book:
            add "gift_book_a"
        if Light_mirror:
            add "gift_mirror_a"
        if Light_cookie:
            add "gift_cookie_a"
        if Light_photo:
            add "gift_photo_a"
        if Light_watch:
            add "gift_watch_a"
        if Light_brush:
            add "gift_brush_a"

        # 获取好感度对应的表情后缀
        $ affection_suffix = get_affection_suffix()

        if unlock_the_handcuffs == False:
            # 根据当前状态显示对应的小人图片
            if Light_room_state == 0:
                imagebutton:
                    idle "Y_lay_0"
                    hover "Y_lay_0"
                    action Function(show_Light_effect, "lay")
                    align (0.6, 0.8)
            elif Light_room_state == 1:
                imagebutton:
                    idle "Y_sleep_0"
                    hover "Y_sleep_0" 
                    action Function(show_Light_effect, "sleep")
                    align (0.8, 0.6)
            elif Light_room_state == 2:
                imagebutton:
                    idle "Y_sit_0"
                    hover "Y_sit_0"
                    action Function(show_Light_effect, "sit")
                    align (0.7, 0.55)
            elif Light_room_state == 3:
                imagebutton:
                    idle "LY_book_1"
                    hover "LY_book_1"
                    align (0.75, 0.48)
            elif Light_room_state == 4:
                imagebutton:
                    idle "LY_chess"
                    hover "LY_chess"
                    align (0.7, 0.78)
            elif Light_room_state == 5:
                imagebutton:
                    idle "LY_sex"
                    hover "LY_sex"
                    align (0.8, 0.55)

                    
            # 显示效果图片（在原图相同位置，更高层级）
            if showing_effect:
                if effect_type == "lay":
                    add "Y_lay" + affection_suffix:
                        align (0.6, 0.8)  # 与原图相同的位置
                        at fade_in_out
                elif effect_type == "sleep":
                    add "Y_sleep" + affection_suffix:
                        align (0.8, 0.6)  # 与原图相同的位置
                        at fade_in_out
                elif effect_type == "sit":
                    add "Y_sit" + affection_suffix:
                        align (0.7, 0.55) # 与原图相同的位置
                        at fade_in_out



        else:
            # 根据当前状态显示对应的小人图片
            if Light_room_state == 0:
                imagebutton:
                    idle "Y_stand_0"
                    hover "Y_stand_0"
                    action Function(show_Light_effect, "stand")
                    align (0.6, 0.8)
            elif Light_room_state == 1:
                imagebutton:
                    idle "Y_sleep2_0"
                    hover "Y_sleep2_0" 
                    action Function(show_Light_effect, "sleep2")
                    align (0.8, 0.6)
            elif Light_room_state == 2:
                imagebutton:
                    idle "Y_sit2_0"
                    hover "Y_sit2_0"
                    action Function(show_Light_effect, "sit2")
                    align (0.7, 0.55)
            elif Light_room_state == 3:
                imagebutton:
                    idle "LY_book_2"
                    hover "LY_book_2"
                    align (0.75, 0.48)
            elif Light_room_state == 4:
                imagebutton:
                    idle "LY_chess"
                    hover "LY_chess"
                    align (0.7, 0.78)
            elif Light_room_state == 5:
                imagebutton:
                    idle "LY_sex"
                    hover "LY_sex"
                    align (0.8, 0.55)
            elif Light_room_state == 6:
                imagebutton:
                    idle "Y_chair_0"
                    hover "Y_chair_0"
                    action Function(show_Light_effect, "chair")
                    align (0.295, 0.5)

            # 显示效果图片（在原图相同位置，更高层级）
            if showing_effect:
                if effect_type == "stand":
                    add "Y_stand" + affection_suffix:
                        align (0.6, 0.8)  # 与原图相同的位置
                        at fade_in_out
                elif effect_type == "sleep2":
                    add "Y_sleep2" + affection_suffix:
                        align (0.8, 0.6)  # 与原图相同的位置
                        at fade_in_out
                elif effect_type == "sit2":
                    add "Y_sit2" + affection_suffix:
                        align (0.7, 0.55) # 与原图相同的位置
                        at fade_in_out
                elif effect_type == "chair":
                    add "Y_chair" + affection_suffix:
                        align (0.295, 0.5) # 与原图相同的位置
                        at fade_in_out

        # 关闭按钮
        textbutton _("关闭"):
            style "quick_button1"
            background "#b4b4b4cd"
            hover_background "#4460fea7"
            align (0.95, 0.95)
            action Hide("Light_room")

        # 商店按钮
        textbutton _("礼物商店"):
            style "quick_button1"
            background "#b4b4b4cd"
            hover_background "#4460fea7"
            align (0.95, 0.05)
            action Show("gift_store")

        
        textbutton _("新手帮助"):
            style "quick_button1"
            background "#b4b4b4cd"
            hover_background "#4460fea7"
            align (0.95, 0.18)
            action Jump("room_jiaocheng")


label room_jiaocheng:

    hide screen Light_room 

    if unlock_the_handcuffs:
        scene Light_room_4 with dissolve
    else:
        scene Light_room_3 with dissolve

    sy"""

    欢迎来到月的房间！在这里你可以观察月在做什么，月的状态每次进入时都会刷新哦。（注意，月的房间内的状态与行动剧情无关。）

    虽然囚室很简陋，但是通过送礼可以小小地改善这一点呢。在游戏进行到7天之后，给月解开镣铐后，点击右上角的【礼物商店】试试吧！

    每天都可以赠送一次礼物！不过需要注意的是，如果关系太差，月是不会接受L的礼物的哦。

    送礼不会花费行动点数，所以请多多送礼吧！有一些礼物还会产生组合反应，不知道你能不能触发彩蛋呢~

    教程结束，现在回到行动界面。

    """
    if unlock_the_handcuffs:
        if affection >= 60:
            scene main bg_4 with dissolve
            $ persistent.unlock_3 = True
        else:
            scene main bg_3 with dissolve
            $ persistent.unlock_2 = True
    else:  
        if affection >= 60:
            scene main bg_2 with dissolve
            $ persistent.unlock_1 = True
        else:
            scene main bg_1 with dissolve
    jump action_menu

screen gift_store:
    zorder 90
    modal True
    frame:
        xsize 1030
        xalign 0.44
        ysize 650
        ypos 40
        padding (20, 40)
        background "#a0a0a0bc"

        vbox:
            text _("可重复赠送的礼物")
            grid 3 3:
                spacing 10
                textbutton _("一束鲜切花"):
                    style "quick_button1"
                    action Jump("gift_flower")   # 调用鲜切花标签
                textbutton _("一本书"):
                    style "quick_button1"
                    action Jump("gift_book")   
                textbutton _("一叠报纸"):
                    style "quick_button1"
                    action Jump("gift_newspaper")   
                textbutton _("铁盒饼干"):
                    style "quick_button1"
                    action Jump("gift_cookie")   
                textbutton _("切角蛋糕"):
                    style "quick_button1"
                    action Jump("gift_cake")   
        
            text _("不可重复赠送的礼物")
            grid 3 3:
                spacing 10
                # 月的手表按钮：同理修改
                if day >= 7:
                    if unlock_the_handcuffs:
                        textbutton _("解开镣铐√"):
                            style "quick_button1"
                            action Jump("give_gift_1")
                    else:
                        textbutton _("解开镣铐"):
                            style "quick_button1"
                            action Jump("unlock_handcuff") 

                if Light_watch:                                     
                    textbutton _("月的手表√"):
                        style "quick_button1"
                        action Jump("give_gift_1")
                else:
                    textbutton _("月的手表"):
                        style "quick_button1"
                        action Jump("gift_watch")

                if Light_photo:                                     
                    textbutton _("家庭相框√"):
                        style "quick_button1"
                        action Jump("give_gift_1")  
                else:
                    textbutton _("家庭相框"):
                        style "quick_button1"
                        action Jump("gift_photo")  

                if Light_mirror:
                    textbutton _("小镜子√"):
                        style "quick_button1"
                        action Jump("give_gift_1")   
                else:
                    textbutton _("小镜子"):
                        style "quick_button1"
                        action Jump("gift_mirror")   

                if Light_brush:
                    textbutton _("木梳√"):
                        style "quick_button1"
                        action Jump("give_gift_1")   
                else:
                    textbutton _("木梳"):
                        style "quick_button1"
                        action Jump("gift_brush")   

                if Light_light:
                    textbutton _("台灯√"):
                        style "quick_button1"
                        action Jump("give_gift_1")   
                else:
                    textbutton _("台灯"):
                        style "quick_button1"
                        action Jump("gift_light")   
                    
                if make_love_points > 2:
                    if Light_sexbang:
                        textbutton _("{size=-5}银制尿道棒√{/size}"):
                            style "quick_button1"
                            action Jump("give_gift_1")
                    else:
                        textbutton _("银制尿道棒"):
                            style "quick_button1"
                            action Jump("gift_sexbang")
        
            textbutton _("关闭"):
                yalign 1.0
                style "quick_button1"
                # background "#b4b4b4cd"
                # hover_background "#4460fea7"
                action Hide("gift_store")


      


# 可重复赠送的礼物
label gift_flower:
    hide screen gift_store
    hide screen Light_room
    if unlock_the_handcuffs:
        scene Light_room_4 with dissolve
    else:
        scene Light_room_3 with dissolve

    if Light_flower:
        show gift_flower_a
    if Light_cake:
        show gift_cake_a
    if Light_newspaper:
        show gift_newspaper_a
    if Light_light:
        show gift_light_a
    if Light_book:
        show gift_book_a
    if Light_mirror:
        show gift_mirror_a
    if Light_cookie:
        show gift_cookie_a
    if Light_photo:
        show gift_photo_a
    if Light_watch:
        show gift_watch_a
    if Light_brush:
        show gift_brush_a

    if affection < 50:
        "现在就算给夜神君送礼物也会被丢出来的吧，还是等关系变好一点再说吧。"
        jump after_gift

    if unlock_the_handcuffs == False:
        "现在手铐还没有解开，为了表示友好，还是先把对方的手铐解开吧。"
        jump after_gift
    show gift_flower at jubu with dissolve
    sy"简介：这是一束鲜切花，散发着淡淡的芳香。"
    menu:
        "要赠送这件礼物给夜神月吗？"
        "是的。":
            if daily_gift_count >= 1:
                sy"今日已赠送过礼物，明天再来吧～"
                jump after_gift
            else:
                if flower_days > 0:
                    
                    "L拿来新的花束替换了花瓶里那束已经有些发蔫的鲜花。"
                    Y smile2"没想到你还挺上心的嘛。"
                    L smile3"夜神君看见新鲜的花朵心情也会更好吧？"
                    "夜神月的表情变得柔和了些。"
                    Y smile1"谢谢。"
                    hide gift_flower with dissolve
                    $ flower_points += 1
                    $ Light_flower = True
                    $ flower_days = 3
                    $ flower_tixing = True
                    if unlock_the_handcuffs:
                        $ affection = min(affection + 1, 75)
                    else:
                        $ affection = min(affection + 1, 70)
                    $ daily_gift_count += 1 
                    jump after_gift

                else:
                    
                    """ 当L从身后掏出一束鲜切花递给月时，这名在校园里十分受欢迎的漂亮青年忍不住呆滞了几秒钟。

                    月的视线从散发着芬芳气味的花束移到L的面瘫脸上，又移了回去，反复几次，怀疑L是不是脑子坏掉了。 """

                    Y fadai"你送我这个干什么？"

                    L order2"科学研究表明，花朵的色彩和气味会刺激人的大脑分泌多巴胺和血清素，从而使人感到愉悦……"

                    Y pt"你知道我问的不是这个，龙崎。不要假装成百科全书装傻。"

                    Y"再说这种话我就当你明恋我，然后因为害羞烧坏了脑子。"

                    L unhappy"嘴上也太不留情了，夜神君。"

                    L pt"倒是没有别的意思，只是在不能外出的时候，看见新鲜的花朵人也许会感到愉悦吧。毕竟这里太单调了。"

                    """ 月闻言只是轻笑一声。 """

                    Y smile2"是渡先生给你的建议吗？"

                    L unhappy"夜神君不信任我的情商吗？真是令人伤心。"

                    L thinking"我会准备花瓶的，这样这束花也能盛开得久一点吧。"
                    hide gift_flower with dissolve
                    $ flower_points += 1
                    $ flower_days = 3
                    $ Light_flower = True
                    $ flower_tixing = True
                    if unlock_the_handcuffs:
                        $ affection = min(affection + 1, 75)
                    else:
                        $ affection = min(affection + 1, 70)
                    $ daily_gift_count += 1 
                    jump after_gift

        "不了，我再想想吧。":
            
            sy"好的，返回行动界面。"
            jump after_gift

label gift_book:
    hide screen gift_store
    hide screen Light_room
    if unlock_the_handcuffs:
        scene Light_room_4 with dissolve
    else:
        scene Light_room_3 with dissolve
        
    if Light_flower:
        show gift_flower_a
    if Light_cake:
        show gift_cake_a
    if Light_newspaper:
        show gift_newspaper_a
    if Light_light:
        show gift_light_a
    if Light_book:
        show gift_book_a
    if Light_mirror:
        show gift_mirror_a
    if Light_cookie:
        show gift_cookie_a
    if Light_photo:
        show gift_photo_a
    if Light_watch:
        show gift_watch_a
    if Light_brush:
        show gift_brush_a
    if affection < 50:
        "现在就算给夜神君送礼物也会被丢出来的吧，还是等关系变好一点再说吧。"
        jump after_gift

    if unlock_the_handcuffs == False:
        "现在手铐还没有解开，为了表示友好，还是先把对方的手铐解开吧。"
        jump after_gift
    show gift_book at jubu with dissolve
    sy"简介：L挑选了一本月可能喜欢的书，硬皮精装本，纸页雪白厚实，唯一需要担心的是在他们吵架时会被当成武器使用。"
    menu:
        "要赠送这件礼物给夜神月吗？"
        "是的。":
            if daily_gift_count >= 1:
                sy"今日已赠送过礼物，明天再来吧～"
                jump after_gift
            else:
                
                L"因为我不能经常来陪夜神君，所以夜神君无聊的时候请看书来打发时间吧。"

                Y han"（谁要你经常来陪啊。）"

                Y smile2"龙崎真是考虑周全呢，这本书我有所耳闻，刚好是之前感兴趣却没来得及看的书，谢谢。"

                L smile3"夜神君喜欢就太好了，毕竟我是靠推理来判断你会不会喜欢的。"

                Y pt"（不要自以为很了解我啊，L这家伙。）"

                Y smile2"""不愧是龙崎呢，读书的确是很好的解乏方式。
                
                如果之后龙崎也愿意来和我一起读书的话，我会很开心的。
                """
                $ Light_book= True
                L smile3"会有这个机会的，等我处理完手上的工作。"
                hide gift_book with dissolve
                if unlock_the_handcuffs:
                    $ affection = min(affection + 2, 75)
                else:
                    $ affection = min(affection + 2, 70)
                $ daily_gift_count += 1 
                jump after_gift

        "不了，我再想想吧。":
            
            sy"好的，返回行动界面。"
            jump after_gift

label gift_newspaper:
    hide screen gift_store
    hide screen Light_room
    if unlock_the_handcuffs:
        scene Light_room_4 with dissolve
    else:
        scene Light_room_3 with dissolve

    if Light_flower:
        show gift_flower_a
    if Light_cake:
        show gift_cake_a
    if Light_newspaper:
        show gift_newspaper_a
    if Light_light:
        show gift_light_a
    if Light_book:
        show gift_book_a
    if Light_mirror:
        show gift_mirror_a
    if Light_cookie:
        show gift_cookie_a
    if Light_photo:
        show gift_photo_a
    if Light_watch:
        show gift_watch_a
    if Light_brush:
        show gift_brush_a
    if affection < 50:
        "现在就算给夜神君送礼物也会被丢出来的吧，还是等关系变好一点再说吧。"
        jump after_gift

    if unlock_the_handcuffs == False:
        "现在手铐还没有解开，为了表示友好，还是先把对方的手铐解开吧。"
        jump after_gift
    show gift_newspaper at jubu with dissolve
    sy"简介：一叠当下最新的报纸，月终于知道今天是几月几日了。太阳底下无新事，反反复复还是那些。"
    menu:
        "要赠送这件礼物给夜神月吗？"
        "是的。":
            if daily_gift_count >= 1:
                sy"今日已赠送过礼物，明天再来吧～"
                jump after_gift
            else:
                
                L smile3"夜神君很想知道外面发生了什么事情吧，所以今天特意带来了报纸。"

                """ 月的目光紧盯着L手里的报纸，毫不掩饰自己的兴趣。

                虽然L肯定筛选过内容，但是闭塞的环境还是让月渴望新的见闻。 """

                Y"啊啊，那真是太感谢了，我还在想龙崎会不会故意把我关到和社会脱节呢。"

                L thinking"以夜神君的聪明才智，要做到这一点还是有点难度吧。可能要进行以五年为单位的囚禁呢。"

                Y han"（……这家伙，一点委屈都不愿意受啊。）"

                """ 月先随意翻看了一下报纸，当然格外注意了和【L】与【Kira】有关的内容，但是很遗憾，在Kira被捕后，民众仿佛已经对Kira失去了兴趣，回到了Kira出世前无聊的日常中。

                月抿着嘴唇，不可避免地有些失望。

                仔细算算，从他主动接受囚禁开始已经过去了快一年的时光，他使用笔记的时间也只有大半年。果然，Kira的影响力还是不够吗？民众的忘性就如此之大吗？ """

                L pt"夜神君可以慢慢看，第二天早上我会来回收的。"

                Y pt"嗯，谢谢。"

                """ L瞥了一眼月有些沮丧的脸，不意外Kira的年轻心性。

                如果赢的是夜神月，他可能会被当做宗教首领一样崇拜吧，只是这个苗头已经被掐灭了，平庸的大众只会去找寻下一个能够打发时间的热点新闻。 """
                hide gift_newspaper with dissolve
                $ Light_newspaper= True
                if unlock_the_handcuffs:
                    $ affection = min(affection + 1, 75)
                else:
                    $ affection = min(affection + 1, 70)
                $ daily_gift_count += 1 
                jump after_gift

        "不了，我再想想吧。":
            
            sy"好的，返回行动界面。"
            jump after_gift

label gift_cookie:
    hide screen gift_store
    hide screen Light_room
    if unlock_the_handcuffs:
        scene Light_room_4 with dissolve
    else:
        scene Light_room_3 with dissolve

    if Light_flower:
        show gift_flower_a
    if Light_cake:
        show gift_cake_a
    if Light_newspaper:
        show gift_newspaper_a
    if Light_light:
        show gift_light_a
    if Light_book:
        show gift_book_a
    if Light_mirror:
        show gift_mirror_a
    if Light_cookie:
        show gift_cookie_a
    if Light_photo:
        show gift_photo_a
    if Light_watch:
        show gift_watch_a
    if Light_brush:
        show gift_brush_a

    if affection < 50:
        "现在就算给夜神君送礼物也会被丢出来的吧，还是等关系变好一点再说吧。"
        jump after_gift

    if unlock_the_handcuffs == False:
        "现在手铐还没有解开，为了表示友好，还是先把对方的手铐解开吧。"
        jump after_gift
    show gift_cookie at jubu with dissolve
    sy"""简介：一盒多口味的曲奇饼干，L不知道月对于甜食的喜好，那就全都来一遍，从自己惯吃的牌子里选了口味最多的那一款。
    
    盒身印着精美的花纹，独立包装防潮保鲜。"""
    menu:
        "要赠送这件礼物给夜神月吗？"
        "是的。":
            if daily_gift_count >= 1:
                sy"今日已赠送过礼物，明天再来吧～"
                jump after_gift
            else:
                if cookie_days > 0:

                    

                    "L拿来月已经吃掉的那几种口味的曲奇，将铁盒里的曲奇补满。他发现每次都是椰子味的和蔓越莓味的被剩下。"

                    L surprise"夜神君不喜欢这两种口味的吗？"

                    Y han"嗯……感觉有点太甜了。"

                    L order2"确实，黑巧和抹茶能很好地控制甜度呢。不介意的话，这两块可以分给我吃吗？"

                    Y fadai"……这倒是没关系。"

                    """ 只是，L这家伙不介意吃自己剩下的饼干吗？月在心底暗忖。 """

                    Y han"（啊……对了，这家伙之前在搜查总部也要过弥海砂的蛋糕吃，真是无可救药的甜食爱好者。）"

                    """ 看着侦探愉快地撕开包装纸，牙齿把饼干咬出清脆的响声，月突然觉得L正在吃的那块饼干看起来要比原来美味了。

                    下次……也许可以再尝试一下。 """
                    hide gift_cookie with dissolve
                    $ Light_cookie= True
                    $ cookie_days = 4
                    $ cookie_tixing = True
                    if unlock_the_handcuffs:
                        $ affection = min(affection + 1, 75)
                    else:
                        $ affection = min(affection + 1, 70)
                    $ daily_gift_count += 1 
                    jump after_gift
                else: 
                    L smile1"这家的曲奇饼干很好吃，想分享给夜神君，于是就带过来了。"

                    L"独立包装吃起来很方便呢，偶尔吃点零食心情也会变好吧。赏味期限是一周，请在期限内吃完。"

                    """ 月端详着约摸4寸大的精致铁盒，里面装了5枚形状各异的曲奇饼干，每一枚的口味都不一样。

                    黄色圆形的是咸黄油味，深褐色方形的是巧克力味，绿色叶子形的是抹茶味，白色圆形表面有一层椰蓉的是椰子味，长方形混着蔓越莓碎的是蔓越莓味。 """

                    Y smile2"龙崎真是有心了，谢谢你的曲奇，我会找时间品尝的。"

                    L"不客气。"
                    hide gift_cookie with dissolve

                    $ Light_cookie= True
                    $ cookie_days = 4
                    $ cookie_tixing = True
                    if unlock_the_handcuffs:
                        $ affection = min(affection + 1, 75)
                    else:
                        $ affection = min(affection + 1, 70)
                    $ daily_gift_count += 1 
                    jump after_gift

        "不了，我再想想吧。":
            
            sy"好的，返回行动界面。"
            jump after_gift

label gift_cake:
    hide screen gift_store
    hide screen Light_room
    if unlock_the_handcuffs:
        scene Light_room_4 with dissolve
    else:
        scene Light_room_3 with dissolve

    if Light_flower:
        show gift_flower_a
    if Light_cake:
        show gift_cake_a
    if Light_newspaper:
        show gift_newspaper_a
    if Light_light:
        show gift_light_a
    if Light_book:
        show gift_book_a
    if Light_mirror:
        show gift_mirror_a
    if Light_cookie:
        show gift_cookie_a
    if Light_photo:
        show gift_photo_a
    if Light_watch:
        show gift_watch_a
    if Light_brush:
        show gift_brush_a
    if affection < 50:
        "现在就算给夜神君送礼物也会被丢出来的吧，还是等关系变好一点再说吧。"
        jump after_gift

    if unlock_the_handcuffs == False:
        "现在手铐还没有解开，为了表示友好，还是先把对方的手铐解开吧。"
        jump after_gift
    show gift_cake at jubu with dissolve
    sy"""简介：经典的草莓奶油蛋糕，艳红的草莓点缀在甜美的奶油上，戚风蛋糕胚中间亦是满满的草莓果肉与奶油组成的夹心。
    
    草莓的酸味完美平衡了甜度，L总是在不经意间吃完一整个6寸蛋糕。"""
    menu:
        "要赠送这件礼物给夜神月吗？"
        "是的。":
            if daily_gift_count >= 1:
                sy"今日已赠送过礼物，明天再来吧～"
                jump after_gift
            else:
                
                L smile1"夜神君，我带来了下午茶的蛋糕。"

                Y"……在分辨不出时间，也没有茶水的情况下吃“下午茶蛋糕”吗，真是好兴致。"

                L thinking"说的也是呢，下次要不要把红茶也带过来呢。不过推着餐车好麻烦啊。"

                Y han"……真是败给你了。算了，留下来吧，我会在想吃的时候吃掉的。"

                L smile3"赏味期限是今天之内，所以请在睡前吃掉吧。"

                Y"知道了、知道了。"
                hide gift_cake with dissolve

                $ Light_cake= True
                if unlock_the_handcuffs:
                    $ affection = min(affection + 1, 75)
                else:
                    $ affection = min(affection + 1, 70)
                $ daily_gift_count += 1 
                jump after_gift

        "不了，我再想想吧。":
            
            sy"好的，返回行动界面。"
            jump after_gift


# 不可重复赠送的礼物

label unlock_handcuff:
    hide screen gift_store
    hide screen Light_room
    if unlock_the_handcuffs:
        scene Light_room_4 with dissolve
    else:
        scene Light_room_3 with dissolve    

    if Light_flower:
        show gift_flower_a
    if Light_cake:
        show gift_cake_a
    if Light_newspaper:
        show gift_newspaper_a
    if Light_light:
        show gift_light_a
    if Light_book:
        show gift_book_a
    if Light_mirror:
        show gift_mirror_a
    if Light_cookie:
        show gift_cookie_a
    if Light_photo:
        show gift_photo_a
    if Light_watch:
        show gift_watch_a
    if Light_brush:
        show gift_brush_a
    if affection < 60:
        "现在L还是不够信任夜神月，还是等关系变好一点再说吧。"
        jump after_gift
    "如果想要关系更进一步，解开镣铐是必须的吧。"
    menu:
        "是否解开月的镣铐？（注意，在主线剧情中解开镣铐后就无法再给月戴上。）"
        "是的。":
            if daily_gift_count >= 1:
                sy"今日已赠送过礼物，明天再来吧～"
                jump after_gift
            else:
                if unlock_the_handcuffs:
                    sy"您已经赠送过该礼物~请换一件其他的礼物吧！"
                    jump after_gift
                else:             
                    """ L早就注意到了月的腕间因为长期被拘束时产生的淤痕，现在也许是解开镣铐的时机了。

                    对于这么快给Kira解开镣铐是否不够妥当，L也经过了思考，但是思考的结果导向了对自身的信任——

                    在【L】的亲身监控下，【Kira】没有再次逃脱作恶的可能性。 """

                    L"从今天开始，夜神君不用再被束缚着了。"

                    """ L掏出钥匙插入了手铐的锁孔，轻轻转动后月的双手就恢复了自由。脚上的拘束带也被去除，从此月就可以在囚室里自由活动了。 """

                    Y fadai"……"

                    Y pt"……你是认真的吗，L？"

                    L"是的。我做下的决定不会反悔。"

                    """ 月看向L的眼神相当复杂，他一边活动着僵硬的手腕关节，一边思考L的用意。 """

                    Y han"（你究竟想从我身上得到什么呢，L？）"

                    Y"（总不能是真的喜欢我到不惜与日本政府为敌……吧。）"

                    Y pt"（如果我有这种魅力，能让硫克像雷姆对弥海砂那样为我写死L就好了。）"

                    Y"（虽然那样也会让游戏变得很无聊就是了。）"

                    $ affection = min(affection+10, 75)
                    $ stress = max(0 , stress - 20)

                    # 好感度上限提升到75
                    $ unlock_the_handcuffs = True
                    $ daily_gift_count += 1 
                    jump after_gift
        "不了，我再想想吧。":
            sy"好的，返回行动界面。"
            jump after_gift



label gift_watch:
    hide screen gift_store
    hide screen Light_room
    if unlock_the_handcuffs:
        scene Light_room_4 with dissolve
    else:
        scene Light_room_3 with dissolve
  
    if Light_flower:
        show gift_flower_a
    if Light_cake:
        show gift_cake_a
    if Light_newspaper:
        show gift_newspaper_a
    if Light_light:
        show gift_light_a
    if Light_book:
        show gift_book_a
    if Light_mirror:
        show gift_mirror_a
    if Light_cookie:
        show gift_cookie_a
    if Light_photo:
        show gift_photo_a
    if Light_watch:
        show gift_watch_a
    if Light_brush:
        show gift_brush_a
    if affection < 60:
        "现在就算给夜神君送礼物也会被丢出来的吧，还是等关系变好一点再说吧。"
        jump after_gift

    if unlock_the_handcuffs == False:
        "现在手铐还没有解开，为了表示友好，还是先把对方的手铐解开吧。"
        jump after_gift
    show gift_watch at jubu with dissolve
    sy"简介：这是属于月的手表，他父亲赠送他的成人生日礼物，对他而言有着特殊的意义。当然，那些小机关已经被L拆除了。"
    menu:
        "要赠送这件礼物给夜神月吗？"
        "是的。":
            if daily_gift_count >= 1:
                sy"今日已赠送过礼物，明天再来吧～"
                jump after_gift
            else:
                if Light_watch:
                    sy"您已经赠送过该礼物~请换一件其他的礼物吧！"
                    jump after_gift
                else:             
                    
                    L order2"听说这是夜神局长送给夜神君的生日礼物呢。"
                    L smile1"希望夜神君能喜欢。"
                    """ L递给青年他过去常用的手表，月接过去翻看了几下，轻轻拨弄着表盘侧边的按钮——但是很可惜，什么也没有发生。 """
                    L smile3"请安心，夜神君，现在它只是一块普通的手表罢了。"
                    Y smile2"看来同一个招数并不能两次都见效呢。"
                    Y"手表确实是对我而言很重要的东西，谢谢你的礼物。"
                    hide gift_watch with dissolve
                    if unlock_the_handcuffs:
                        $ affection = min(affection + 5, 75)
                    else:
                        $ affection = min(affection + 5, 70)
                    $ Light_watch = True
                    $ daily_gift_count += 1 
                    jump after_gift
        "不了，我再想想吧。":
            
            sy"好的，返回行动界面。"
            jump after_gift

label gift_photo:
    hide screen gift_store
    hide screen Light_room
    if unlock_the_handcuffs:
        scene Light_room_4 with dissolve
    else:
        scene Light_room_3 with dissolve

    if Light_flower:
        show gift_flower_a
    if Light_cake:
        show gift_cake_a
    if Light_newspaper:
        show gift_newspaper_a
    if Light_light:
        show gift_light_a
    if Light_book:
        show gift_book_a
    if Light_mirror:
        show gift_mirror_a
    if Light_cookie:
        show gift_cookie_a
    if Light_photo:
        show gift_photo_a
    if Light_watch:
        show gift_watch_a
    if Light_brush:
        show gift_brush_a
    if affection < 60:
        "现在就算给夜神君送礼物也会被丢出来的吧，还是等关系变好一点再说吧。"
        jump after_gift

    if unlock_the_handcuffs == False:
        "现在手铐还没有解开，为了表示友好，还是先把对方的手铐解开吧。"
        jump after_gift
    show gift_photo at jubu with dissolve
    sy"简介：木质的可立相框里简易地装着一张相片，上面印着夜神家庆祝月考上大学后在校门前的合影，一家人打扮整齐，在相机面前笑得很开心的样子。"
    menu:
        "要赠送这件礼物给夜神月吗？"
        "是的。":
            if daily_gift_count >= 1:
                sy"今日已赠送过礼物，明天再来吧～"
                jump after_gift
            else:
                if Light_photo:
                    sy"您已经赠送过该礼物~请换一件其他的礼物吧！"
                    jump after_gift
                else:             
                    
                    L smile3"夜神君，虽然现在不能让你外出，但这点程度的话还是可以的。"
                    """ L将相框递给月，相片隔着一层薄薄的亚克力板陈列其中，月用指腹轻轻抚摸着照片，良久没有说话。 """
                    L"我和夜神君说过，他还会有再见到家人的一天的。"
                    L"所以……请打起精神来吧。"
                    """ 月抬头平静地看着L，侦探难得地从那双琥珀色的眼睛里读不出情绪。 """
                    Y"嗯，我知道了。谢谢你，龙崎。"
                    hide gift_photo with dissolve
                    if unlock_the_handcuffs:
                        $ affection = min(affection + 5, 75)
                    else:
                        $ affection = min(affection + 5, 70)
                    $ Light_photo = True
                    $ daily_gift_count += 1 
                    jump after_gift
        "不了，我再想想吧。":
            
            sy"好的，返回行动界面。"
            jump after_gift

label gift_mirror:
    hide screen gift_store
    hide screen Light_room
    if unlock_the_handcuffs:
        scene Light_room_4 with dissolve
    else:
        scene Light_room_3 with dissolve

    if Light_flower:
        show gift_flower_a
    if Light_cake:
        show gift_cake_a
    if Light_newspaper:
        show gift_newspaper_a
    if Light_light:
        show gift_light_a
    if Light_book:
        show gift_book_a
    if Light_mirror:
        show gift_mirror_a
    if Light_cookie:
        show gift_cookie_a
    if Light_photo:
        show gift_photo_a
    if Light_watch:
        show gift_watch_a
    if Light_brush:
        show gift_brush_a
    if affection < 60:
        "现在就算给夜神君送礼物也会被丢出来的吧，还是等关系变好一点再说吧。"
        jump after_gift

    if unlock_the_handcuffs == False:
        "现在手铐还没有解开，为了表示友好，还是先把对方的手铐解开吧。"
        jump after_gift
    show gift_mirror at jubu with dissolve
    sy"简介：一枚随处可见的便携化妆镜，可以通过它随时随地地检查自己的仪表，因为小巧所以方便携带、是非常便利的设计。"
    menu:
        "要赠送这件礼物给夜神月吗？"
        "是的。":
            if daily_gift_count >= 1:
                sy"今日已赠送过礼物，明天再来吧～"
                jump after_gift
            else:
                if Light_mirror:
                    sy"您已经赠送过该礼物~请换一件其他的礼物吧！"
                    jump after_gift
                else:             
                    
                    """ L从牛仔裤的侧兜里掏出一枚可折叠的化妆镜，是车站前药妆店里常见的普通款式，只需要将盖子打开就可以很方便地检查自己的状态。 """
                    L smile2"总感觉夜神君会需要这个呢，请试试看吧。"
                    """ L打开小镜子、捏住镜脚端详了一会，随后简单用衣摆擦拭掉了镜面上的指纹，将镜子递给了月。 """
                    Y smile2"真是稀奇的礼物呢，龙崎怎么会想到送这个给我？"
                    """ 月打开后对着镜子简单整理了一下自己的刘海，头发相比于他习惯的长度而言已经长得太长……或许找机会修剪一下会更好吧，月捻着发尾想道。 """
                    Y"不过还算实用，所以谢谢了。"
                    hide gift_mirror with dissolve
                    if unlock_the_handcuffs:
                        $ affection = min(affection + 2, 75)
                    else:
                        $ affection = min(affection + 2, 70)
                    $ Light_mirror = True
                    $ daily_gift_count += 1 
                    jump after_gift
        "不了，我再想想吧。":
            
            sy"好的，返回行动界面。"
            jump after_gift

label gift_brush:
    hide screen gift_store
    hide screen Light_room
    if unlock_the_handcuffs:
        scene Light_room_4 with dissolve
    else:
        scene Light_room_3 with dissolve

    if Light_flower:
        show gift_flower_a
    if Light_cake:
        show gift_cake_a
    if Light_newspaper:
        show gift_newspaper_a
    if Light_light:
        show gift_light_a
    if Light_book:
        show gift_book_a
    if Light_mirror:
        show gift_mirror_a
    if Light_cookie:
        show gift_cookie_a
    if Light_photo:
        show gift_photo_a
    if Light_watch:
        show gift_watch_a
    if Light_brush:
        show gift_brush_a
    if affection < 60:
        "现在就算给夜神君送礼物也会被丢出来的吧，还是等关系变好一点再说吧。"
        jump after_gift

    if unlock_the_handcuffs == False:
        "现在手铐还没有解开，为了表示友好，还是先把对方的手铐解开吧。"
        jump after_gift
    show gift_brush at jubu with dissolve
    sy"简介：由檀木制成的木梳，木质细腻温润，凑近可以闻到淡淡的檀香，有着吉祥的寓意、非常适合用于赠礼。"
    menu:
        "要赠送这件礼物给夜神月吗？"
        "是的。":
            if daily_gift_count >= 1:
                sy"今日已赠送过礼物，明天再来吧～"
                jump after_gift
            else:
                if Light_brush:
                    sy"您已经赠送过该礼物~请换一件其他的礼物吧！"
                    jump after_gift
                else:             
                    """ L带着一个长条形的礼物盒走进了囚室，盒子只有手掌大小，打开后便能看见一把木梳静静地躺在里面。 """
                    Y fadai"这是……梳子？"
                    L smile3"是的，之前在搜查总部的时候经常看到夜神君整理自己的头发，所以我想他可能需要这个。"
                    """ L取出木梳，将梳齿切入月的发丝间，从上至下地梳理了几下青年有些杂乱的褐色头发。 """
                    Y surprise"喂……！龙崎！你怎么又不经得我同意就！"
                    L smile2"很快就好了，夜神君。"
                    L"你看，已经变得顺滑很多了吧。"
                    """ L的手指畅通无阻地从发顶滑到了发尾，手指搔挠着月的头皮让他觉得有些发痒，但过程的确如L所言十分顺利，原先有些打结的头发现在被全部梳开，月久违地感受到了一丝清爽。 """
                    Y han"龙崎偶尔也会送这样实用的礼物呢。"
                    Y smile2"……谢谢，那么我就收下了。"

                    if unlock_the_handcuffs:
                        $ affection = min(affection + 2, 75)
                    else:
                        $ affection = min(affection + 2, 70)
                    $ Light_brush = True
                    $ daily_gift_count += 1 
                    hide gift_brush with dissolve
                    jump after_gift
        "不了，我再想想吧。":
            
            sy"好的，返回行动界面。"
            jump after_gift

label gift_light:
    hide screen gift_store
    hide screen Light_room
    if unlock_the_handcuffs:
        scene Light_room_4 with dissolve
    else:
        scene Light_room_3 with dissolve

    if Light_flower:
        show gift_flower_a
    if Light_cake:
        show gift_cake_a
    if Light_newspaper:
        show gift_newspaper_a
    if Light_light:
        show gift_light_a
    if Light_book:
        show gift_book_a
    if Light_mirror:
        show gift_mirror_a
    if Light_cookie:
        show gift_cookie_a
    if Light_photo:
        show gift_photo_a
    if Light_watch:
        show gift_watch_a
    if Light_brush:
        show gift_brush_a
    if affection < 60:
        "现在就算给夜神君送礼物也会被丢出来的吧，还是等关系变好一点再说吧。"
        jump after_gift

    if unlock_the_handcuffs == False:
        "现在手铐还没有解开，为了表示友好，还是先把对方的手铐解开吧。"
        jump after_gift
    show gift_light at jubu with dissolve
    sy"简介：通体白色的书桌用台灯，插电或充电使用，电池支持长时间读写，也可以调节亮度适用于夜间阅读。"
    menu:
        "要赠送这件礼物给夜神月吗？"
        "是的。":
            if daily_gift_count >= 1:
                sy"今日已赠送过礼物，明天再来吧～"
                jump after_gift
            else:
                if Light_light:
                    sy"您已经赠送过该礼物~请换一件其他的礼物吧！"
                    jump after_gift
                else:             
                    
                    """ L将台灯放到了囚室的简易书桌上，他摁下台灯底座上的感应按钮，左右滑动向月展示着如何调控灯光的明暗。 """
                    L smile3"虽然囚室的熄灯时间是固定的，但如果夜神君偶尔想熬夜的话，我想他应该用得上台灯。"
                    L thinking"因为囚室里没有安装更多电线，所以我会定期替台灯充好电带过来。夜神君如果发现台灯电量不足的话也请告诉我。"
                    """ 月跟着L的动作试了两下感应按钮，台灯便随他动作变换着明暗，台灯虽不如白炽灯明亮，但在黑暗里也足够照出令人安心的一隅光明。 """
                    Y smile2"谢谢，我会好好利用它的。"
                    L smile3"不用谢，夜神君能喜欢就好。"
                    hide gift_light with dissolve
                    $ Light_light = True
                    $ daily_gift_count += 1 
                    if unlock_the_handcuffs:
                        $ affection = min(affection + 3, 75)
                    else:
                        $ affection = min(affection + 3, 70)
                    jump after_gift
        "不了，我再想想吧。":
            
            sy"好的，返回行动界面。"
            jump after_gift


label gift_sexbang:
    hide screen gift_store
    hide screen Light_room
    if unlock_the_handcuffs:
        scene Light_room_4 with dissolve
    else:
        scene Light_room_3 with dissolve
        
    if Light_flower:
        show gift_flower_a
    if Light_cake:
        show gift_cake_a
    if Light_newspaper:
        show gift_newspaper_a
    if Light_light:
        show gift_light_a
    if Light_book:
        show gift_book_a
    if Light_mirror:
        show gift_mirror_a
    if Light_cookie:
        show gift_cookie_a
    if Light_photo:
        show gift_photo_a
    if Light_watch:
        show gift_watch_a
    if Light_brush:
        show gift_brush_a
    show gift_sexbang at jubu with dissolve
    sy"简介：纯银打造的尿道棒，顶端做成了十字架的造型，光从外表看完全就是一件艺术品。总长12cm，顶端处粗5mm，尾部尖端处粗2mm。"
    menu:
        "要赠送这件礼物给夜神月吗？"
        "是的。":
            if daily_gift_count >= 1:
                sy"今日已赠送过礼物，明天再来吧～"
                jump after_gift
            else:
                if Light_sexbang:
                    sy"您已经赠送过该礼物~请换一件其他的礼物吧！"
                    jump after_gift
                else:             
                    L thinking"（之后也许可以给夜神君用上，先收好吧。）"
                    $ Light_sexbang = True
                    $ daily_gift_count += 1 
                    jump after_gift
        "不了，我再想想吧。":
            sy"好的，返回行动界面。"
            jump after_gift

label give_gift_1:
    sy"您已经赠送过该礼物~请换一件其他的礼物吧！"
    jump after_gift


# 添加淡入淡出效果
transform fade_in_out:
    alpha 0.0
    linear 0.3 alpha 1.0  # 淡入
    pause 2.4            # 保持显示
    linear 0.3 alpha 0.0  # 淡出

label after_gift:
    hide gift_book with dissolve
    hide gift_flower with dissolve
    hide gift_newspaper with dissolve
    hide gift_cookie with dissolve
    hide gift_cake with dissolve
    hide gift_watch with dissolve
    hide gift_photo with dissolve
    hide gift_mirror with dissolve
    hide gift_brush with dissolve
    hide gift_light with dissolve
    hide gift_sexbang with dissolve
    sy"送礼结束，送礼不扣除行动点，回到行动界面。"
    if unlock_the_handcuffs:
        if affection >= 60:
            scene main bg_4 with dissolve
            $ persistent.unlock_3 = True
        else:
            scene main bg_3 with dissolve
            $ persistent.unlock_2 = True
    else:  
        if affection >= 60:
            scene main bg_2 with dissolve
            $ persistent.unlock_1 = True
        else:
            scene main bg_1 with dissolve
    
    # 检查行动点数是否归零
    if action_points <= 0:
        call next_day from _call_next_day_8
    else:
        jump action_menu