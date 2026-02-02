image main_menu:
    "gui/overlay/main_menu.png"

image main bg_1:
    "images/dialog/main bg_1.png"

image main bg_2:
    "images/dialog/main bg_2.png"

image main bg_3:
    "images/dialog/main bg_3.png"

image main bg_4:
    "images/dialog/main bg_4.png"

image lock:
    "images/gallery/lock.png"

init python:
    # 步骤1：创建一个画廊对象（Gallery类的实例）
    # 这个对象相当于一个"相册管理员"，负责管理所有画廊的按钮、图片、解锁状态
    g = Gallery()

    # 步骤2：向画廊中添加按钮和图片（按钮相当于"相册分类"，每个按钮关联一组图片）

    # 1. 第一个按钮："title"（标题类图片）
    g.button("主界面图")  # 创建名为"title"的按钮（分类）

    g.image("main_menu")   # 给"title"按钮关联名为"title"的图片（需提前定义该图片）
    g.image("main bg_1")   # 关联名为"dawn1"的图片
    g.unlock("main bg_1")  # 强制解锁"dawn1"图片（玩家一开始就能看）
    g.image("main bg_2")  # 关联并解锁"bigbeach1"图片
    g.condition("persistent.unlock_1")    
    g.image("main bg_3")  # 关联并解锁"bigbeach1"图片
    g.condition("persistent.unlock_2")    
    g.image("main bg_4")  # 关联并解锁"bigbeach1"图片
    g.condition("persistent.unlock_3")    
    g.image("true_end_title")  
    g.condition("persistent.true_end_title")

    g.button("未解锁")  
    g.image("lock")   

    # 1. 创建“日常行动-喂食、清洁”按钮
    g.button("日常行动-喂食、清洁")  

    g.image("feed_1")  
    g.condition("persistent.unlock_feed_1")  
    g.image("feed_2")  
    g.condition("persistent.unlock_feed_2")

    g.image("bath_1")  
    g.condition("persistent.unlock_bath_1")
    g.image("bath_2")  
    g.condition("persistent.unlock_bath_2")
    g.image("bath_3")  
    g.condition("persistent.unlock_bath_3")
    g.image("bath_4")  
    g.condition("persistent.unlock_bath_4")



    g.button("日常行动-娱乐")   

    g.image("book_jie")  
    g.condition("persistent.unlock_book_jie")  
    g.image("book_jie1")  
    g.condition("persistent.unlock_book_jie1")
    g.image("book_jie2")  
    g.condition("persistent.unlock_book_jie2")
    g.image("book_jie3")  
    g.condition("persistent.unlock_book_jie3")
    g.image("book_nian")  
    g.condition("persistent.unlock_book_nian")
    g.image("book_nian1")  
    g.condition("persistent.unlock_book_nian1")
    g.image("book_nian2")  
    g.condition("persistent.unlock_book_nian2")
    g.image("book_nian3")  
    g.condition("persistent.unlock_book_nian3")
    g.image("book_nian4")  
    g.condition("persistent.unlock_book_nian4")
    g.image("book_zuo")  
    g.condition("persistent.unlock_book_zuo")
    g.image("book_zuo1")  
    g.condition("persistent.unlock_book_zuo1")
    g.image("book_zuo2")  
    g.condition("persistent.unlock_book_zuo2")
    g.image("book_zuo3")  
    g.condition("persistent.unlock_book_zuo3")

    g.image("chess")  
    g.condition("persistent.unlock_chess")
    g.image("chess_L")
    g.condition("persistent.unlock_chess_LY") 
    g.image("chess_y")
    g.condition("persistent.unlock_chess_LY") 
    g.image("chess_draw")  
    g.condition("persistent.unlock_chess_draw")
    g.image("chess_L_win")  
    g.condition("persistent.unlock_chess_Lwin")
    g.image("chess_y_win")  
    g.condition("persistent.unlock_chess_Ywin")

    g.image("blackjack_1")  
    g.condition("persistent.unlock_blackjack")    
    g.image("blackjack_L_win")  
    g.condition("persistent.unlock_blackjack_Lwin")
    g.image("blackjack_y_win")  
    g.condition("persistent.unlock_blackjack_Ywin")



    g.button("粉红行动-做爱")

    g.image("sex_1a")
    g.condition("persistent.unlock_sex_1")  
    g.image("sex_1b")
    g.condition("persistent.unlock_sex_1")  


    g.image("sex_2a")
    g.condition("persistent.unlock_sex_2") 
    g.image("sex_2b")
    g.condition("persistent.unlock_sex_2") 
    
    g.image("sex_kiss1")
    g.condition("persistent.unlock_sex_kiss1")

    g.image("sex_3a1")
    g.condition("persistent.unlock_sex_3a")  
    g.image("sex_3b1")
    g.condition("persistent.unlock_sex_3a") 
    g.image("sex_3a2")
    g.condition("persistent.unlock_sex_3b")  
    g.image("sex_3b2")
    g.condition("persistent.unlock_sex_3b") 
    g.image("sex_3c")
    g.condition("persistent.unlock_sex_3c") 

    g.image("sex_4a1")
    g.condition("persistent.unlock_sex_4")  
    g.image("sex_4a2")
    g.condition("persistent.unlock_sex_4")
    g.image("sex_4a3")
    g.condition("persistent.unlock_sex_4")
    g.image("sex_4b1")
    g.condition("persistent.unlock_sex_4")  
    g.image("sex_4b2")
    g.condition("persistent.unlock_sex_4")
    g.image("sex_4b3")
    g.condition("persistent.unlock_sex_4")

    g.image("sex_5a_y0")
    g.condition("persistent.unlock_sex_5_sexbang")  
    g.image("sex_5a_y1")
    g.condition("persistent.unlock_sex_5_sexbang")  
    g.image("sex_5a_y2")
    g.condition("persistent.unlock_sex_5_sexbang")
    g.image("sex_5a_y3")
    g.condition("persistent.unlock_sex_5_sexbang")
    g.image("sex_5b_y1")
    g.condition("persistent.unlock_sex_5_sexbang")    
    g.image("sex_5b_y2")
    g.condition("persistent.unlock_sex_5_sexbang")

    g.image("sex_5a_w1")
    g.condition("persistent.unlock_sex_5")  
    g.image("sex_5a_w2")
    g.condition("persistent.unlock_sex_5")
    g.image("sex_5b_w1")
    g.condition("persistent.unlock_sex_5")  
    g.image("sex_5b_w2")
    g.condition("persistent.unlock_sex_5")


    g.button("结局")

    g.image("ne_b1")
    g.condition("persistent.unlock_normal_end")  
    g.image("ne_b2")
    g.condition("persistent.unlock_normal_end")  

    g.image("he_b1")
    g.condition("persistent.unlock_happy_end")  
    g.image("he_b4")
    g.condition("persistent.unlock_happy_end")  
    g.image("he_b2_1")
    g.condition("persistent.unlock_happy_end")  
    g.image("he_b2_2")
    g.condition("persistent.unlock_happy_end")  
    g.image("he_b3")
    g.condition("persistent.unlock_happy_end") 
   

    g.image("be_b1_1")
    g.condition("persistent.unlock_bad_end")  
    g.image("be_b1_2")
    g.condition("persistent.unlock_bad_end")  
    g.image("be_b2_1")
    g.condition("persistent.unlock_bad_end")  
    g.image("be_b2_2")
    g.condition("persistent.unlock_bad_end")  
    g.image("be_b3_1")
    g.condition("persistent.unlock_bad_end")  
    g.image("be_b3_2")
    g.condition("persistent.unlock_bad_end")  
    g.image("be_b4")
    g.condition("persistent.unlock_bad_end")  
    g.image("be_b5")
    g.condition("persistent.unlock_bad_end")  


    g.image("te_b1_1")
    g.condition("persistent.unlock_true_end")  
    g.image("te_b1_2")
    g.condition("persistent.unlock_true_end")  
    g.image("te_b1_3")
    g.condition("persistent.unlock_true_end")  
    g.image("te_b2_1")
    g.condition("persistent.unlock_true_end")  
    g.image("te_b2_2")
    g.condition("persistent.unlock_true_end")  
    g.image("te_b3_1")
    g.condition("persistent.unlock_true_end")  
    g.image("te_b3_2")
    g.condition("persistent.unlock_true_end")  
    g.image("te_b4")
    g.condition("persistent.unlock_true_end")  

    g.image("dead_end")
    g.condition("persistent.unlock_dead_end") 


    g.button("日常行动-外出")
 
    g.image("date_1b")
    g.condition("persistent.unlock_date_1")  
    g.image("date_2b")
    g.condition("persistent.unlock_date_2")  
    g.image("date_3")
    g.condition("persistent.unlock_date_3")  
    g.image("date_4b1")
    g.condition("persistent.unlock_date_4")  
    g.image("date_4b2")
    g.condition("persistent.unlock_date_4")  
    g.image("date_4b3")
    g.condition("persistent.unlock_date_4")  

    # 设置图片切换时的动画效果（转场）：用"dissolve"（溶解效果）切换图片
    g.transition = dissolve





image gal bg:
    "images/gallery/game_menu.png"

image gal-main menu:
    "images/gallery/gal-main menu.png"

image gal-lock:
    "images/gallery/gal-lock.png"


image gal-main bg:
    "images/gallery/gal-main bg.png"

image gal-feed:
    "images/gallery/gal-feed.png"

image gal-sex1:
    "images/gallery/gal-sex1.png"

image gal-sex2:
    "images/gallery/gal-sex2.png"

image gal-end:
    "images/gallery/gal-end.png"

image gal-pastime:
    "images/gallery/gal-pastime.png"



# 步骤3：定义画廊的显示界面（玩家看到的画廊页面）
screen gallery:

    # 标记当前界面为"menu"类型，确保打开画廊时替换主菜单（避免多层界面叠加）
    tag menu

    # 画廊背景：显示名为"beach2"的图片作为背景（需提前定义该图片）
    add "gal bg"

    # 按钮布局：用2行3列的网格（grid）排列所有画廊按钮（共9个按钮，正好3x3）
    grid 3 2:  # 3列2行（第一个数字是列数，第二个是行数）
        xfill False  # 关闭宽度自适应（按钮不拉伸）
        yfill False  # 关闭高度自适应（按钮不拉伸）
        xspacing 40  # 按钮之间的水平间距（数值越大，左右间距越宽）
        yspacing 60  # 按钮之间的垂直间距（数值越大，上下间距越宽）
        ypos 130
        xpos 80

        # 循环创建按钮：调用g.make_button生成每个按钮的显示样式
        # 格式：g.make_button(按钮名, 按钮图片, 对齐方式)
        # 1. 第一个按钮 + 文字（主封面图）
        vbox:  # 垂直布局：按钮在上，文字在下
            align (0.5, 0.5)  # 整体居中
            add g.make_button("主界面图", "gal-main menu", xalign=0.5, yalign=0.5)  # 按钮
            text _("主界面图") size 24 color "#ffffff" ypos 10  # 文字（ypos 10 是按钮和文字的间距）

        # 3. 第三个按钮 + 文字（喂食）
        vbox:
            align (0.5, 0.5)
            if persistent.unlock_feed_1 or persistent.unlock_feed_2 or persistent.unlock_bath_1 or persistent.unlock_bath_2 or persistent.unlock_bath_3 or persistent.unlock_bath_4:
                add g.make_button("日常行动-喂食、清洁", "gal-feed", xalign=0.5, yalign=0.5)
            else:
                add g.make_button("未解锁", "gal-lock", xalign=0.5, yalign=0.5)
            text _("日常行动-喂食、清洁") size 24 color "#ffffff" ypos 10
        
        vbox:
            align (0.5, 0.5)
            if persistent.unlock_book_jie or persistent.unlock_book_nian or persistent.unlock_book_zuo or persistent.unlock_chess or persistent.unlock_blackjack:
                add g.make_button("日常行动-娱乐", "gal-pastime", xalign=0.5, yalign=0.5)
            else:
                add g.make_button("未解锁", "gal-lock", xalign=0.5, yalign=0.5)
            text _("日常行动-娱乐") size 24 color "#ffffff" ypos 10

        vbox:
            align (0.5, 0.5)
            if persistent.unlock_date_1 == False:
                add g.make_button("未解锁", "gal-lock", xalign=0.5, yalign=0.5)
            else:
                add g.make_button("日常行动-外出", "gal-date", xalign=0.5, yalign=0.5)
            text _("日常行动-外出") size 24 color "#ffffff" ypos 10

        vbox:
            align (0.5, 0.5)
            if persistent.unlock_sex_1 == False:
                add g.make_button("未解锁", "gal-lock", xalign=0.5, yalign=0.5)
            else:
                add g.make_button("粉红行动-做爱", "gal-sex1", xalign=0.5, yalign=0.5)
            text _("粉红行动-做爱") size 24 color "#ffffff" ypos 10

        vbox:
            align (0.5, 0.5)
            if persistent.unlock_dead_end or persistent.unlock_bad_end or persistent.unlock_happy_end or persistent.unlock_normal_end or persistent.unlock_true_end:
                add g.make_button("结局", "gal-end", xalign=0.5, yalign=0.5)
            else:
                add g.make_button("未解锁", "gal-lock", xalign=0.5, yalign=0.5)
            text _("结局") size 24 color "#ffffff" ypos 10




    # 返回按钮：点击后回到主菜单
    textbutton _("返回") action Return() xalign 0.5 yalign 0.95  # xalign/yalign控制按钮在屏幕底部居中 
        # 定义页码名称对象：用于显示“第X页”“自动存档”等页码文本

