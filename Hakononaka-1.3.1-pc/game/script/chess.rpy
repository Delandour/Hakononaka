# 示例：下棋游戏标签
label play_chess:
    
    if chess_play_count == 1:
        """ L拿着一盒国际象棋走进了囚室，月明显注意到了，他的目光在棋盒上黏了几秒，然后又转回L。"""
        if affection >= 60:

            """ 月的目光带着期待。 """

            Y"终于有些有趣的东西了吗？这里的生活确实太无聊了。"

            """ L点头回应。 """

        else:

            """ 月的目光充满嘲讽之意。 """

            Y"大侦探也会关心囚犯的心理健康吗？"

            """ L无视了这句话。 """
        L order2"我确实注意到了夜神君最近的压力指数有些高，下棋是很好的放松方式，和我对弈也许可以缓解你的无聊。"
        if unlock_the_handcuffs == False:
            Y"听上去不错，但是我现在这样要怎么下棋？"

            L"每次下棋的时候我会解开你的镣铐，如果夜神君试图袭击我或者逃走，这项活动会被永久取消。"

            Y"我知道我无处可去，不用废话了。"

            """ L取出钥匙，解开了月的手铐和脚铐。月活动着手腕和脚腕，他真是受够被铐住的日子了。

            然后L打开棋盒，棋盒展开之后自然就是一副棋盘，棋子整齐地码放其中。 """

        L pt"我执黑棋吧。"

        Y smile2"你还真是好心，知道让让我。"

        """ 夜神月哼笑了一声。 
        
        他们把囚室里唯一的一套桌椅搬到床对面，L抛弃了一看就很硬的椅子，蹲到了月的床上，月只能在椅子上落座。
        
        """
    else:
        if stress > 70:
            Y "我今天不想下棋。没心情。"
            "L看见月烦躁的脸色，知道现在勉强他也没用，只能拿着棋盒离开了囚室。"
            $ pastime_points -= 1
            $ Y_room = True
            show screen stats with dissolve
            jump action_menu
            
        "这是你们第[chess_play_count]次下棋。"
        L smile2"夜神君似乎很期待和我下棋的游戏呢。"
        Y "那是因为只有在这个时候，我才有机会打败你。"
        L unhappy"真是可怕的胜负欲。"
        Y "别说得你自己不想赢一样。"
        Y "别废话了，开始吧。"


    
    # 调用国际象棋对战系统
    call start_chess_battle from _call_start_chess_battle
    $ persistent.unlock_chess_LY = True #下棋cg
    # 根据对战结果添加不同反应
    if abs(total_score) < 0.8:  # 平局
        "平局！两人对这个结果都不太服气，不过同样，他们又认可对方的实力，觉得勉强可以接受。"
        Y"势均力敌……下次我一定会赢。"
        L smile1"那就让我期待下一局的结果吧。"
        $ persistent.unlock_chess_draw = True
        $ stress = max(0, stress-8)
    elif total_score > 0:  # L胜
        if total_score > 2.5:
            "L完胜！L看起来游刃有余。"
            L smile1"夜神君已经累了吗？"
        else:
            "L险胜！月看起来不是很高兴。"        
        Y"……"
        "月盯着棋盘，似乎在分析自己哪里出错了。"
        #voice "voice/light/Y_I lose.mp3"
        Y "哼……今天不过是你运气好而已。"
        L "夜神君，有时候坦然地面对自己的失败比较好哦。"
        Y angry"……"
        L order2"（哇，好可怕的眼神。）"
        $ persistent.unlock_chess_Lwin = True
        $ stress = max(0, stress-5)
    else:  # 月胜
        if total_score < -2.5:
            "月完胜！月露出有些得意的笑容。"
            Y deyi"L，你只有这点水平吗？"
        else:
            "月险胜！L蜷缩在床上，眼中充满兴味。"
            L smile3"不愧是夜神君。"
        Y deyi"怎么了，今天状态不好吗？"
        "L撇嘴，不理会月假惺惺的安慰。"
        L unhappy"只是输了一次而已，下一局我会认真的。"
        $ persistent.unlock_chess_Ywin = True
        if unlock_the_handcuffs:
            $ affection = min(affection + 3, 75)
        else:
            $ affection = min(affection + 3, 70)
        $ stress = max(0, stress-10)
    
    call screen chess_stats

    jump daily_pastime_end



init python:
    # 1. 初始化当前语言变量（默认中文"None"，对应RenPy默认语言）
    # 注意：RenPy中默认语言（无翻译时）无需额外标识，故用"None"代表中文
    current_language = "None"  # 可选值："None"（中文）、"english"（英文）、"japanese"（日文）

    # 2. 定义语言切换函数（更新当前语言并刷新界面）
    def set_language(lang):
        global current_language
        current_language = lang
        # 通知RenPy切换翻译语言（"None"时使用默认中文，无需加载翻译文件）
        if lang == "english":
            renpy.change_language("english")
        elif lang == "japanese":
            renpy.change_language("japanese")
        elif lang == "None":  # "None"（中文）
            renpy.change_language(None)  # 重置为默认语言（中文）
        # 刷新当前界面（确保文本实时更新）
        renpy.restart_interaction()


    # 2. 核心映射表：英文标识 → 多语言显示文本（关键！）
    phase_display = {  # 阶段映射
        "opening": _("开局"),
        "middlegame": _("中局"),
        "endgame": _("终局")
    }
    style_display = {  # 战术风格映射
        "offense": _("进攻"),
        "defense": _("防守"),
        "unconventional": _("异想天开"),
        "aggressive": _("激进")
    }

    # ===== 战术数据库 =====
    tactics_db = {
        "opening": {  # 英文标识：开局
            "offense": [  # 英文标识：进攻
                {"名称": _("意大利开局"), "a":6, "b":3, "c":4, "文案": _("这种开局使用古典直接的中心控制，象瞄准f7弱点，随时准备攻陷敌方防线。")},
                {"名称": _("苏格兰开局"), "a":7, "b":2, "c":3, "文案": _("这种开局进行激进的中心争夺，在早期挑起激烈战斗，势如破竹。")},
                {"名称": _("维也纳开局"), "a":5, "b":4, "c":4, "文案": _("这种开局的特点是拥有灵活的转换结构，可转向攻守两种模式。")} 
            ],
            "defense": [  # 英文标识：防守
                {"名称": _("卡罗康防御"), "a":3, "b":7, "c":2, "文案": _("稳固的兵链结构，大军压境，缓慢推进反击。")},
                {"名称": _("斯拉夫防御"), "a":4, "b":6, "c":3, "文案": _("坚实的中心支撑，兵力集结，避免早期弱点。")},
                {"名称": _("剑桥泉防御"), "a":2, "b":8, "c":3, "文案": _("超稳固的龟缩阵型，考验对手的耐心。")}
            ],
            "unconventional": [  # 英文标识：异想天开
                {"名称": _("阿廖欣防御"), "a":4, "b":3, "c":8, "文案": _("L执起黑马跳入f6，引诱对手推进中心兵。他紧盯着月，看对方会如何回应挑衅。")},
                {"名称": _("格伦菲尔德防御"), "a":5, "b":4, "c":6, "文案": _("L放任白方占据中心，看似空门打开，实则预谋着在侧翼进行反击。")},
                {"名称": _("欧文防御"), "a":3, "b":5, "c":7, "文案": _("L执起象提前到b4，进行非常规牵制。月盯着棋盘陷入思考。")}
            ]
        },
        "middlegame": {  # 英文标识：中局
            "offense": [
                {"名称": _("王翼冲锋"), "a":7, "b":4, "c":3, "文案": _("h兵推进打开敌方阵地，试图在千军万马中直取敌王项上人头。")},
                {"名称": _("中心突破"), "a":6, "b":5, "c":2, "文案": _("d兵e兵强力推进粉碎防线，攻势凶猛。")},
                {"名称": _("双车入侵"), "a":5, "b":6, "c":4, "文案": _("双车占领开放线施压，以猛烈的进攻姿态快速吞吃敌方棋子。")}
            ],
            "defense": [
                {"名称": _("堡垒象"), "a":3, "b":8, "c":2, "文案": _("象藏兵链后构建铁桶阵——建立绝对防御姿态。")},
                {"名称": _("叠车防御"), "a":2, "b":7, "c":4, "文案": _("双车守护次底线化解进攻，没有棋子可以突破我的防线。")},
                {"名称": _("兵链封锁"), "a":1, "b":9, "c":3, "文案": _("用兵墙封锁所有突破点——对方的行动早在预测之中。")}
            ],
            "unconventional": [
                {"名称": _("弃子攻杀"), "a":9, "b":1, "c":7, "文案": _("L选择牺牲棋子，撕开裂口，用高风险换取高回报。")},
                {"名称": _("调虎离山"), "a":4, "b":5, "c":8, "文案": _("L在佯攻后翼时突然转向王翼，让月有些猝不及防。")},
                {"名称": _("幽灵牵制"), "a":3, "b":6, "c":9, "文案": _("L制造虚假威胁诱导失误，月仔细端详着棋路，目光在那几枚棋子上停留。")}
            ]
        },
        "endgame": {  # 英文标识：终局
            "offense": [
                {"名称": _("通路兵冲锋"), "a":6, "b":5, "c":3, "文案": _("远方兵全力推进，对胜利的执着追求支撑着士兵向前冲锋。")},
                {"名称": _("王翼入侵"), "a":7, "b":4, "c":2, "文案": _("国王亲自带队扫荡敌兵，欲戴王冠，必承其重。")},
                {"名称": _("闪击战术"), "a":8, "b":3, "c":4, "文案": _("利用牵制瞬间突破，如同死神收割敌方棋子的生命。")}
            ],
            "defense": [
                {"名称": _("对王战术"), "a":3, "b":8, "c":3, "文案": _("精确控制对王位置，逼迫对方无路可走，只能投降。")},
                {"名称": _("堡垒和棋"), "a":2, "b":9, "c":2, "文案": _("构建绝对防御结构，只要对方前进一步，必然遭受猛烈攻击。")},
                {"名称": _("永动机防守"), "a":1, "b":7, "c":5, "文案": _("现在棋盘上陷入一个怪圈，对方无论怎么走棋，都无法checkmate，只能在无限循环中和局。")}
            ],
            "unconventional": [
                {"名称": _("长将和棋"), "a":4, "b":4, "c":7, "文案": _("L步步紧逼，连续checkmate，试图把月逼入绝境。")},
                {"名称": _("逼和陷阱"), "a":5, "b":3, "c":8, "文案": _("L布下了一个陷阱，月只要吃掉那枚棋子就会滑落到只能求和的境地。")},
                {"名称": _("升变诡计"), "a":6, "b":2, "c":9, "文案": _("L的士兵推进到了底线，升变成为皇后，月的表情变得凝重。")}
            ]
        }
    }

    # Y的专属激进战术
    Y_aggressive_tactics = {
        "opening": [  # 英文标识：开局
            {"名称": _("王翼弃兵"), "a":8, "b":1, "c":6, "文案": _("月牺牲f兵换取开放线路猛攻，他的棋路极端而凶险，L不禁皱起眉头。")},
            {"名称": _("丹麦弃兵"), "a":9, "b":2, "c":4, "文案": _("月用双倍弃兵撕开防线，白色士兵已所剩无几，但是同样，L为了抵挡进攻也不得不损失了一些棋子。")},
            {"名称": _("中局弃兵"), "a":7, "b":3, "c":5, "文案": _("月无视士兵损失强行突破，白兵杀入黑方防线，逼迫对方露出腹地。")}
        ],
        "middlegame": [  # 英文标识：中局
            {"名称": _("双象冲锋"), "a":8, "b":3, "c":5, "文案": _("双象控制大斜线强攻，洁白的主教棋子闪烁着神圣审判的光芒。")},
            {"名称": _("皇后冒险"), "a":9, "b":2, "c":4, "文案": _("月操控皇后深入敌后制造混乱，他擅长利用手边一切可利用的，尤其是他的王牌。")},
            {"名称": _("马跳绝境"), "a":7, "b":4, "c":6, "文案": _("月执起白马跳入敌营中心发起敢死突击，迫使L不得不回头处理这枚危险的棋子。")}
        ],
        "endgame": [  # 英文标识：终局
            {"名称": _("弃兵引王"), "a":8, "b":2, "c":6, "文案": _("牺牲兵引诱敌王暴露，他擅长利用手边一切可利用的，包括他自己。")},
            {"名称": _("强制造杀"), "a":9, "b":1, "c":5, "文案": _("月无视损失构建杀网，他的棋路极端而凶险，L不禁皱起眉头。")},
            {"名称": _("时钟战术"), "a":7, "b":3, "c":7, "文案": _("月微微一笑，加快了下棋的速度，利用时间压力逼迫L失误。")}
        ]
    }

    # 克制关系
    counters = {
        "unconventional": {"defense": 1.2, "文案": _("非常规走法瓦解稳固防线。")},
        "aggressive": {"offense": 1.5, "defense": 1.3, "文案": _("以暴制暴压制常规进攻。")},
        "defense": {"aggressive": 1.2, "文案": _("铜墙铁壁阻挡冒进冲锋。")},
        "offense": {"unconventional": 1.2, "文案": _("精确计算破解花哨战术。")}
    }

    # 对抗计算
    def calculate_battle(L_tactic, Y_tactic, L_style, Y_style):
        L_effect = (L_tactic["a"] - Y_tactic["b"]) + (L_tactic["c"] - Y_tactic["c"]) * 0.3
        Y_effect = (Y_tactic["a"] - L_tactic["b"]) + (Y_tactic["c"] - L_tactic["c"]) * 0.3
        
        if Y_style in counters.get(L_style, {}):
            L_effect *= counters[L_style][Y_style]
            counter_text = _("\n◆ {desc}（获得克制加成）").format(desc=counters[L_style]["文案"])
        elif L_style in counters.get(Y_style, {}):
            Y_effect *= counters[Y_style][L_style]
            counter_text = _("\n◆ {desc}（获得克制加成）").format(desc=counters[Y_style]["文案"])
        else:
            counter_text = ""
        
        return L_effect - Y_effect, counter_text




# 游戏界面
screen chess_interface():
    frame:
        background "#00000078"
        xalign 0.3
        yalign 0.05
        xsize 500
        vbox:
            xalign 0.5
            label _("{color=#97c0fdff}国际象棋对决{/color}"):
                text_size 50
                xalign 0.5
                
            # 为比分文本添加翻译符号
            text _("当前比分: [total_score:.2f]") color "#ffffff"
            null height 20
            hbox:
                for phase in ["opening", "middlegame", "endgame"]:
                    if current_phase == phase:
                        textbutton _(phase_display[phase]):
                            style "selected_button"
                            action NullAction()
                    else:
                        textbutton _(phase_display[phase]):
                            action NullAction()


init python:
    def show_chess_character(char):
        if char == "L":
            renpy.show("chess_L", at_list=[renpy.store.center])
            renpy.with_statement(Dissolve(0.5))
        else:
            renpy.show("chess_y", at_list=[renpy.store.center])
            renpy.with_statement(Dissolve(0.5))
        renpy.pause(0.5)


# 主游戏流程
label start_chess_battle:
    $ current_phase = "opening"  # 初始阶段：英文标识
    $ total_score = 0.0
    $ phase_records = []
    
    scene chess with dissolve
    $ persistent.unlock_chess = True
    
    show screen chess_interface
    if chess_play_count == 1:
        "===== 国际象棋对决 =====" 
        sy"规则：L与月进行三局棋局对抗，月执白棋先走，L执黑棋后行。" 
        sy"在月选择战术走棋之后，请为L选择当局的战术风格，两人的战术进行对决。战术风格之间有克制关系，可自行摸索。"
        sy"左上角的计分板有当前比分与棋局的进行阶段。正数代表L占据优势，负数代表月占据优势。"
        sy"三局棋下完之后，根据最后的分数判定胜负。"
        sy"接下来游戏开始，请在月走棋之后选择本局的战术风格吧！"

    
    # 三阶段对决
    python:
        for phase in ["opening", "middlegame", "endgame"]:
            current_phase = phase
            renpy.notify(_("=== {} ===").format(_(phase_display[phase])))
        
            renpy.hide("chess_L")
            renpy.hide("chess_y")
   
            # 系统选择
            if renpy.random.random() < 0.5:
                Y_style = "aggressive"
                Y_tactic = renpy.random.choice(Y_aggressive_tactics[phase])
            else:
                Y_style = renpy.random.choice(["offense", "offense", "defense"])
                Y_tactic = renpy.random.choice(tactics_db[phase][Y_style])
            
            renpy.show("chess_y", at_list=[renpy.store.center])
            renpy.with_statement(Dissolve(0.3))
            renpy.say(Y, _("使用了【{name}】\n{desc}").format(
                name=Y_tactic["名称"], 
                desc=Y_tactic["文案"]))
            renpy.pause(0.5)
            
            # 使用 renpy.display_menu
            menu_items = [
                (_("进攻"), "offense"),
                (_("防守"), "defense"),
                (_("异想天开"), "unconventional")
            ]
            L_style = renpy.display_menu(menu_items)
            
            L_tactic = renpy.random.choice(tactics_db[phase][L_style])
            renpy.show("chess_L", at_list=[renpy.store.center])
            renpy.with_statement(Dissolve(0.3))
            renpy.say(L, _("使用了【{}】\n{}").format(L_tactic["名称"], L_tactic["文案"]))
            renpy.pause(0.5)
   
            # 计算对抗
            phase_score, counter_text = calculate_battle(L_tactic, Y_tactic, L_style, Y_style)
            total_score += phase_score
            phase_records.append((phase_score, counter_text))
            
    
    # 最终结果 - 使用标准翻译方式
    python:
        abs_score = abs(total_score)
        if abs_score < 0.8:
            ending_img = "chess_draw"
            chess_stats["draw"] += 1
        elif abs_score < 2.5:
            if total_score > 0:
                ending_img = "chess_L_win"
                chess_stats["L_win"] += 1
            else:
                ending_img = "chess_y_win"
                chess_stats["Y_win"] += 1
        else:
            if total_score > 0:
                ending_img = "chess_L_win"
                chess_stats["L_win"] += 1
            else:
                ending_img = "chess_y_win"
                chess_stats["Y_win"] += 1
        chess_stats["total_games"] += 1
    
    show expression ending_img at center
    
    hide screen chess_interface
    return


# 统计屏幕
screen chess_stats():
    frame:
        xalign 0.5
        yalign 0.05
        xsize 400
        ysize 430
        background "#9595959c"

        vbox:
            xalign 0.5
            yalign 0.5
            label _("历史对战统计"):
                text_size 45
            text _("总局数: [chess_stats['total_games']]")
            text _("L胜利: [chess_stats['L_win']]")
            text _("夜神月胜利: [chess_stats['Y_win']]")
            text _("平局: [chess_stats['draw']]")
            text _("L胜率: [int(chess_stats['L_win']/chess_stats['total_games']*100 if chess_stats['total_games']>0 else 0)]%")
            text _("夜神月胜率: [int(chess_stats['Y_win']/chess_stats['total_games']*100 if chess_stats['total_games']>0 else 0)]%")
            textbutton _("关闭"):
                action Return(True)
                


# 样式定义
style selected_button:
    background "#FFAAAA"
    hover_background "#FFCCCC"

screen pastime_notify(current, max_val, action_points):
    # 弹窗模式：阻止点击其他区域，必须点击确认才能关闭
    modal True
    zorder 200  # 确保弹窗在最上层显示
         
    vbox:
        xalign 0.5
        yalign 0.5
        spacing 30
        
        # 弹窗内容框
        frame:
            xsize 800
            ysize 200
            background "#a1a1a1d9"  # 半透明背景
            padding (10, 10)
            vbox:
                xalign 0.5
                yalign 0.2
                spacing 20
                # 标题
                text _("娱乐时间结束"): 
                    xalign 0.5

                hbox:
                    text _("好感度："):
                        min_width 80  # 固定标签宽度，对齐更整齐
                        yalign 0.5
                    bar:
                        value AnimatedValue(affection, affection_max, 1.0)  # 动画过渡效果
                        xmaximum 200  # 进度条宽度
                        ysize 26      # 进度条高度
                        yalign 0.5
                    text " [affection]/[affection_max]（[get_status_description(affection, affection_descriptions)]）":
                        yalign 0.5


    
        # 确认按钮
        textbutton _("确认"):
            action Return()  
            xalign 0.5
            ypos -90

translate None python:
    phase_display = {  # 阶段映射
        "opening": _("开局"),
        "middlegame": _("中局"),
        "endgame": _("终局")
    }
    style_display = {  # 战术风格映射
        "offense": _("进攻"),
        "defense": _("防守"),
        "unconventional": _("异想天开"),
        "aggressive": _("激进")
    }

    # ===== 战术数据库 =====
    tactics_db = {
        "opening": {  # 英文标识：开局
            "offense": [  # 英文标识：进攻
                {"名称": _("意大利开局"), "a":6, "b":3, "c":4, "文案": _("这种开局使用古典直接的中心控制，象瞄准f7弱点，随时准备攻陷敌方防线。")},
                {"名称": _("苏格兰开局"), "a":7, "b":2, "c":3, "文案": _("这种开局进行激进的中心争夺，在早期挑起激烈战斗，势如破竹。")},
                {"名称": _("维也纳开局"), "a":5, "b":4, "c":4, "文案": _("这种开局的特点是拥有灵活的转换结构，可转向攻守两种模式。")} 
            ],
            "defense": [  # 英文标识：防守
                {"名称": _("卡罗康防御"), "a":3, "b":7, "c":2, "文案": _("稳固的兵链结构，大军压境，缓慢推进反击。")},
                {"名称": _("斯拉夫防御"), "a":4, "b":6, "c":3, "文案": _("坚实的中心支撑，兵力集结，避免早期弱点。")},
                {"名称": _("剑桥泉防御"), "a":2, "b":8, "c":3, "文案": _("超稳固的龟缩阵型，考验对手的耐心。")}
            ],
            "unconventional": [  # 英文标识：异想天开
                {"名称": _("阿廖欣防御"), "a":4, "b":3, "c":8, "文案": _("L执起黑马跳入f6，引诱对手推进中心兵。他紧盯着月，看对方会如何回应挑衅。")},
                {"名称": _("格伦菲尔德防御"), "a":5, "b":4, "c":6, "文案": _("L放任白方占据中心，看似空门打开，实则预谋着在侧翼进行反击。")},
                {"名称": _("欧文防御"), "a":3, "b":5, "c":7, "文案": _("L执起象提前到b4，进行非常规牵制。月盯着棋盘陷入思考。")}
            ]
        },
        "middlegame": {  # 英文标识：中局
            "offense": [
                {"名称": _("王翼冲锋"), "a":7, "b":4, "c":3, "文案": _("h兵推进打开敌方阵地，试图在千军万马中直取敌王项上人头。")},
                {"名称": _("中心突破"), "a":6, "b":5, "c":2, "文案": _("d兵e兵强力推进粉碎防线，攻势凶猛。")},
                {"名称": _("双车入侵"), "a":5, "b":6, "c":4, "文案": _("双车占领开放线施压，以猛烈的进攻姿态快速吞吃敌方棋子。")}
            ],
            "defense": [
                {"名称": _("堡垒象"), "a":3, "b":8, "c":2, "文案": _("象藏兵链后构建铁桶阵——建立绝对防御姿态。")},
                {"名称": _("叠车防御"), "a":2, "b":7, "c":4, "文案": _("双车守护次底线化解进攻，没有棋子可以突破我的防线。")},
                {"名称": _("兵链封锁"), "a":1, "b":9, "c":3, "文案": _("用兵墙封锁所有突破点——对方的行动早在预测之中。")}
            ],
            "unconventional": [
                {"名称": _("弃子攻杀"), "a":9, "b":1, "c":7, "文案": _("L选择牺牲棋子，撕开裂口，用高风险换取高回报。")},
                {"名称": _("调虎离山"), "a":4, "b":5, "c":8, "文案": _("L在佯攻后翼时突然转向王翼，让月有些猝不及防。")},
                {"名称": _("幽灵牵制"), "a":3, "b":6, "c":9, "文案": _("L制造虚假威胁诱导失误，月仔细端详着棋路，目光在那几枚棋子上停留。")}
            ]
        },
        "endgame": {  # 英文标识：终局
            "offense": [
                {"名称": _("通路兵冲锋"), "a":6, "b":5, "c":3, "文案": _("远方兵全力推进，对胜利的执着追求支撑着士兵向前冲锋。")},
                {"名称": _("王翼入侵"), "a":7, "b":4, "c":2, "文案": _("国王亲自带队扫荡敌兵，欲戴王冠，必承其重。")},
                {"名称": _("闪击战术"), "a":8, "b":3, "c":4, "文案": _("利用牵制瞬间突破，如同死神收割敌方棋子的生命。")}
            ],
            "defense": [
                {"名称": _("对王战术"), "a":3, "b":8, "c":3, "文案": _("精确控制对王位置，逼迫对方无路可走，只能投降。")},
                {"名称": _("堡垒和棋"), "a":2, "b":9, "c":2, "文案": _("构建绝对防御结构，只要对方前进一步，必然遭受猛烈攻击。")},
                {"名称": _("永动机防守"), "a":1, "b":7, "c":5, "文案": _("现在棋盘上陷入一个怪圈，对方无论怎么走棋，都无法checkmate，只能在无限循环中和局。")}
            ],
            "unconventional": [
                {"名称": _("长将和棋"), "a":4, "b":4, "c":7, "文案": _("L步步紧逼，连续checkmate，试图把月逼入绝境。")},
                {"名称": _("逼和陷阱"), "a":5, "b":3, "c":8, "文案": _("L布下了一个陷阱，月只要吃掉那枚棋子就会滑落到只能求和的境地。")},
                {"名称": _("升变诡计"), "a":6, "b":2, "c":9, "文案": _("L的士兵推进到了底线，升变成为皇后，月的表情变得凝重。")}
            ]
        }
    }

    # Y的专属激进战术
    Y_aggressive_tactics = {
        "opening": [  # 英文标识：开局
            {"名称": _("王翼弃兵"), "a":8, "b":1, "c":6, "文案": _("月牺牲f兵换取开放线路猛攻，他的棋路极端而凶险，L不禁皱起眉头。")},
            {"名称": _("丹麦弃兵"), "a":9, "b":2, "c":4, "文案": _("月用双倍弃兵撕开防线，白色士兵已所剩无几，但是同样，L为了抵挡进攻也不得不损失了一些棋子。")},
            {"名称": _("中局弃兵"), "a":7, "b":3, "c":5, "文案": _("月无视士兵损失强行突破，白兵杀入黑方防线，逼迫对方露出腹地。")}
        ],
        "middlegame": [  # 英文标识：中局
            {"名称": _("双象冲锋"), "a":8, "b":3, "c":5, "文案": _("双象控制大斜线强攻，洁白的主教棋子闪烁着神圣审判的光芒。")},
            {"名称": _("皇后冒险"), "a":9, "b":2, "c":4, "文案": _("月操控皇后深入敌后制造混乱，他擅长利用手边一切可利用的，尤其是他的王牌。")},
            {"名称": _("马跳绝境"), "a":7, "b":4, "c":6, "文案": _("月执起白马跳入敌营中心发起敢死突击，迫使L不得不回头处理这枚危险的棋子。")}
        ],
        "endgame": [  # 英文标识：终局
            {"名称": _("弃兵引王"), "a":8, "b":2, "c":6, "文案": _("牺牲兵引诱敌王暴露，他擅长利用手边一切可利用的，包括他自己。")},
            {"名称": _("强制造杀"), "a":9, "b":1, "c":5, "文案": _("月无视损失构建杀网，他的棋路极端而凶险，L不禁皱起眉头。")},
            {"名称": _("时钟战术"), "a":7, "b":3, "c":7, "文案": _("月微微一笑，加快了下棋的速度，利用时间压力逼迫L失误。")}
        ]
    }




# 7. 定义RenPy翻译块（英文翻译，对应"english"语言）
translate english python:
    # 1. 映射表翻译：英文标识→英文显示文本
    phase_display = {
        "opening": "Opening",
        "middlegame": "Middlegame",
        "endgame": "Endgame"
    }
    style_display = {
        "offense": "Offense",
        "defense": "Defense",
        "unconventional": "Unconventional",
        "aggressive": "Aggressive"
    }

    # 战术数据库英文翻译（覆盖原_()包裹的中文文本）
    tactics_db = {
        "opening": {
            "offense": [
                {"名称": "Italian Game", "a":6, "b":3, "c":4, "文案": "This opening uses classical direct central control; the bishop targets the f7 weakness, ready to breach the enemy's defense at any time."},
                {"名称": "Scotch Game", "a":7, "b":2, "c":3, "文案": "This opening engages in aggressive central competition, sparking intense battles early on with unstoppable momentum."},
                {"名称": "Vienna Game", "a":5, "b":4, "c":4, "文案": "This opening features a flexible structural transition, capable of switching between offensive and defensive modes."}
            ],
            "defense": [
                {"名称": "Caro-Kann Defense", "a":3, "b":7, "c":2, "文案": "A stable pawn chain structure; the army presses the border, advancing counterattacks slowly."},
                {"名称": "Slav Defense", "a":4, "b":6, "c":3, "文案": "A solid central support, gathering troops to avoid early weaknesses."},
                {"名称": "Cambridge Springs Defense", "a":2, "b":8, "c":3, "文案": "An ultra-stable turtle formation that tests the opponent's patience."}
            ],
            "unconventional": [
                {"名称": "Alekhine's Defense", "a":4, "b":3, "c":8, "文案": "L picks up the black knight and jumps to f6, luring the opponent to advance the central pawn. He stares intently at Light to see how the latter will respond to the provocation."},
                {"名称": "Grünfeld Defense", "a":5, "b":4, "c":6, "文案": "L allows White to occupy the center; while it seems like an opening is left, he is actually plotting a counterattack on the flank."},
                {"名称": "Nimzo-Indian Defense", "a":3, "b":5, "c":7, "文案": "L moves the bishop to b4 in advance for unconventional pinning. Light stares at the board, deep in thought."}
            ]
        },
        "middlegame": {
            "offense": [
                {"名称": "Kingside Charge", "a":7, "b":4, "c":3, "文案": "Advance the h-pawn to open the enemy's position, attempting to take the enemy king's head directly amid the army."},
                {"名称": "Central Breakthrough", "a":6, "b":5, "c":2, "文案": "The d-pawn and e-pawn advance forcefully to shatter the defense, with a fierce offensive."},
                {"名称": "Double Rooks on the Open File", "a":5, "b":6, "c":4, "文案": "Double rooks occupy the open file to apply pressure, quickly devouring enemy pieces with a violent offensive stance."}
            ],
            "defense": [
                {"名称": "Fortress Setup", "a":3, "b":8, "c":2, "文案": "Hide the bishop behind the pawn chain to build an iron barrel formation—establishing an absolute defensive stance."},
                {"名称": "Stacked-Rank Defense", "a":2, "b":7, "c":4, "文案": "Double rooks guard the second rank to neutralize attacks; no piece can breach my defense."},
                {"名称": "Pawn Chain Blockade", "a":1, "b":9, "c":3, "文案": "Block all breakthrough points with a pawn wall—the opponent's moves are already within prediction."}
            ],
            "unconventional": [
                {"名称": "Piece Sacrifice Attack", "a":9, "b":1, "c":7, "文案": "L chooses to sacrifice a piece to tear open a gap, exchanging high risk for high reward."},
                {"名称": "Deflection", "a":4, "b":5, "c":8, "文案": "L feigns an attack on the flank, then suddenly shifts to the king's side, catching Light off guard."},
                {"名称": "Decoy Pin", "a":3, "b":6, "c":9, "文案": "L creates a false threat to lure a mistake; Light examines the chess path carefully, his gaze lingering on those few pieces."}
            ]
        },
        "endgame": {
            "offense": [
                {"名称": "Passed Pawn Charge", "a":6, "b":5, "c":3, "文案": "The distant pawn advances with all its strength; the persistent pursuit of victory supports the soldier's charge forward."},
                {"名称": "King's Side Invasion", "a":7, "b":4, "c":2, "文案": "The king leads the army personally to sweep the enemy's pieces; to wear the crown, one must bear its weight."},
                {"名称": "Pin and Breakthrough", "a":8, "b":3, "c":4, "文案": "Use pinning to break through in an instant, like the god of death reaping the lives of enemy pieces."}
            ],
            "defense": [
                {"名称": "Opposition", "a":3, "b":8, "c":3, "文案": "Precisely control the king's position to force the opponent into a dead end, leaving them with no choice but to surrender."},
                {"名称": "Fortress Draw", "a":2, "b":9, "c":2, "文案": "Build an absolute defensive structure; if the opponent takes even one step forward, they will surely suffer a violent attack."},
                {"名称": "Perpetual Check", "a":1, "b":7, "c":5, "文案": "The board is now stuck in a strange loop; no matter how the opponent moves, they cannot checkmate, and the game can only end in a draw through infinite repetition."}
            ],
            "unconventional": [
                {"名称": "Perpetual Check Draw", "a":4, "b":4, "c":7, "文案": "L presses forward step by step, delivering consecutive checks in an attempt to push Light into a desperate situation."},
                {"名称": "Forced Draw Trap", "a":5, "b":3, "c":8, "文案": "L sets a trap; if Light takes that piece, he will slip into a situation where he can only seek a draw."},
                {"名称": "Pawn Promotion to a queen", "a":6, "b":2, "c":9, "文案": "L's pawn advances to the back rank and promotes to a queen; Light's expression becomes solemn."}
            ]
        }
    }

    # Y的专属激进战术英文翻译
    Y_aggressive_tactics = {
        "opening": [
            {"名称": "King's Gambit", "a":8, "b":1, "c":6, "文案": "Light sacrifices the f-pawn to gain an open file for a fierce attack; his chess style is extreme and dangerous, making L frown involuntarily."},
            {"名称": "Danish Gambit", "a":9, "b":2, "c":4, "文案": "Light uses a double pawn sacrifice to tear through the defense; the white pawns are nearly gone, but similarly, L has to lose some pieces to fend off the attack."},
            {"名称": "Pawn Sacrifice (Middlegame)", "a":7, "b":3, "c":5, "文案": "Light ignores pawn losses and breaks through forcefully; the white pawns infiltrate the black defense, forcing the opponent to expose their interior."}
        ],
        "middlegame": [
            {"名称": "Bishop Pair Assault", "a":8, "b":3, "c":5, "文案": "Double bishops control the long diagonal for a strong attack; the white bishop pieces shine with the light of divine judgment."},
            {"名称": "Queen Infiltration", "a":9, "b":2, "c":4, "文案": "Light maneuvers the queen deep behind enemy lines to create chaos; he is good at using everything at his disposal, especially his trump card."},
            {"名称": "Knight Sacrifice", "a":7, "b":4, "c":6, "文案": "Light picks up the white knight and jumps into the center of the enemy camp to launch a desperate assault, forcing L to turn back and deal with this dangerous piece."}
        ],
        "endgame": [
            {"名称": "Decoy with Pawn", "a":8, "b":2, "c":6, "文案": "Sacrifice a pawn to lure the enemy king into exposure; he is good at using everything at his disposal, including himself."},
            {"名称": "Forced Checkmate", "a":9, "b":1, "c":5, "文案": "Light ignores losses to build a checkmate net; his chess style is extreme and dangerous, making L frown involuntarily."},
            {"名称": "Time Pressure", "a":7, "b":3, "c":7, "文案": "Light smiles slightly, speeds up his chess play, and uses time pressure to force L into a mistake."}
        ]
    }

    # 克制关系英文翻译
    counters = {
        "unconventional": {"defense": 1.2, "文案": "Unconventional moves break down stable defenses."},
        "aggressive": {"offense": 1.5, "Defense":1.3, "文案": "Suppress conventional attacks with violence."},
        "defense": {"aggressive": 1.2, "文案": "An iron wall blocks reckless charges."},
        "offense": {"unconventional": 1.2, "文案": "Precise calculations break down fancy tactics."}
    }

# 8. 定义RenPy翻译块（日文翻译，对应"japanese"语言，复用你之前的日文翻译结果）
translate japanese python:
    # 1. 映射表翻译：英文标识→日文显示文本
    phase_display = {
        "opening": "開局",
        "middlegame": "中局",
        "endgame": "終局"
    }
    style_display = {
        "offense": "攻撃",
        "defense": "防御",
        "unconventional": "奇抜な一手",
        "aggressive": "過激な一手"
    }
    # 战术数据库日文翻译
    tactics_db = {
        "opening": {
            "offense": [
                {"名称": "イタリアン・オープニング", "a":6, "b":3, "c":4, "文案": "このオープニングは古典的で直接的なセンターコントロールを使用し、ビショップがf7の弱点を狙い、随時敵の防線を攻略する準備をしています。"},
                {"名称": "スコッティッシュ・オープニング", "a":7, "b":2, "c":3, "文案": "このオープニングは攻撃的なセンター争奪を行い、序盤から激しい戦闘を引き起こし、勢いよく進みます。"},
                {"名称": "ウィーン・オープニング", "a":5, "b":4, "c":4, "文案": "このオープニングの特徴は柔軟な構造転換を持ち、攻撃モードと防御モードの両方に切り替えられることです。"}
            ],
            "defense": [
                {"名称": "カロカン防衛法", "a":3, "b":7, "c":2, "文案": "安定したポーンチェーン構造で、大軍が国境に迫り、ゆっくりと反撃を進めます。"},
                {"名称": "スラブ防衛法", "a":4, "b":6, "c":3, "文案": "堅固なセンター支援で、兵力を集結させ、序盤の弱点を回避します。"},
                {"名称": "ケンブリッジ・スプリングス防衛法", "a":2, "b":8, "c":3, "文案": "超安定した引きこもり陣形で、相手の忍耐力を試します。"}
            ],
            "unconventional": [
                {"名称": "アレヒン防衛法", "a":4, "b":3, "c":8, "文案": "Lは黒のナイトを取りf6に動かし、相手にセンターのポーンを進めさせる誘いをかけます。Lは月をしっかりと見つめ、相手がどう挑発に応えるかを観察しています。"},
                {"名称": "グルンフェルド防衛法", "a":5, "b":4, "c":6, "文案": "Lは白側にセンターを占めさせますが、一見防御が薄いように見えても、実は側翼で反撃することを企んでいます。"},
                {"名称": "オーウェン防衛法", "a":3, "b":5, "c":7, "文案": "Lはビショップを取り早めにb4に動かし、非伝統的な牽制を行います。月は盤面を見つめて思考に耽ります。"}
            ]
        },
        "middlegame": {
            "offense": [
                {"名称": "キングサイド突撃", "a":7, "b":4, "c":3, "文案": "hポーンを進めて敵の陣地を開き、多数の兵力の中から敵のキングを直接攻撃しようとします。"},
                {"名称": "センター突破", "a":6, "b":5, "c":2, "文案": "dポーンとeポーンを強力に進めて防線を粉砕し、攻撃は猛烈です。"},
                {"名称": "双ルーク侵入", "a":5, "b":6, "c":4, "文案": "双ルークが開放ラインを占領して圧力をかけ、猛烈な攻撃態勢で速やかに敵の駒を取ります。"}
            ],
            "defense": [
                {"名称": "要塞ビショップ", "a":3, "b":8, "c":2, "文案": "ビショップをポーンチェーンの後ろに隠して鉄壁の陣を構築し、絶対的な防御態勢を確立します。"},
                {"名称": "重ねルーク防御", "a":2, "b":7, "c":4, "文案": "双ルークがセカンドラインを守って攻撃を中和し、どの駒も私の防線を突破できません。"},
                {"名称": "ポーンチェーン封鎖", "a":1, "b":9, "c":3, "文案": "ポーンの壁ですべての突破点を封鎖し、相手の行動はすでに予測の範囲内です。"}
            ],
            "unconventional": [
                {"名称": "駒捨て攻撃", "a":9, "b":1, "c":7, "文案": "Lは駒を犠牲にすることを選び、防御の切れ目を作り、高いリスクで高い報酬を得ようとします。"},
                {"名称": "虎を遠ざけ山を離す策（陽動誘導）", "a":4, "b":5, "c":8, "文案": "Lは側翼を陽動攻撃している途中で突然キングサイドに方向を変え、月に手も足も出ないようにします。"},
                {"名称": "幽霊牽制", "a":3, "b":6, "c":9, "文案": "Lは偽の脅威を作って誤りを誘導します。月は棋路を注意深く観察し、視線をその数枚の駒にとどめます。"}
            ]
        },
        "endgame": {
            "offense": [
                {"名称": "パスポーン突撃", "a":6, "b":5, "c":3, "文案": "遠方のポーンを全力で進め、勝利への執念が兵士たちを前進させる突撃を支えています。"},
                {"名称": "キングサイド侵入", "a":7, "b":4, "c":2, "文案": "キングが自ら率いて敵の兵士を掃討します。王冠をかぶる者はその重さを負わなければなりません。"},
                {"名称": "閃撃戦術", "a":8, "b":3, "c":4, "文案": "牽制を利用して瞬間的に突破し、まるで死神が敵の駒の生命を刈り取るようです。"}
            ],
            "defense": [
                {"名称": "対キング戦術", "a":3, "b":8, "c":3, "文案": "キングの位置を正確に制御し、相手に逃げ場をなくし、降伏するよう追い詰めます。"},
                {"名称": "要塞引き分け", "a":2, "b":9, "c":2, "文案": "絶対的な防御構造を構築し、相手が一歩でも前進すれば必ず猛烈な攻撃を受けます。"},
                {"名称": "永久機関防御", "a":1, "b":7, "c":5, "文案": "現在盤面上は奇妙な循環に陥っており、相手がどのように駒を動かしてもチェックメイトできず、無限ループの中で引き分けになるしかありません。"}
            ],
            "unconventional": [
                {"名称": "長将棋引き分け", "a":4, "b":4, "c":7, "文案": "Lは一歩一歩迫り、連続でチェックをかけ、月を追い込もうとします。"},
                {"名称": "引き分け誘いトラップ", "a":5, "b":3, "c":8, "文案": "Lはトラップを仕掛けており、月がその駒を取るだけで引き分け以外に選択肢がない状況に陥ります。"},
                {"名称": "成り変わり策略", "a":6, "b":2, "c":9, "文案": "Lのポーンが最奥のラインまで進み、クイーンに成り変わり、月の表情が険しくなります。"}
            ]
        }
    }

    # 3. Y的专属激进战术翻译
    Y_aggressive_tactics = {
        "opening": [
            {"名称": "キングサイドポーン捨て", "a":8, "b":1, "c":6, "文案": "月はfポーンを犠牲にして開放ラインを得て猛攻します。その棋路は極端で危険であり、Lは思わず眉を顰めました。"},
            {"名称": "デンマークポーン捨て", "a":9, "b":2, "c":4, "文案": "月は倍のポーンを捨てて防線を破り、白のポーンは残り少なくなりましたが、同様にLも攻撃を防ぐためにいくつかの駒を失わざるを得ませんでした。"},
            {"名称": "中局ポーン捨て", "a":7, "b":3, "c":5, "文案": "月はポーンの損失を無視して強行突破し、白のポーンが黒側の防線に侵入し、相手の内側を露出させるよう逼迫します。"}
        ],
        "middlegame": [
            {"名称": "双ビショップ突撃", "a":8, "b":3, "c":5, "文案": "双ビショップが大斜線を制御して強攻し、白いビショップの駒は神聖な裁きの輝きを放っています。"},
            {"名称": "クイーン冒険", "a":9, "b":2, "c":4, "文案": "月はクイーンを敵の背後に深く進めて混乱を引き起こします。手元にあるすべてのものを活用するのが得意で、特に自らの切り札を活用します。"},
            {"名称": "ナイト絶境跳び", "a":7, "b":4, "c":6, "文案": "月は白のナイトを取り敵の陣営の中心に跳び込んで決死の突撃を仕掛け、Lにこの危険な駒を処理するために振り返るよう強います。"}
        ],
        "endgame": [
            {"名称": "ポーン捨てキング誘い", "a":8, "b":2, "c":6, "文案": "ポーンを犠牲にして敵のキングを露出させる誘いをかけます。月は手元にあるすべてのものを活用するのが得意で、自分自身も含みます。"},
            {"名称": "強行チェックメイト", "a":9, "b":1, "c":5, "文案": "月は損失を無視してチェックメイトの網を構築します。その棋路は極端で危険であり、Lは思わず眉を顰めました。"},
            {"名称": "時計戦術", "a":7, "b":3, "c":7, "文案": "月はほんのり笑い、チェスをするスピードを上げ、時間のプレッシャーを利用してLにミスを犯させようとします。"}
        ]
    }

    # 4. 克制关系翻译
    counters = {
        "unconventional": {"defense": 1.2, "文案": "非伝統的な駒の動かし方で安定した防線を崩します。"},
        "aggressive": {"offense": 1.5, "defense": 1.3, "文案": "暴力で暴力を制し、伝統的な攻撃を抑制します。"},
        "defense": {"aggressive": 1.2, "文案": "鉄壁の防線で無謀な突撃を阻止します。"},
        "offense": {"unconventional": 1.2, "文案": "正確な計算で華やかな戦術を解き明かします。"}
    }