label daily_none:

    scene L_sofa with dissolve

    "L吃着甜品，翻看着案件资料，度过了平淡的几个小时。"

    # 消耗1点行动点数
    $ action_points -= 1
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
        call next_day from _call_next_day_2
    else:
        sy"你还剩下 [action_points] 点行动点数。"
        jump action_menu

label daily_zuobi:
    menu:
        "要一键满状态吗？"
        "加好感减压力":
            $ affection = 65
            $ stress = 0
            $ health = 100
            $ stamina = 100
            "已完成。"
            jump action_menu
        "加饱腹度和清洁值":
            $ satiety = 100
            $ clean = 100
            "已完成。"
            jump action_menu
        "满状态跳过一天":
            $ affection = 65
            $ stress = 0
            $ health = 100
            $ stamina = 100
            $ satiety = 100
            $ clean = 100
            call next_day from _call_next_day_10
        "跳过一天":
            call next_day from _call_next_day_11
