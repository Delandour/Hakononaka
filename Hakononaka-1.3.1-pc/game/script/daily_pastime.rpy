default total_score = 0.0
default chess_play_count = 0
default read_book_count = 0
default blackjack_count = 0
default read_book_jie = False
default read_book_zuo = False
default read_book_nian = False
default pastime_points = 0 #当天对话次数（每日重置）
default current_phase = ""
default phase_records = []



# 在脚本开头定义
default chess_stats = {
    "L_win": 0,
    "Y_win": 0,
    "draw": 0,
    "total_games": 0
}

init python:
    import random
    # 定义游戏-标签映射字典，同时初始化计数器
    game_data = {
        "看书": {"label": "read_book", "count": 0},
        "下棋": {"label": "play_chess", "count": 0},
        "玩21点": {"label": "blackjack", "count": 0}
    }
    games = list(game_data.keys())  # 用于随机选择的游戏列表

label daily_pastime:
    $ Y_room = False
    if health <= 40:
        "夜神月看起来身体不适，需要尽快喂食药物。"
        menu:
            sy"需要返回行动菜单吗？"
            "返回":
                sy"不消耗行动点数，你还剩下[action_points]点行动点数。"
                $ Y_room = True
                jump action_menu

            "继续行动":
                if pastime_points >= 2:
                    "今天的娱乐时间已经足够了。"
                    "去做点别的事情吧。"
                    sy"你还剩下[action_points]点行动点数。"
                    $ Y_room = True
                    jump action_menu

                $ pastime_points += 1  
                hide screen stats with dissolve
                jump handle_pastime


    if pastime_points >= 2:
        "今天的娱乐时间已经足够了。"
        "去做点别的事情吧。"
        sy"你还剩下[action_points]点行动点数。"
        $ Y_room = True
        jump action_menu
    hide screen stats with dissolve
    $ pastime_points += 1  # 总对话次数+1
    jump handle_pastime



label handle_pastime:

    menu:
        "选择今天的活动："
        "看书":
            $ read_book_count += 1
            jump read_book
        "下棋"if day > 4:
            $ chess_play_count += 1
            jump play_chess
        "玩21点"if day > 7:
            $ blackjack_count += 1
            jump blackjack_game


define book = [_("《查拉图斯特拉如是说》"), _("《地下室手记》"), _("《化身博士》"), _("《麦田里的守望者》"), _("《悉达多》"), _("《1984》"), _("《使女的故事》"), _("《忒修斯之船》"), _("《玫瑰的名字》"), _("《沙之书》"), _("《银河系漫游指南》"), _("《Y的悲剧》"), _("《希腊棺材之谜》"), _("《雪崩》"), _("《发条橙》"), _("《恶魔的彩球歌》")]

translate japanese python:
    book = ["「ツァラトゥストラはかく語りき」", "「地下室の手記」", "「ジキル博士とハイド氏」", "「ライ麦畑でつかまえて」", "「シッダールタ」", "「1984」", "「侍女の物語」", "「テセウスの船」", "「薔薇の名前」", "「砂の本」", "「銀河ヒッチハイク・ガイド」", "「Yの悲劇」", "「ギリシャ棺の謎」", "「スノウ・クラッシュ」", "「時計じかけのオレンジ」", "「悪魔の手毬唄」"]

# 示例：看书游戏标签
label read_book:

    if read_book_count == 1:  # 第一次随机到

        "L拿着一本[renpy.random.choice(book)]走进了囚室，月明显注意到了，他的目光在书籍的标题上黏了几秒，然后又转回L。"

        if affection >= 60:

            "月的目光带着期待。"

            Y smile1"终于有些有趣的东西了吗？这里的生活确实太无聊了。"

            "L点头回应。"
        else:

            "月的目光充满嘲讽之意。"

            Y smile2"大侦探也会关心囚犯的心理健康吗？"

            "L无视了这句话。"

            L order2"我确实注意到了夜神君最近的压力指数有些高，看书是很好的放松方式，我挑了一些你可能会感兴趣的书。"

        if unlock_the_handcuffs == False:

            Y"听上去不错，但是我现在这样要怎么看书？"
        else:

            Y"好啊，那么请你把书给我吧。"
        if unlock_the_handcuffs:
            $ read_book_jie = True
            $ persistent.unlock_book_jie =True
            jump book3
        else:
            menu:
                "今天想采取的读书方式是……"
                "把书念给月听":
                    $ read_book_nian = True
                    $ persistent.unlock_book_nian =True
                    jump book1
                "坐到月身边一起看书":
                    $ read_book_zuo = True
                    $ persistent.unlock_book_zuo =True
                    jump book2
                "让他自己看（解开月的手铐）":
                    $ read_book_jie = True
                    $ persistent.unlock_book_jie =True
                    jump book3
    


    else:  # 第n次随机到
        """这是L第[read_book_count]次带着书前来了。
        
        他拿着一本[renpy.random.choice(book)]走进了囚室，月明显注意到了，他的目光在书籍的标题上黏了几秒，然后又转回L。"""

        if affection >= 60:

            "月的目光带着期待。他已经迫不及待想要读一些新的书了。"
        else:

            "月的目光很冷淡。如果可以，他希望L能只把书留下。"

        L"希望今天的书能让夜神君满意。"

  
        if unlock_the_handcuffs:
            $ read_book_jie = True
            $ persistent.unlock_book_jie =True
            jump book3

        menu:
            "今天想采取的读书方式是……"
            "把书念给月听"if unlock_the_handcuffs == False:
                $ read_book_nian = True
                $ persistent.unlock_book_nian =True
                jump book1
            "坐到月身边一起看书"if unlock_the_handcuffs == False:
                $ read_book_zuo = True
                $ persistent.unlock_book_zuo =True
                jump book2
            "让他自己看（解开月的手铐）":
                $ read_book_jie = True
                $ persistent.unlock_book_jie =True
                jump book3




label book1:
    scene book_nian with dissolve

    if read_book_count == 1:

        L"我可以念给夜神君听。"
    else:
        L"我念给夜神君听吧。"

    $ stress = max(0, stress-8)

    "月露出了“果然如此”的眼神。不过他也没有多说什么，毕竟在L的私人监狱里，他没办法抗拒L的意志。"

    "L坐到床边，和月保持了一定距离，他的嗓音低沉，语调平平不带感情，就像在念一份报告。"
    $ reaction_label = renpy.random.choice(full_reactions)
    call expression reaction_label from _call_expression_1  # 调用对应的反应标签
    jump daily_pastime_end  # 跳转到结束标签

label book3:

    scene book_jie with dissolve


    $ stress = max(0, stress - 10)

    if unlock_the_handcuffs:
        $ affection = min(affection + 3, 75)
    else:
        $ affection = min(affection + 3, 70)

    if unlock_the_handcuffs:
        "下一秒月有些诧异地看着L没有选择离开，而是同样坐了下来，望向他手中的书本。"
    else:
        Y smile1"谢谢。"

        """
        月活动了一下手腕，接过L手上的书籍，准备打开书本翻阅。

        下一秒他有些诧异地看着L没有选择离开，而是同样坐了下来，望向他手中的书本。
        """
    L smile2"我想和夜神君一起看。"

    Y Light"……算了，随你便吧"

    """ 
    月举着书，把朝向往L的方向偏了一些，让对方也能看见书上的文字。

    L从善如流地凑过来，蹲坐在月的旁边。

    月皱了皱眉，这么近的距离，他确实有点不太自在。

    这个距离近到已经突破了社交距离的30cm，近到他甚至能闻到L身上清爽的沐浴露味道。

    月强迫自己清空杂念，把注意力放到书上。
    """
    $ reaction_label = renpy.random.choice(limited_reactions)
    call expression reaction_label from _call_expression_2  # 调用对应的反应标签
    jump daily_pastime_end  # 跳转到结束标签

label book2:
    scene book_zuo with dissolve

    $ stress = max(0, stress-8)

    if read_book_count == 1:

        L"不用这么麻烦，这样夜神君也可以看见。"
    else:
        L"夜神君只要坐着就好。"

    """ L坐到了月的旁边，难得没有采用蹲姿，而是把书摊开到两人的大腿上。

    月皱了皱眉，这么近的距离，他确实有点不太自在。

    这个距离近到已经突破了社交距离的30cm，近到他甚至能闻到L身上清爽的沐浴露味道。

    月强迫自己清空杂念，把注意力放到书上。
    """    
    $ reaction_label = renpy.random.choice(limited_reactions)
    call expression reaction_label from _call_expression_3  # 调用对应的反应标签
    jump daily_pastime_end  # 跳转到结束标签

# 定义反应列表（存储标签名而非文本）
init python:
    # 完整反应列表（包含睡着，供book1使用）
    full_reactions = [
        "reaction_sleep",   # 反应1：睡着
        "reaction_chat",    # 反应2：聊天
        "reaction_debate",  # 反应3：辩论
        "reaction_angry"    # 反应4：愤怒
    ]
    
    # 精简反应列表（不含睡着，供book2和book3使用）
    limited_reactions = [
        "reaction_chat",    # 反应2：聊天
        "reaction_debate",  # 反应3：辩论
        "reaction_angry"    # 反应4：愤怒
    ]
# 反应1：睡着（分段显示）
label reaction_sleep:
    scene book_nian4
    $ persistent.unlock_book_nian4 =True

    "月听着听着，竟然产生了困意，不知不觉低着头睡着了。"
    "L察觉到之后停止了读书，有些无奈地让月侧躺在床上，给他盖上了被子，然后悄然离开了囚室。"
    return  # 结束后返回

# 反应2：聊天（分段+动作）
label reaction_chat:

    if read_book_jie == True:
        scene book_jie1 with dissolve
        $ persistent.unlock_book_jie1 =True
    elif read_book_nian == True:
        scene book_nian1 with dissolve
        $ persistent.unlock_book_nian1 =True
    elif read_book_zuo == True:
        scene book_zuo1 with dissolve
        $ persistent.unlock_book_zuo1 =True


    """ 月逐渐沉浸在了书中的世界里，看向把自己关起来的罪魁祸首也没那么不顺眼了，甚至偶尔还会跟L聊上几句书里的内容。
    
    两人度过了一段轻松愉快的时间。 """
    return

# 反应3：辩论（多段对话）
label reaction_debate:

    if read_book_jie == True:
        scene book_jie2 with dissolve
        $ persistent.unlock_book_jie2 =True
    elif read_book_nian == True:
        scene book_nian2 with dissolve
        $ persistent.unlock_book_nian2 =True
    elif read_book_zuo == True:
        scene book_zuo2 with dissolve
        $ persistent.unlock_book_zuo2 =True

    """ 月相当专注，在书的进度推进到他感兴趣的内容时，他甚至会主动叫住L来和自己讨论。
    
    他的见解相当锐利，直指矛盾核心，有时候可以说是激进，L也跟他有来有往地辩论起来，最后谁也没说服谁。
    
    不过月最后也没有显得生气，他难得直视L的眼睛，问他下次什么时候再把书带来。 """
    if unlock_the_handcuffs:
        $ affection = min(affection + 5, 75)
    else:
        $ affection = min(affection + 5, 70)

    return

# 反应4：愤怒（带情绪变化）
label reaction_angry:

    if read_book_jie == True:
        scene book_jie3 with dissolve
        $ persistent.unlock_book_jie3 =True
    elif read_book_nian == True:
        scene book_nian3 with dissolve
        $ persistent.unlock_book_nian3 =True
    elif read_book_zuo == True:
        scene book_zuo3 with dissolve
        $ persistent.unlock_book_zuo3 =True


    """ 月难得有了表达欲，他开始针对书中的内容发表自己的长篇大论，并且越说越兴奋。
    
    L对看书时频繁被打断的现状感到不满，于是他也开始了自己的报复行为：
    
    如果这是一本推理小说，他直接剧透了犯人是谁；
    
    如果这是一本哲学书，他专门翻到月讨厌的论点部分；
    
    如果……没有如果了，月彻底愤怒了，他大声控诉了L这种不道德的行为，但是L只是面瘫着脸把书合上，然后站到了囚室外面，关上门。
    
    月瞪着L，差点把自己气出内伤。 """
    $ affection = max(0, affection - 5)

    return


# 在脚本开头添加 blackjack 变量的声明
default blackjack = None
default blackjack_player_wins = 0
default blackjack_dealer_wins = 0
default blackjack_draws = 0

init python:
    import random
    
    # Card, Deck, Hand 类的定义保持不变
    class Card:
        def __init__(self, suit, value):
            self.suit = suit
            self.value = value
            
        def __str__(self):
            return f"{self.value}{self.suit}"
    
    class Deck:
        def __init__(self):
            self.cards = []
            self.build()
            
        def build(self):
            suits = ['♠', '♥', '♦', '♣']
            values = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
            self.cards = [Card(suit, value) for suit in suits for value in values]
            
        def shuffle(self):
            random.shuffle(self.cards)
            
        def deal(self):
            if len(self.cards) > 0:
                return self.cards.pop()
            else:
                self.build()
                self.shuffle()
                return self.cards.pop()
    
    class Hand:
        def __init__(self):
            self.cards = []
            self.value = 0
            
        def add_card(self, card):
            self.cards.append(card)
            self.calculate_value()
            
        def calculate_value(self):
            self.value = 0
            aces = 0
            
            for card in self.cards:
                if card.value in ['J', 'Q', 'K']:
                    self.value += 10
                elif card.value == 'A':
                    aces += 1
                    self.value += 11
                else:
                    self.value += int(card.value)
                    
            while self.value > 21 and aces > 0:
                self.value -= 10
                aces -= 1
                
        def __str__(self):
            return " ".join(str(card) for card in self.cards)

    # 全局变量定义
    blackjack_game_over = False
    blackjack_player_wins = 0
    blackjack_dealer_wins = 0
    blackjack_draws = 0
    
    # BlackjackGame 类定义
    class BlackjackGame:
        def __init__(self):

            self.deck = Deck()
            self.deck.shuffle()
            self.player_hand = Hand()
            self.dealer_hand = Hand()
            self.player_chips = 100
            self.current_bet = 0
            self.game_state = "betting"  # betting, player_turn, dealer_turn, game_over
            self.message = self._("欢迎来到21点游戏!")
            self.round_over = False
            
        def _(self, text):
            """动态翻译辅助方法"""
            return renpy.translate_string(text)
            
        def place_bet(self, amount):
            if amount <= 0:
                self.message = self._("下注必须大于0!")
                return False
            elif amount > self.player_chips:
                self.message = self._("你没有足够的筹码!")
                return False
            else:
                self.current_bet = amount
                self.player_chips -= amount
                self.game_state = "player_turn"
                self.deal_initial_cards()
                return True
                
        def deal_initial_cards(self):
            self.player_hand = Hand()
            self.dealer_hand = Hand()
            self.player_hand.add_card(self.deck.deal())
            self.dealer_hand.add_card(self.deck.deal())
            self.player_hand.add_card(self.deck.deal())
            self.dealer_hand.add_card(self.deck.deal())
            self.round_over = False
            
            # 检查黑杰克
            if self.player_hand.value == 21:
                self.message = self._("黑杰克! L赢了!")
                self.player_chips += int(self.current_bet * 2.5)
                self.round_over = True
                self.game_state = "game_over"
                store.blackjack_player_wins += 1
                
        def player_hit(self):
            self.player_hand.add_card(self.deck.deal())
            if self.player_hand.value > 21:
                self.message = self._("L爆点了! 月赢!")
                self.round_over = True
                self.game_state = "game_over"
                store.blackjack_dealer_wins += 1
            elif self.player_hand.value == 21:
                self.message = self._("L达到21点! 请停牌。")
                
        def player_stand(self):
            self.game_state = "dealer_turn"
            self.dealer_play()
            
        def dealer_play(self):
            while self.dealer_hand.value < 16:
                self.dealer_hand.add_card(self.deck.deal())
                
            self.determine_winner()
            
        def determine_winner(self):
            player_value = self.player_hand.value
            dealer_value = self.dealer_hand.value
            
            if dealer_value > 21:
                self.message = self._("月爆点了! L赢!")
                self.player_chips += self.current_bet * 2
                store.blackjack_player_wins += 1
            elif player_value > dealer_value:
                self.message = self._("L赢!")
                self.player_chips += self.current_bet * 2
                store.blackjack_player_wins += 1
            elif dealer_value > player_value:
                self.message = self._("月赢了!")
                store.blackjack_dealer_wins += 1
            else:
                self.message = self._("平局! 筹码返还")
                self.player_chips += self.current_bet
                store.blackjack_draws += 1
                
            self.round_over = True
            self.game_state = "game_over"
            
        def new_round(self):
            if len(self.deck.cards) < 10:
                self.deck = Deck()
                self.deck.shuffle()
                self.message = self._("新的一副牌已洗好!")
            else:
                self.message = self._("请下注")
            self.game_state = "betting"
            self.round_over = False

translate japanese strings:
    # game/script/daily_pastime.rpy中的BlackjackGame消息
    old "欢迎来到21点游戏!"
    new "ブラックジャックへようこそ！"
    
    old "下注必须大于0!"
    new "賭け金は0より大きくなければなりません！"
    
    old "你没有足够的筹码!"
    new "チップが足りません！"
    
    old "黑杰克! L赢了!"
    new "ブラックジャック！Lの勝ち！"
    
    old "L爆点了! 月赢!"
    new "Lがバースト！月の勝ち！"
    
    old "L达到21点! 请停牌。"
    new "Lが21点です！スタンドしてください。"
    
    old "月爆点了! L赢!"
    new "月がバースト！Lの勝ち！"
    
    old "L赢!"
    new "Lの勝ち！"
    
    old "月赢了!"
    new "月の勝ち！"
    
    old "平局! 筹码返还"
    new "引き分け！チップを返還します"
    
    old "新的一副牌已洗好!"
    new "新しいデッキをシャッフルしました！"
    
    old "请下注"
    new "賭けてください"




label blackjack_game:
    # 初始化 blackjack 游戏
    if blackjack is None:
        $ blackjack = BlackjackGame()
    if blackjack_count == 1:
        "L走进囚室，从牛仔裤裤兜里掏出一盒扑克牌。"
        Y "你是哆啦O梦吗？怎么每次都能掏出来一些奇怪的东西。"
        L unhappy "我可是好心为夜神君找来各种方便游玩的游戏来陪你，就用这种冷淡的态度对我吗？"
        Y "那是什么语气，好恶心。"
        L "……"
        L pt "总之，要来玩21点吗？"
        Y "好啊，反正闲着也很无聊。"
        "他们把囚室里唯一的一套桌椅搬到床对面，L抛弃了一看就很硬的椅子，蹲到了月的床上，月只能在椅子上落座。"
        sy"""===== 21点游戏规则 =====
        
        目标：使手牌点数总和尽可能接近21点，但不能超过。

        牌的点数：2-10：牌面点数；J、Q、K：10点；A：1点或11点（自动选择最有利的值）

        流程：

        L（玩家）拥有初始筹码100，每轮开始前下注。L和月（庄家）各发两张牌，月的一张牌隐藏。

        L可以选择"要牌"（再拿一张牌）或"停牌"（不再要牌）。L回合结束后，月要牌。

        比较双方点数，更接近21点的一方本局游戏获胜。根据游戏结果结算筹码，玩家可以选择继续或退出。

        游戏结束条件：

        1.筹码达到或超过300（获胜）。2.筹码为0（失败）。3.玩家主动退出。

        游戏开始。
            
        """
        jump blackjack
    else:
        "你已经玩了[blackjack_count]次21点。"
        sy"游戏开始。"
    # 初始化游戏状态
    $ blackjack_game_over = False
    $ blackjack.new_round()
    
    jump blackjack


label blackjack:
    # 确保 blackjack 已初始化
    if blackjack is None:
        $ blackjack = BlackjackGame()
    scene blackjack_1 with dissolve
    $ persistent.unlock_blackjack = True
    
    # 检查游戏是否结束
    if blackjack.player_chips <= 0:
        $ blackjack_game_over = True
        jump after_blackjack
    elif blackjack.player_chips >= 300:
        $ blackjack_game_over = True
        jump after_blackjack
    
    # 显示当前筹码和下注选项
    sy"当前筹码：[blackjack.player_chips]，获胜目标筹码：300。"
    
    if blackjack.game_state == "betting":
        menu:
            "当前筹码：[blackjack.player_chips]，请下注："
            "下注20筹码":
                if blackjack.place_bet(20):
                    jump blackjack_round
                else:
                    "[blackjack.message]"
                    jump blackjack
            "下注50筹码":
                if blackjack.place_bet(50):
                    jump blackjack_round
                else:
                    "[blackjack.message]"
                    jump blackjack
            "下注100筹码":
                if blackjack.place_bet(100):
                    jump blackjack_round
                else:
                    "[blackjack.message]"
                    jump blackjack
            "All in!":  # 新增的All in选项
                if blackjack.place_bet(blackjack.player_chips):
                    jump blackjack_round
                else:
                    "[blackjack.message]"
                    jump blackjack                  
    else:
        jump blackjack_round

# 新增blackjack_round标签处理游戏回合
label blackjack_round:
    # 显示初始手牌
    "L的手牌: [blackjack.player_hand] (点数: [blackjack.player_hand.value])\n月的手牌: [blackjack.dealer_hand.cards[0]] 和一张暗牌"
    
    # 如果是黑杰克，直接显示结果
    if blackjack.round_over:
        "[blackjack.message]"
        jump blackjack_2
    
    # 玩家回合
    while blackjack.game_state == "player_turn":
        menu:
            "L的手牌: [blackjack.player_hand] (点数: [blackjack.player_hand.value])，请选择："
            "要牌":
                $ blackjack.player_hit()
                "L要了一张牌。"
                "L的手牌: [blackjack.player_hand] (点数: [blackjack.player_hand.value])"
                
                if blackjack.round_over:
                    "[blackjack.message]"
                    jump blackjack_2
            "停牌":
                $ blackjack.player_stand()
                "L选择停牌。"
                jump blackjack_round
    
    # 庄家回合（自动进行）
    if blackjack.game_state == "dealer_turn":
        "月的手牌: [blackjack.dealer_hand] (点数: [blackjack.dealer_hand.value])\n[blackjack.message]"
        jump blackjack_2

# 修改blackjack_2标签
label blackjack_2:
    # 显示最终手牌和结果
    "最终手牌 - L: [blackjack.player_hand] (点数: [blackjack.player_hand.value])\n最终手牌 - 月: [blackjack.dealer_hand] (点数: [blackjack.dealer_hand.value])"

    
    # 检查游戏是否应该结束
    if blackjack.player_chips <= 0:
        $ blackjack_game_over = True
        jump after_blackjack
    elif blackjack.player_chips >= 300:
        $ blackjack_game_over = True
        jump after_blackjack
    
    # 询问是否继续
    menu:
        "当前筹码：[blackjack.player_chips]。是否继续下一轮？"
        "继续游戏":
            $ blackjack.new_round()
            jump blackjack
        "结束游戏":
            jump after_blackjack

# 新增after_blackjack标签处理游戏结束
label after_blackjack:
    scene blackjack_1 with dissolve
    
    # 判断游戏结果
    if blackjack.player_chips >= 300:
        scene blackjack_L_win with dissolve
        $ persistent.unlock_blackjack_Lwin = True
        "经过激烈的对战，L的筹码达到了[blackjack.player_chips]，超过了目标300！"
        "月看着筹码堆，表情复杂。"
        Y "看来今天运气站在你那边。"
        L smile2 "运气也是实力的一部分，夜神君。"
        $ stress = max(0, stress - 5)
        
    elif blackjack.player_chips <= 0:
        scene blackjack_Y_win with dissolve
        $ persistent.unlock_blackjack_Ywin = True
        "L的筹码输光了，月赢得了这场游戏。"
        Y deyi "看来即使是世界第一侦探，也有不擅长的事情。"
        L unhappy "……只是今天状态不好。"
        $ stress = max(0, stress - 8)
        if unlock_the_handcuffs:
            $ affection = min(affection + 3, 75)
        else:
            $ affection = min(affection + 3, 70)

    else:
        "游戏结束，L最终拥有[blackjack.player_chips]筹码。"
        "月看着筹码堆，表情平静。"
        Y "今天就到这里吧。"
        L "嗯。"
        $ stress = max(0, stress - 5)
    
    # 显示游戏统计
    "21点总对战局数统计："
    "L胜利: [blackjack_player_wins]局\n月胜利: [blackjack_dealer_wins]局\n平局: [blackjack_draws]局"
    
    
    # 重置游戏状态
    $ blackjack = BlackjackGame()
    
    # 跳转到日常娱乐结束
    jump daily_pastime_end



# 所有游戏结束后跳转到此
label daily_pastime_end:
    $ read_book_nian = False
    $ read_book_zuo = False
    $ read_book_jie = False
    show screen stats with dissolve
    
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

    # 消耗1点行动点数
    $ action_points -= 1
    call screen pastime_notify(affection, affection_max, action_points)
    # 检查行动点数是否归零
    if action_points <= 0:
        call next_day from _call_next_day_7 
    else:
        sy"你还剩下 [action_points] 点行动点数。"
    $ Y_room = True
    jump action_menu