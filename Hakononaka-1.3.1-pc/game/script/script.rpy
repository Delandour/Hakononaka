# 初始化随机数种子
init python:
    import random
    random.seed()

# 声明屏幕（增加交互确认功能）
screen legal_notice_screen():
    modal True  # 阻止玩家跳过
    add "legal_notice" xalign 0.5 yalign 0.5
    timer 4.0 action [Hide("legal_notice_screen", transition=Dissolve(1.0)), Return()]  # 必须显示4秒

# 定义启动屏幕：显示工作室图标
screen studio_splash():
    add "images/studio_logo.png" xalign 0.5 yalign 0.5  # 图标居中
    timer 3.0 action Hide("studio_splash", transition=Dissolve(1.0))  # 隐藏时用1秒溶解


# 启动流程（分三阶段）
label splashscreen:
    ## 第一阶段：工作室Logo展示（品牌宣传）
    show screen studio_splash with Dissolve(1.0)
    pause 3.0
    hide screen studio_splash with Dissolve(1.0)
    
    ## 第二阶段：法律声明（强制阅读）
    show screen legal_notice_screen with Dissolve(1.0)
    pause 
    hide screen legal_notice_screen with Dissolve(1.0)

    return


label start:

    scene notice2

    # menu:
    #     "是否重置画廊？"
    #     "是":
    #         #微笑主界面
    #         $ persistent.unlock_1 = False

    #         #日常行动-喂食、清洁
    #         #喂饭
    #         $ persistent.unlock_feed_1 = False
    #         #自己吃
    #         $ persistent.unlock_feed_2 = False
    #         #洗头
    #         $ persistent.unlock_bath_1 = False
    #         #擦身
    #         $ persistent.unlock_bath_2 = False
    #         #月自己擦身
    #         $ persistent.unlock_bath_3 = False
    #         $ persistent.unlock_bath_4 = False


    #         #粉红行动
    #         #腿交
    #         $ persistent.unlock_sex_1 = False
    #         #口交
    #         $ persistent.unlock_sex_2 = False
    #         #kiss分支L给月口交
    #         $ persistent.unlock_sex_kiss1 = False

    #         #be
    #         $ persistent.unlock_dead_end = False

    #         #日常行动-娱乐
    #         #看书
    #         $ persistent.unlock_book_jie = False
    #         $ persistent.unlock_book_jie1 = False
    #         $ persistent.unlock_book_jie2 = False
    #         $ persistent.unlock_book_jie3 = False
    #         $ persistent.unlock_book_nian = False
    #         $ persistent.unlock_book_nian1 = False
    #         $ persistent.unlock_book_nian2 = False
    #         $ persistent.unlock_book_nian3 = False
    #         $ persistent.unlock_book_nian4 = False
    #         $ persistent.unlock_book_zuo = False
    #         $ persistent.unlock_book_zuo1 = False
    #         $ persistent.unlock_book_zuo2 = False
    #         $ persistent.unlock_book_zuo3 = False
    #         #下棋
    #         $ persistent.unlock_chess = False
    #         $ persistent.unlock_chess_LY = False
    #         $ persistent.unlock_chess_draw = False
    #         $ persistent.unlock_chess_Lwin = False
    #         $ persistent.unlock_chess_Ywin = False
    #         "已重置完毕。"


    #     "否":
    #         "好的。"

    mb"""
    你好，这里是Neko Alliance工作室，欢迎您游玩《箱庭》！

    本游戏完全{color=#ff0000}免费{/color}，任何人不得以任何名义出售本游戏，{color=#ff0000}如果您花钱在他人处购买了本游戏的安装包，请立即找他退款。{/color}

    工作室联系方式：QQ号：3372414035；小红书ID：Neko Alliance，小红书号：95066558299；X账号@sanhuamao4280

    itch工作室主页：{a=https://neko-alliance.itch.io/}https://neko-alliance.itch.io/{/a}

    本游戏为R18游戏，请确保您已满18岁再游玩本作。

    注意，本游戏包含以下元素：囚禁、强奸（非自愿性行为）、BDSM、角色穿孔以及疼痛表现、主要角色死亡。

    如果您会对以上情节感到不适，请退出本游戏或者请不要攻略Bad End和Dead End。

    本游戏内可由玩家选择的性行为均为非自愿性行为，如果您会感到不适，请不要选择做爱选项。
    
    本游戏的cp为L月，请自行避雷。

    关于二次上传：允许截图游戏内画面进行repo，但是{color=#ff0000}禁止将所有cg图集截图以分享的名义打包上传到QQ群、小红书、LOFTER、微博等平台；{/color}

    {color=#ff0000}严禁将cg图打包在闲鱼等二手平台上售卖。{/color}

    所有cg画面均为工作室约稿所得，总花费 26791 RMB，作为中国大陆工作室，{color=#ff0000}一旦发现必追责，请不要抱有侥幸心理！{/color}

    所有cg画面均为工作室约稿所得，总花费 26791 RMB，作为中国大陆工作室，{color=#ff0000}一旦发现必追责，请不要抱有侥幸心理！{/color}

    所有cg画面均为工作室约稿所得，总花费 26791 RMB，作为中国大陆工作室，{color=#ff0000}一旦发现必追责，请不要抱有侥幸心理！{/color}
 
    以上，接下来请享受本作吧。

    """


    play music "jinpo.mp3"

    scene watari with vpunch

    play sound "sound/peopel huanjing.mp3"

    show ICPO with wiperight:
        xalign 0.18
        yalign 0.4
        zoom 0.8


    pb """ “到底是怎么回事？Kira为什么会在移交到国际刑事法庭的路上因为飞机失事死亡？”

    “让我们直接和L对话，交涉人！”

    “为什么不公开Kira的身份？！”

    会场里交涉人宣布继Kira死亡之后，L将退出对Kira事件的调查。这通发言掀起了轩然大波。

    各国的警方如同八卦记者一样，恨不得从座位上跳起来扑向渡，把话筒递到渡的嘴边。只有日本的警方端坐在座位上，保持沉默。 """

    #voice "voice/L/L1_silence.mp3"

    D 2 "请肃静，现在就让大家听听L的声音。"
    stop sound
    play sound "sound/microphone_feedback.mp3"
    queue sound "sound/people whisper.mp3" loop

    pb "话筒一阵刺耳的高音过后，会场恢复了安静，警官们窃窃私语着，猜测交涉人会给出什么回答。"

    show watari_labtop with wipeleft:
        xalign 0.9
        yalign 0.7
        zoom 0.75


    pb "渡打开一台银白色的笔记本电脑，L哥特字母的图案出现在电脑屏幕和会场的大荧幕之上，L独特的电子音也随之响起。"

    #voice "voice/L/L1_ICPO.mp3"

    L laptop """ICPO的各位，我是L。

    在各位屈服于Kira的杀人能力的时候，是我带领人员秘密调查，找到了真凶。

    当Kira在日本落网之后，政府又开始心思活跃，开始想要利用Kira的杀人能力。

    恕我直言，这简直是卑鄙无耻的行为。

    现在我正式宣布退出对Kira事件的调查，此案相关的情报我会永远保守秘密。

    以上，谢谢聆听。"""

    hide watari_labtop

    pb "语音通话被挂断了，渡干脆利落地合上电脑，在众人反应过来之前从后门离开了。"

    hide ICPO

    scene black with dissolve
    stop sound

    pb "被关在身后的，是一片哗然的会场，充斥着对L狂妄言论的声讨，渡对此的反应只是扶正了有些歪斜的礼帽。"
    pb """L本人早已预料到了这种情况，所谓的语音通话只是提前准备好的录音，
    
    他这次来并不是为了解释什么，或者和警方们谈心，只是在通知罢了。"""
    pb "本尊早就将此事抛之脑后，划定为已完成的事项，不再关心。"
    pb "因为他现在，有更加关注的事情。"
 
    scene L_sofa
    with dissolve

    pb "蹲坐在舒服的皮质沙发椅上，海绵和弹簧提供恰到好处的支撑力，宽大的座椅让整个人团在里面也不会觉得狭窄。"
    pb """口味浓郁的香草奶油冰激凌被装在造型精美的镭射玻璃高脚杯里，上面淋了一层巧克力，
    
    上面本应点缀的车厘子已经被吃掉了，一柄银质餐匙斜靠在杯壁上，匙面上还有未吮干净的奶油。"""
    
    L icecream1 "已经结束了吗？辛苦你了，渡。"
    D "引起了相当大的骚动呢，不知道之后会持续多久。"
    L icecream1 "既定事实确定之后，公众很快就会把注意力转移到别的事情上的。"
    pb "老人在话筒对面叹了口气，L感受到对方的担忧之情，但只是抿着嘴，固执地不愿意说更多。"
    L icecream1 "渡，快回来吧。"

    pb """

    切断通讯后，L的视线落在屏幕上的一点，失去了焦距，难得发了会呆。

    ……无论如何，已经做下的事情，不会改变。

    他不是会为打翻的牛奶惋惜的人。

    视线重新聚焦，落在了一处监控屏幕上。

    那屏幕里铁黑的栏杆排列，明显是一间牢房。

    而在牢房之中，正关押着一名青年。

    一名有着褐色柔顺头发，年纪不大，身材匀称的青年。

    他正穿着纯黑的囚服，双手被反铐在身后，双脚也被紧缚，低着头，从监控摄像头里看不清他的表情。

    如果是不知情的旁人看见，估计会好奇，这青年犯了什么罪，需要被这样严苛地对待？

    这时候如果告诉这人，这位就是大名鼎鼎的、正处于死亡状态的Kira，估计会被吓一跳吧。

    完全无法想象，这名看起来年轻优秀的青年会是以一己之力恐吓威慑全世界罪犯的传奇杀人犯。

    夜神月……L在心里默念着这名青年的名字。

    私心亦或是私刑，这的的确确是他做的事情。

    愚弄了全世界，将Kira关在了自己的秘密牢房内。

    胆大包天地留有Kira对死亡笔记的所有权，只为了让夜神月保留使用死亡笔记和他对弈的记忆。

    消去对方的现实社会身份，无论做了什么都不会被世人发现。

    此处，是他所搭建的{color=#0000ff}箱庭世界{/color}。

    """
    
    stop music fadeout 1.0  
    play music "audio/daily.mp3" 
    scene main bg_1 with fade
    show screen stats
    with dissolve

    "曾持有世界上最恐怖的杀人凶器的罪犯被关押在这里，即使世人皆以为他已经死去。"
    "褐发青年被戴上镣铐，不过他依然表现得相当平静。"
    sy"今天是监禁的第 [day] 天。"
    sy"现在有 [action_points] 个行动点数。"
    sy"点击行动菜单上的按钮就可以采取行动，注意拖动滚动条可以查看粉红行动的选项按钮哦。"
    sy"接下来可以行动了。"
    menu:
        sy"需要查看新手教程吗？"
        # "测试选项":
        #     jump food_h7
        "需要":
            sy"""

            在本游戏中，你可以用L的视角在21天内对监禁中的夜神月采取任意行动。

            每天有4个行动点数，行动点数耗尽后进入下一天。

            注意，外出和做爱会消耗2点行动点数。外出需要一定的天数和好感度才能解锁。

            采取不同的行动，夜神月的状态也会发生改变。温柔地对待亦或是冷酷地折磨？由你来决定。

            右上角显示的是夜神月的简易状态值，点击行动菜单里【月的状态】可以查看详细的数值。

            月好感度的高低有时候会影响剧情的发展，同时是影响结局走向的重要数值。

            在本游戏中，月的好感度最高只能升到75。考虑到月的人设，他是一个很难对别人交心的人呢。

            请时刻注意月的饱食度、清洁度、压力值，如果数值太低会降低月的健康值。

            如果健康值归零，游戏会结束，进入Dead End。
            
            注意，在死亡结局中有对角色死亡的描写，请做好心理准备，即使是虚拟角色也请爱护他吧。

            粉红行动和外出会消耗月的体力值，月每天会根据身体情况恢复一定的体力值。如果月的身体状态好，会恢复更多的体力值。

            涩涩虽好，但是需要节制哦~

            侧边栏【月的房间】按钮，点进去之后可以查看囚室的整体图和夜神月的Q版状态。点击小月可以进行互动~

            如果在意月的囚室生活，请经常点进去看看吧！

            本游戏一共有Normal END、Happy END、Bad END、TRUE END四个结局，请尽情地存档与读档吧！
            
            True END需要解锁NE、HE、BE中任意两个结局解锁，在标题页面的【额外内容】中查看。
            
            如果不知道怎么解锁HE与BE，【额外内容】中也有相应的攻略提示。

            可以在标题画面的【画廊】查看已经收集到的CG。

            以上，祝您游玩愉快~

            """
        "不需要":
            sy"祝您游玩愉快~"
    $ Y_room = True


label action_menu:

    $ renpy.choice_for_skipping()

    call screen action_menu(adj=choice_adjustment)

    $ choice = _return

    if not choice:
        jump status 

    $ reset_example()

    call expression choice.label from _call_expression
    $ Y_room = True
    jump action_menu

label status:

    call screen status

    if not choice:
        $ Y_room = True
        jump action_menu 

init python:
    import random

label next_day:

    
    # 增加天数
    $ day += 1

    # 原有特殊事件逻辑
    if day == 22:
        jump end_choose

    # 重置行动点数
    $ action_points = 4
    $ daily_gift_count = 0
    $ dialog_points = 0
    $ pastime_points = 0

    $ kiss2_points = 0
    $ fondle2_points = 0
    $ current_food_choice = None  # 清空前一天的食物选择
    $ fed = False  # 重置当日喂食状态

    # 饱食度每日自然下降
    $ satiety = max(0, satiety - 25)
    
    # 清洁度每日自然下降
    $ clean = max(0, clean - 15)

    $ stress = min(100, stress + 3)

    
    # 计算饱食度对健康的影响
    $ satiety_penalty = 30 if satiety <= 0 else (10 if satiety <= 30 else 0)
    
    # 计算清洁度对健康的影响
    $ clean_penalty = 30 if clean <= 0 else (10 if clean <= 30 else 0)

    $ stress_penalty = 20 if stress >= 90 else (10 if stress >= 70 else 0)
    
    # 应用健康惩罚
    $ health = max(0, health - satiety_penalty - clean_penalty - stress_penalty)

    if health >= 61:
        $ stamina = min(100, stamina + 25)
    elif 41 < health < 61:
        $ stamina = min(100, stamina + 15)
        $ stress = min(100, stress +2)
    else:
        $ stamina = max(0, stamina - 20)
        $ stress = min(100, stress +7)
    
    if satiety >= 70 and clean >= 70:
        $ health = min (health + 8, 100)

    # 检查健康值是否为0
    if health <= 0:
        jump dead_end

    if satiety < 40:
        $ affection = max(0, affection-10)
        $ stress = min(stress + 10, 100)

    if clean < 40:
        $ affection = max(0, affection-10)
        $ stress = min(stress + 5, 100)

    if stress > 60:
        $ affection = max(0, affection-5)

    if health < 60:
        $ affection = max(0, affection-10)

    if Light_photo:

        if renpy.random.random() < 0.2:

            L"（刚好有空闲……夜神君在干什么呢？）"

            """ 侦探熟门熟路地点开囚室的监视画面，发现褐发青年正坐在床边，头颅低垂，怔怔地注视着手中的相框。 """

            L"（那个是……之前送给夜神君的家庭合照吧。）"

            """ 因为牢狱之灾显得略长的刘海遮住了一半眼睛，让L读不懂夜神月此时的表情。

            青年的视线虚虚地落在相片里幸福美满的一家人身上，仿佛在透过一张定格时光的相纸回忆着什么。

            L无法共情这种感受，他对于家庭的概念是模糊的，他的童年里也没有关爱他的父母和会向他撒娇的弟弟妹妹。

            L不认为渡是普世意义上的【父亲】角色，渡是家人，也是引导者和助手。在很长一段时间中，一片黑白的世界里，渡是唯一拥有色彩的人类。

            现在拥有色彩的人选多了一位，是他所认可的对手和唯一感兴趣的人类——夜神月。 """

            L"（看来，家人对于夜神君也是很重要的存在呢。）"

            L"（家庭……是怎样的存在呢。想象不出来。）"

            """ L捏起一块马卡龙，放入口中咀嚼，甜腻的甘纳许混合着淡淡的杏仁香气在口腔里弥漫开来，画面中的褐发青年结束了沉思，把相框摆回了置物架上。 """

    if Light_mirror and Light_brush:

        if renpy.random.random() < 0.3:

            """ L已经养成了时不时往月的房间监控画面看一眼的习惯，有时候他会看见有趣的场景，比如现在——

            夜神月正坐在桌边，对着便携化妆镜整理自己的仪容。

            青年用木梳仔细梳理自己的头发，把杂乱的头发整理得柔顺光洁，小心地调整刘海的高度。 """

            Y"（头发有点长太长了，最近刘海老是扎到眼睛。）"

            Y"（要干脆把刘海梳开吗……但是不太习惯呢。）"

            Y"（或者拜托龙崎带自己去理发店？嗯……这个稍微有点……）"

            Y"（还是请渡先生帮忙呢……他看起来很全能的样子，就是平时见不到面。）"

            Y"（讨厌的牢狱生活，感觉皮肤都粗糙了很多。脸上都有油脂粒了……）"

            """ 叹了口气，月合上了化妆镜，把小镜子和梳子放回置物架上。 """

            L"（像是会打理自己的毛发的小动物……）"

    if Light_book and Light_light:

        if random.random() < 0.3:

            """ 夜晚的时间，L的房间通常处于静谧之中，所以从音箱中传来的翻动书页的声音格外清晰。 """

            L surprise"（我记得夜神君的囚室应该已经熄灯了才对。）"

            """ L将监控画面切换到最上方，看见囚室中亮起了一盏微光，褐发青年坐在桌前阅读他所精心挑选的书籍，享受着熬夜的快乐。

            台灯的光芒下，青年俊美的眉眼低垂，光影柔和了锋利的五官。他漫不经心地一手撑着脸，一手翻动书页，已是看得入迷。

            遇见无聊的部分，月的阅读速度会明显加快，纸张翻动的声音连成一片；

            遇见有趣的部分，月的目光则会久久停留在泛着油墨香的字句上，甚至在阅读中露出微笑。 """

            L smile1"（嗯……如果再过半小时，夜神君还没有睡觉的话，就提醒他一下吧。熬夜太长时间不利于身体健康。）"

            """ 每天都在熬夜且毫无自知的黑发侦探又观赏了几分钟监控画面，最后把窗口缩小固定在了显示器的左上角。 """

    if Light_cake:

        if stress < 40:

            """ L在监控屏幕里看见月坐在桌前吃掉了那块草莓蛋糕，露出了意外的神色。 """

            L surprise"（是觉得比想象中好吃吗？）"

            """ 褐发青年一口接着一口把一整块切角蛋糕吃进了肚子，最后唇边沾上了一块白色的奶油。

            L看得心里有些发痒，把拇指贴上液晶屏幕，好像可以隔着屏幕帮月擦去那块不小心沾上的奶油。

            不过很快，月自己也意识到了这点，伸出舌尖把唇边的奶油舔掉了。 """

            L smile1"（总感觉……自己也有点想吃草莓蛋糕了。）"

            $ satiety = min(satiety + 10 , 100)
            $ Light_cake = False

        elif stress < 70:

            """ L在监控屏幕里看见月坐在桌前，神色有些郁郁寡欢，那块蛋糕只是吃了几口就放下了。

            塑料的一次性餐叉被搁置在一旁，残留的奶油很快就塌陷了。 """

            L unhappy"（今天夜神君的心情好像不是很好呢……）"

            L thinking"（之后要去陪他玩点什么吗？）"

            $ Light_cake = False

        else:

            """ 蛋糕被原封不动地放在桌上，直到奶油塌陷发硬都没有被受赠予者进食。表皮已经开始发蔫的草莓显得有些可怜。 """

            L unhappy"（夜神君的心情好像很差啊……是没有吃甜食的心情吗？）"

            L thinking"（要不要明天带他做一些能放松的事情呢。）"

            $ Light_cake = False

        # 蛋糕事件结束

    if day == 4:
        stop music fadeout 2.0
        hide screen stats with dissolve 
        window hide
        scene black with dissolve
        pause 1.0
        play music "audio/night.mp3" 
        """ 【夜晚熄灯的前十分钟】

        夜神月的生物钟提醒他，快到要睡觉的时间了。

        每当这时候他就会看见L的身影从黑暗中浮现在囚室栏杆之前，在囚室惨白的灯光下如同幽灵。栅栏门打开时咔哒作响，再重重地关上。 """

        L"到要睡觉的时间了，夜神君。"

        """ 一开始月还不太习惯L的出现，他在心中暗忖这不是狱警的工作吗，有什么值得L亲自关监的？但是如今已经是重复到让人倦怠的流程。 """

        Y"我知道了。"

        """ 褐发青年微微一用力，让自己侧躺在床上，然后被绑住的双脚也挪上来，整个人像体操运动员那样费力地扭动着身体。

        夜神月在被拒绝过一次之后就放弃请求L在睡前解开自己的手铐了，他宁愿用这种别扭的姿势调整自己的睡姿，也不要顺应L可能想听见他低声下气恳求的心思。

        月想不明白如今睡觉时解开自己的手铐又能怎样？他还能干什么？打手冲吗？

        还是算了，只是幻想一下在L的监视下干这种事情就让人想吐。

        L从床头把叠好的被子打开，月的视野会短暂地陷入黑暗，随后又露出白炽灯和L那张讨厌的脸，对方会像有强迫症一样把被子平摊得整整齐齐，均匀地盖在月的身上。 """

        Y"（每天睡前要看见这张脸，真是让人想做噩梦。）"

        """ 之后月会再借助腰腿发力让自己躺到枕头上，睡前运动终于结束。 """

        L"晚安，夜神君。"

        stop music fadeout 2.0

        """ 那双漆黑的眼睛离开了，月因为L有些紧绷的神经稍稍放松。

        在L离去后的五分钟左右，囚室就会陷入黑暗，四周安静得月只能听见自己的呼吸声。"""

        scene black with dissolve

        """月强迫自己闭上眼睛，他需要睡觉，需要通过睡眠来恢复精力，这样他才有足够的体力来抵抗可能漫长到无法想象的监禁。

        今天是被转移到L这里的第三天。已经比之前好多了。所以无需害怕了。

        不断地不断地在心中重复着话语，催眠着自己，夜神月才能做到勉强入睡。

        从弥海砂被当作第二Kira嫌疑人所逮捕，自己主动通过被监禁来洗清嫌疑之后，夜神月就再也没有回到过正常的生活之中。

        在长达50日的拘束监禁、作为Kira被逮捕、现在转移到L的牢房这大半年时间内，最平和的时间竟然是和L铐在一起的时光。

        能够睡在普通的床上，普通地洗澡和进食，斗志满满地想要抓到真正的Kira来洗清嫌疑，连对L的讨厌之情都被找到四叶时的激动和兴奋冲淡了。

        失去记忆时，甚至会和L打架的，愚蠢又天真的自己。

        那样的生活现在竟让现在的自己感到了一丝羡慕。是被吐真剂和电击弄坏了脑子吗？

        一阵突如其来的强烈的自我厌恶席卷了月的心底，他怎么会羡慕那种天真的一无所知的状态？难道他在为使用死亡笔记后悔吗？

        不对，不是的，不是这样的！他从来没觉得得到死亡笔记是不幸的事情！

        丧失记忆只是手段，不能成为逃避的居所，如果遗忘，就等同于背叛。

        这样想着，头皮处似乎又传来了烧灼般的剧痛。

        {color=#0000ff}【因为是珍贵的活体Kira，所以不可以对他的身体造成不可逆的伤害，口口最后选择了相对无害的审问方式，即注射吐真剂配合电击头部的特定神经进行审问。{/color}

        {color=#0000ff}为了保证审问者的人身安全，犯人全身穿着拘束衣被固定，同时眼部佩戴眼罩进行视力剥夺。{/color}

        {color=#0000ff}审问过程中首先给犯人注射硫喷妥钠，让犯人处于轻度麻醉状态，无法进行深度思考。{/color}

        {color=#0000ff}前期提问内容为已知的信息，用于确认犯人现在的精神状态。注意，Kira没有个人隐私而言，审问者不可因为犯人的年龄而心生恻隐之心。{/color}

        {color=#0000ff}后期提问内容主要围绕他是否知情死亡笔记的修复方法、世界上是否有第二本死亡笔记、死亡笔记的具体规则以及应用方法等。{/color}

        {color=#0000ff}当犯人的回答与答案不同时，使用电击进行惩罚。只有一天内正确回答额定的问题数量后才能给他提供可入口的食物。{/color}

        {color=#0000ff}Kira是人类史上最恶劣的杀人犯，对其采取各种措施都是被允许的。{/color}

        {color=#0000ff}唯一需要保证的是Kira的生存，在犯人无法继续回答问题时，使用鼻胃管将营养制剂输送到胃内进行生命维持。】{/color}"""

        play sound "audio/sound/tinnitus.mp3"

        """{color=#f00}不可再想起那片黑暗。{/color}

        {color=#f00}不可以不可以不可以不可以不可以不可以不可以不可以不可以不可以不可以不可以不可以{/color}

        {b}{color=#f00}快忘掉快忘掉快忘掉快忘掉快忘掉快忘掉快忘掉快忘掉快忘掉快忘掉快忘掉快忘掉快忘掉快忘掉快忘掉快忘掉快忘掉快忘掉快忘掉快忘掉快忘掉{/color}{/b}

        伴随着强烈的耳鸣声的，是某人在呼喊他的名字——

        “夜神君？夜神君？月君！你还好吗？快醒醒！月君！” """
        stop sound
        scene room_1 with flashbulb
        
        Y jiaoji1"……！！"

        """ 月猛地从梦魇中惊醒，他褐色的额发已经被冷汗打湿了，全数黏在皮肤上，传来又凉又粘腻的触感。

        他的头还在一阵一阵发晕，视野在一片模糊中被大力晃动，在费力地眨眨眼后终于看清了叫醒他的人的样貌。

        纯黑的头发和眼睛，独属于欧洲人的五官，苍白的皮肤，此刻眉头正紧皱着盯着自己看。

        是L。夜神月在意识到这一点后反而有种诡异的安心感。真是令人作呕的感觉。 """
        play music "audio/night.mp3" 
        Y yaoya"……我没事。"

        L order1"勉强自己也要有一个限度。"

        """ L的语气还是很生硬，但是月发现自己手腕处的手铐被解开了，L往他的手中塞了一瓶温热的瓶装水。 """

        L order2"请喝吧。"

        Y pt"不把我的手铐铐上喂我喝吗？"

        L"看见夜神君现在这么有精神真是太好了。如果这是你的请求的话，我会照做的。"

        """ 在L真的低下头把脸凑过来时，月悚然一惊，不自然地侧过了身体，嘴上只能服软。 """

        Y"……谢谢，但是还是不用了。"

        """ 在月安静地吞咽矿泉水时，L也在一旁安静地站着，似乎是在思考什么。 """

        L"“我不知道。”"

        Y"什么？"

        L"夜神君的梦话。你一直在重复这句话。“我不知道。”这是你的噩梦内容吗？"

        """ 月陷入了沉默。

        他本就不擅长把脆弱的一面展露人前，更何况对象是L，他认定为宿敌的人选。几乎不需要思考，月就做出了判断。 """

        Y"""……你听错了吧。
        
        我不记得我说过这种话，现在连梦见什么都不记得了。
        
        谢谢你的水，我喝好了。"""

        """ 月把手上剩下的半瓶水往上递去，L的半张脸在透明矿泉水瓶的折射下扭曲变形，另外半张脸则是一如既往的冷淡。 """

        L pt"这瓶水我就不收走了，请夜神君自己留下吧。"

        Y fadai"那手铐……？"

        L"今天晚上就不用了。开灯时我会来的。请好好休息。"

        """ L雪白的身影远去了，月盯着他的背影难得发了会呆，直到五分钟过去，黑暗重新笼罩了囚室。"""

        scene room_2 with dissolve

        """月摸索着把水瓶放到床头边的地面上，重新躺回了床上。

        被冷汗打湿的后背依然粘腻得令人难以忍受，但是能够自由活动的双臂带来的舒适感就像一直憋气的人突然恢复呼吸一样，让月可以忽略这点小小的不适。

        L……难道真的一直在看着自己吗？想想他之前在自己的房间装了64个摄像头，似乎已经没必要使用疑问的语气了。

        深深吐出胸中的浊气，月重新闭上眼睛。L的监视，亦是一种保护……吗。

        这样的夜晚，还会持续多久呢……  """       
        show screen stats with dissolve
        stop music fadeout 1.0  
        play music "audio/daily.mp3" 

    if day == 7:
        stop music fadeout 2.0
        hide screen stats with dissolve
        window hide
        scene black with dissolve
        pause 1.0
        play music "audio/L_thinking.mp3" 
        scene L_sofa_2 with fade
        """ 黑暗的笼罩放大了声音。

        L已经习惯不分昼夜地工作，习惯唯一的光源是显示器的荧光管，习惯安静的室内只有敲打键盘、点击鼠标和机箱风扇工作的声音。

        只是最近晚上陪伴他的声音多了一种。

        夜神月的囚室会在规定的时间熄灯、开灯，模拟自然的日出日落，目的是维持囚犯的正常作息。

        有一种合理的刑讯逼供手段是把囚犯关在强光照射的狭小囚室里，强行剥夺囚犯的睡眠，睡眠不足会影响脑部供血，导致囚犯陷入焦躁、逻辑混乱，方便警察抓出囚犯口供的马脚。

        L确实已经没有什么需要审问夜神月的了，关于Kira的作案动机、作案手法、死亡笔记的规则应用，他全都一清二楚。

        所以他当然不会使用这种手段去干涉夜神月的睡眠，在日常对话中也没有讯问夜神月——这反而让年轻的Kira疑惑了。

        L对此只是饶有兴趣地看着褐发青年有些躁动的眼神，像是不安的小鼠抓挠笼门。

        L很清楚这种空虚的等待最能催磨人的意志力，这和当初夜神月主动要求被监禁不同，当时的夜神月抱着洗清嫌疑的目的，为了这个目的他可以咬牙坚持；

        但是换做失去记忆的夜神月，他失去了这个目的，精神便很快虚弱下来，态度也发生了极端的转变。

        L将夜神月从政府机构的手中夺过来，却并不希望对方保持着强韧的精神，或者被对方以为可以利用自己达到更多的目的。

        作为对手，他比任何人都清楚夜神月的危险性和强大的精神力。

        那是在他的监视下仍然能面不改色维持正常生活，同时使用死亡笔记进行杀人行为的世界级杀人犯。

        也许仅凭这一点，L就不想让夜神月轻易地死去。

        在解决了Kira案件之后，渡也为他找来一部分别的案件，数量比Kira出现前要少得多，犯罪率的下降确实让侦探濒临失业，但是更重要的是，L开始觉得无趣了。

        Kira案是他成为【L】之后遇见过的最危险也是最有趣的案件：第一次被逼迫着主动在他人面前露面，第一次主动亲身接触嫌疑人，对L来说都是相当新奇的体验。

        如果世界上有一件事比死亡更恐怖，那就是无聊。

        L痴迷于这种会让他肾上腺素上升的危险的游戏，赌上性命的游戏……然后令人遗憾的是，他对于“有趣”的阈值似乎被夜神月永久提高了一截。

        在感到无聊的时候，白天亦或是深夜，L就会这样咬着拇指注视着囚室的监控屏幕。这种眼神和孩子看着自己的拓麻歌子的眼神也许没有什么不同。

        安睡的青年正发出规律的呼吸声。

        那双眼神锐利的眼睛闭上之后，夜神月的脸呈现出他这个年纪的青年应该有的稚气和柔软，在日本他甚至还是个不能饮酒的孩子。

        L正在从日常和夜神月的互动中汲取乐趣。

        他并不是一个擅长照顾人的人，以他的自理能力能照顾好自己都算勉强，但是这是他最近新发现的娱乐活动。

        当你发现一个人的行为全部都由你支配，他的生存都要依赖你的时候，尤其这个人还是你昔日的宿敌……这种时候产生愉悦感也是正常的，不是吗？

        所以在渡担心L凡事都要亲力亲为会不会很快感到厌倦时，L反而表现出了超乎寻常的耐心。

        他乐此不疲地做着类似给月喂饭、帮月擦身，甚至包括在熄灯前给月盖上被子的事情。

        虽然夜神月一直强调可以帮他解开手铐，让他自己做这些事情，他也不会逃跑，但是L大多数时候并不会理会夜神月的请求。

        L享受着对夜神月一人的强权，将自己的意志凌驾于月的意志之上，然后在对方妥协后收割快感。

        他会这样一点点侵犯夜神月的边界，直到对方钝感到不会察觉不对，习惯了余生要和曾经的宿敌一起度过。

        因为这里是你无法逃离的、属于我的【箱庭】啊，月君。

        晚安。然后，明天见。 """        
        show screen stats with dissolve
        stop music fadeout 1.0  
        play music "audio/daily.mp3" 
    if sex_4:
        hide screen stats with dissolve
        scene room_2 with dissolve
        play music "audio/night.mp3" 
        """ 夜神月不知道自己睡了多久，激烈的性爱本就极大消耗了体力，迷迷糊糊中睁开眼睛，囚室内还没开灯，仍是一片黑暗。

        本想换个姿势继续睡的，月习惯性地翻身，用被子把自己裹得更紧，但是在牵拉肌肉时被一阵尖锐的酸痛感驱赶了睡意。 """

        Y yaoya"……嘶！"

        Y"（果然，白天做得太过头了……L那家伙。）"

        if unlock_the_handcuffs == False:

            Y surprise"（嗯？镣铐被解开了。）"

            """ 久违的自由让月忍不住又伸展了几下手脚，在狭窄的床铺上翻了几个身，找到一个舒服的位置才不动了。 """

        # 分歧点结束

        """一想到白天那场疯狂的性爱，月的小腿肚子就在打颤，心底冒出了一团火，烧得他浑身发燥。

        他从没考虑过自己为什么会在和L的性爱中失态成那个样子，直到被对方赤裸裸地点明。

        【夜神君在干性高潮上很有天赋呢。】

        一想到L的这句话，夜神月的浑身就打了个寒颤，拼命地想把这句话从脑内抹去。

        他惯常接受的夸奖是关于他在学习上的天赋，运动上的天赋，为人大方，乐于助人……

        他是父母眼中优秀的儿子，老师眼中优秀的学生，未来要进入警界发光发亮的警视厅新星——绝不是某人的禁脔。

        是L和药物的错，就是这样的。

        自己不是见过照片和视频吗，在毒品的控制下人会暴露出什么丑态，只是通过自己没有戒断反应来看，L应该还没有给他注射毒品。

        那应该只是烈性的催情药，通常是那些性功能障碍者使用的药物。

        但是……身为男性，在使用催情药之后，前列腺也会有快感吗？

        这里涉及到夜神月的知识盲区了，对于性少数群体他本就没有过多关注，此刻思维停滞，无法再更进一步。

        比起这个，世界的王牌侦探【L】竟然是同性恋者……说出去会掀起惊天大浪吧。

        更糟糕的是，【L】对【Kira】拥有性欲这件事……

        真是完全搞不明白，L的想法。

        如果说在对弈时，夜神月还能通过两人都渴望获胜的心理去推断L的棋路；那么在感情这种暧昧不清的东西上，以他对L的了解，就完全不足以支撑起推理的前提。

        在搜查四叶集团时，即使和L同吃同睡，他也依然难以猜测对方内心深处的想法。

        该不会，从那时起L就……月的心里冒出一阵恶寒，自己当时在L面前毫无防备洗澡睡觉的样子，不会成为对方的意淫素材吧？！

        想到这里，月的胳膊和后背上起了一层鸡皮疙瘩，过了十几秒才缓过来。

        至少，当时L表现出来的像是无性恋的样子，并没有什么异常……谁知道他是在装模作样还是怎样。

        深呼吸了几口气，月面前压下烦躁的心绪和对未来的不安。

        总之……先好好活下去，然后……找机会逃走吧。

        他绝对无法接受，被当做性玩具度过余生。 """
        $ sex_4 = False
        $ bad_end = True
        show screen stats with dissolve
        stop music fadeout 1.0  
        play music "audio/daily.mp3" 
    # 显示状态变化
    sy"""一天结束了……"""

    if unlock_the_handcuffs:
        if affection >= 60:
            scene main bg_4 with fade
            $ persistent.unlock_3 = True
        else:
            scene main bg_3 with fade
            $ persistent.unlock_2 = True
    else:  
        if affection >= 60:
            scene main bg_2 with fade
            $ persistent.unlock_1 = True
        else:
            scene main bg_1 with fade
    
    sy"""今天是第 [day] 天。

    你恢复了 [action_points] 点行动点数。

    饱食度自然下降，当前饱食度: [satiety]/100

    清洁度自然下降，当前清洁度: [clean]/100

    """

    
    # 健康值变化提示

    if satiety <= 50:
        """ 月看起来已经挨饿了有一段时间了，他的脸颊消瘦下去，整个人显得无精打采。

        也许该给他喂食了，否则可能会生病。 """        


    if satiety_penalty > 0:
        if satiety <= 0:
            sy"由于月极度饥饿，健康值下降30点"
        else:
            sy"由于月很饥饿，健康值下降10点"

    if clean <= 40:
        """ 月偶尔会做出一些奇怪的举动，像野生动物磨蹭树皮一样在墙上摩擦自己的皮肤，L反应过来那是为了缓解身体某处的瘙痒

        ——毕竟你已经很久没有给他做清洁了。

        他原本柔顺而富有光泽的头发变成了一缕一缕紧贴在头皮上，浑身散发着油脂发臭的气味。

        也许该给他洗澡了，否则可能会生病。 """        

    if clean_penalty > 0:
        if clean <= 0:
            sy"由于月的卫生状态糟糕，健康值下降30点"
        else:
            sy"由于月的卫生状况差，健康值下降10点"

    if stress > 70:
        """ 月在囚室中表现得有些奇怪，他在醒着的时候有时会焦躁地一直改变姿势，但是无论如何都找不到让自己舒适的那个；

        有时候他会忍受不了一般冲监控摄像头喊话，可发泄情绪依然不能平息他的烦躁；

        有时候他会嘴唇蠕动着自言自语，L从唇语中读出的是

        {color=#f00}“杀了我杀了我杀了我杀了我杀了我……”{/color}

        月看起来精神不太安定，是不是压力太大了？ """

    if stress_penalty > 0:
        if stress >= 90:
            sy"由于月精神崩溃，健康值下降20点"
        else:
            sy"由于月精神状态不佳，健康值下降10点"

    if health <= 40:
        """ L注视监控屏幕时发现月在床上蜷缩成一团，双眼紧闭着，脸色苍白，表情有些痛苦，时不时低声咳嗽着。

        月看起来已经生病了，需要尽快吃药。 """    

    if Light_flower:

        $ flower_days = max(0,flower_days-1)

        if flower_tixing:
            if flower_days == 1:

                $ Light_flower = False

                "月囚室里的鲜花有些蔫了。L把蔫了的鲜花收走了，也许该送点新的鲜花了。"
                $ flower_tixing = False

    if Light_cookie:

        $ cookie_days = max(0,cookie_days-1)

        if cookie_tixing:
            if cookie_days == 1:

                $ Light_cookie = False

                "月好像已经把铁盒里的曲奇吃完了——当然，只是他喜欢的那几个口味。要不要再送点新的呢？"
                $ cookie_tixing = False


    if day == 7:
        sy"""月的礼物商店里开放了【解开镣铐】的兑换选项，有空去看看吧~

        L和月的关系可以更进一步发展了，有空去试试【外出】选项吧~

        注意，以上两个新功能都需要一定的好感度才能进行哦！

        外出需要消耗2点行动点数和大量体力，请合理安排~
        
        """

    if Light_newspaper:
        jump newspaper

    if day == 5:
        L"（最近只是读书好像已经不能满足夜神君了，真是容易感到无聊的人。）"

        L"（今天要不要带国际象棋去和夜神君一起玩呢……）"

        sy"解锁了新的娱乐-下棋。请有空去游玩一下吧！"

    if day == 8:
        L"（和夜神君看书和对弈的时光总是很愉快，要不要试试新的游戏呢……）"

        L"（比如说纸牌什么的？）"

        sy"解锁了新的娱乐-玩21点。请有空去游玩一下吧！"

    if affection <= 40:
        "当L站到囚室门口时，月用冷漠的眼神瞥了他一眼。"
    elif affection <= 60:
        "当L站到囚室门口时，月平静地注视过去。"
    elif affection <= 70:
        "当L站到囚室门口时，月的脸露出了微笑。"
    else:
        "当L站到囚室门口时，月看起来很开心，他琥珀色的眼睛蕴含着喜悦的光芒。" 
    $ Y_room = True
    jump action_menu


default random_newspaper = [] 

label newspaper:

    """ L在监视屏幕上看见夜神月正拿起白天送过去的报纸阅读，神情晦暗不明。

    月先是仔细检查了报纸的日期、排版、使用的油墨和纸质，并不排除L会给他假报纸的可能性，只是这点不能在L面前表露出来。

    L有一定概率会在监控中发现他的行为，但是比起摄像头，还是L本人的压迫感会更重。

    在确认了报纸的真实性之后，月开始仔细阅读每一个板块，重点阅读社会版与国际新闻版，试图寻找【L】与【Kira】相关的新闻，还有——

    是否有新的罪犯离奇死亡（心脏麻痹）的新闻报道？

    是否有新的死神往人间界丢入了死亡笔记？

    夜神月深呼吸了一口气，安抚住躁动的心跳，沉下目光搜索有用的信息。 """

    if not random_newspaper:
        # 用 random.sample() 从列表中随机选择所有元素（不重复）
        $ random_newspaper = random.sample(["newspaper1", "newspaper2", "newspaper3"], 3)
    # 从随机列表中取第一个元素播放，然后删除它（避免重复）
    $ current_newspaper = random_newspaper.pop(0)
    jump expression current_newspaper   

label newspaper1:
    """ 与之前他作为Kira活动的时候相比，大大小小的犯罪报道昭示着人性的罪恶重现于这个世界上。

    原本已经停止腐化、慢慢变好的世界重新回到了夜神月捡到死亡笔记之前，不，因为反弹心理甚至更加恶劣了。

    各国政府疲于应对向Kira挑衅而犯下罪行的犯罪者，对此民众的舆论褒贬不一。可惜，L给予的报纸里并没有更详细的内容。

    但是夜神月相信，在网络上，匿名论坛里，一定有大量的人祈祷着Kira的回归。 """

    Y angry"（可恶……就差一点，赢的就应该是我了。）"

    Y pt"（这样下去，很快Kira的存在就会被淡忘吧。）"

    Y"（究竟还有没有能再次夺回Kira身份的一天呢……）"
    jump after_newspaper

label newspaper2:
    """ 在报纸上，夜神月看见了各国媒体对于L的称赞：

    【L无愧于世界第一侦探之名，即便是能够隔空杀人的Kira连环杀人案件，在L出马之后也被轻而易举地解决了。】

    【L拯救了世界，终结了Kira的暴政！】

    【世界需要L，正义必胜！】

    当然还有一些媒体为了夺人眼球编写的阴谋论：【Kira的真身在日本，这背后的黑幕是……】 """

    Y"（全都是一些无聊的发言……L这家伙给我看这个是想干什么，羞辱我吗？无聊。）"
    jump after_newspaper

label newspaper3:
    """ 报纸上的新闻平平无奇，政府又推出了什么利民政策，又有黑心企业被曝光了，哪里发生了意外事故，哪个明星又爆出了绯闻……

    世界回归到原本的样子：平静、繁荣、有人在哭、有人在笑、一部分世界在腐朽、一部分世界欣欣向荣。

    而这一切已经和夜神月，和Kira无关了。

    Kira事件就像一道愈合的伤口，在疤痕脱落后便无人关心。 """

    Y"（你想表达什么呢，L？）"

    Y"（我的理想只是空中楼阁，在现实面前的一道泡影吗？无论我做什么都是白费力气吗？）"

    Y"（如果觉得这样就可以让我认输，那你也未免太小瞧我了。）"
    jump after_newspaper

label after_newspaper:

    """ 监控屏幕中月合上了报纸，结束了今天的阅读。

    L从月的表情中看不出喜怒，对方本就是善于隐藏自己情绪的性格，所以他也不是很意外。

    下次用其他方法继续试探夜神月好了。只有这个游戏，他怎么也玩不腻。 """  

    if unlock_the_handcuffs:
        if affection >= 60:
            scene main bg_4 with fade
            $ persistent.unlock_3 = True
        else:
            scene main bg_3 with fade
            $ persistent.unlock_2 = True

    else:  
        if affection >= 60:
            scene main bg_2 with fade
            $ persistent.unlock_1 = True
        else:
            scene main bg_1 with fade

    if affection <= 40:
        "当L站到囚室门口时，月用冷漠的眼神瞥了他一眼。"
    elif affection <= 60:
        "当L站到囚室门口时，月平静地注视过去。"
    elif affection <= 70:
        "当L站到囚室门口时，月的脸露出了微笑。"
    else:
        "当L站到囚室门口时，月看起来很开心，他琥珀色的眼睛蕴含着喜悦的光芒。" 

    # 报纸事件结束 
    $ Light_newspaper = False
    $ Y_room = True
    jump action_menu



label normal_end_staff:

    hide screen stats
    scene black
    play music "audio/Clair de Lune_title.mp3"

    nvl clear
    nvl show dissolve

    nvlpb""" staff名单

    原作：《DEATH NOTE》

    文案：东郊街的猫饼,西城区的猫球（负责豪华喂食和外出文案）

    美术：中心区的烙略，Keshi

    程序：北郊区的猫条

    UI：南城区的猫糕

    {clear}

    图片素材：

    自己拍摄的照片、{a=https://www.pexels.com}pexels{/a}

    音乐：

    Clair de Lune - Claude Debussy

    Funeral March - Frédéric Chopin

    {a=https://maou.audio/}魔王魂{/a}

    DOVA-SYNDROME

    音效：ZAPSPLAT、{a=https://freesound.org/}freesound{/a}、{a=https://taira-komori.net/freesoundcn.html}小森平的免费下载音效{/a}

    {clear}

    英文翻译：Keshi，naynay，费醌，易弦，阿渔，罗森，杜衡，Saric，川原汐泉，水芹王，powder

    日文翻译：カタリテ，西城区的猫球，くぎ，ミチ，千春叶子，灯

    泰文翻译：Keshi

    特别感谢 测试人员：江桐，苦茶，逍遥文游，Eukigrieo，杜衡，唐沐夏轩，2&7，白琊
    """

    nvl clear

    nvlmb"""你好，这里是东郊街的猫饼，是《箱庭》的主策划，并且负责主要文案的写作

    衷心感谢你游玩本游戏，希望你能够在游玩的过程中体会到一丝乐趣~

    欢迎给我留下反馈，无论是bug，游玩体验，想吐槽的内容全都可以！
    
    谢谢大小老师创作出DN这部作品，荣耀属于原作，ooc属于我XD

    ——以下是个人大篇幅碎碎念——"""

    nvl clear

    nvlmb"""感谢您游玩了《箱庭》的 Normal End！

    本结局的文案分工为：我负责撰写夜神月回到L所在的酒店时的剧情，猫球老师负责撰写其余的所有剧情。

    走到这里算是平稳落地了呢，可喜可贺，可喜可贺~

    原本NE中预计有一段月穿着dk制服和L玩师生play的惩罚性爱，但是因为工期限制被我们砍掉了（目移）

    不过后面想想这样也挺好，这样大家才更有动力去攻略HE和BE嘛（笑）

    如果您还没有玩过HE,BE和TE，我强烈推荐您进行游玩！相关攻略和TE的剧情就在标题页面的“额外内容”中。"""

    nvl clear

    nvlmq"""这次试着在ne的结尾部分写了一点关于月初心的想法，如果月真的成为了L的助手，想必他们两位一定会呈现出完全不一样的办案风格。

    在Kira消失后的日子，世界会变得怎么样呢？我想或许会迎来一段相当杂乱无序的时光，犯罪率会反扑，罪犯们会把积压的恐惧倾泻到普通的群众身上。

    月还有着独属于他的少年心气，他不会坐以待毙、而是借助了L现有的资源优势，用另一种方式去执行他的正义。

    在 Normal End 里L默许了这种行为，两人之间的关系更加微妙，不管是L、还是月，都没能完全探明自己的心意，他们还需要更长的时间。"""
    nvl clear

    nvlmb"""结局的写作花费了比我们预计更多的心血，我们全体工作室成员希望您有在游玩中感受到L月的魅力！

    在此po出我的ao3主页：{a=https://archiveofourown.org/users/Delandour/works}https://archiveofourown.org/users/Delandour/works{/a}（需要科学上网）
    
    宣传一下目前我还在写的作品《Killer》，对犯罪心理学者L x 连环杀人犯&警视月感兴趣的可以去我主页看看哦~ 
    
    有生之年希望能把《Killer》也做成游戏呢~
    
    感谢你看到这里，之后有缘再见（挥手）
    
    """

    nvl hide dissolve

    $ renpy.set_return_stack(())
    return  
  
label happy_end_stuff:
    hide screen stats
    scene black
    play music "audio/Clair de Lune_title.mp3"

    nvl clear
    nvl show dissolve

    nvlpb""" staff名单

    原作：《DEATH NOTE》

    文案：东郊街的猫饼,西城区的猫球（负责豪华喂食和外出文案）

    美术：中心区的烙略，Keshi

    程序：北郊区的猫条

    UI：南城区的猫糕

    {clear}

    图片素材：

    自己拍摄的照片、{a=https://www.pexels.com}pexels{/a}

    音乐：

    Clair de Lune - Claude Debussy

    Funeral March - Frédéric Chopin

    {a=https://maou.audio/}魔王魂{/a}

    DOVA-SYNDROME

    音效：ZAPSPLAT、{a=https://freesound.org/}freesound{/a}、{a=https://taira-komori.net/freesoundcn.html}小森平的免费下载音效{/a}

    {clear}

    英文翻译：Keshi，naynay，费醌，易弦，阿渔，罗森，杜衡，Saric，川原汐泉，水芹王，powder

    日文翻译：カタリテ，西城区的猫球，くぎ，ミチ，千春叶子，灯

    泰文翻译：Keshi

    特别感谢 测试人员：江桐，苦茶，逍遥文游，Eukigrieo，杜衡，唐沐夏轩，2&7，白琊
    """

    nvl clear

    nvlmb"""你好，这里是东郊街的猫饼，是《箱庭》的主策划，并且负责主要文案的写作

    衷心感谢你游玩本游戏，希望你能够在游玩的过程中体会到一丝乐趣~

    欢迎给我留下反馈，无论是bug，游玩体验，想吐槽的内容全都可以！
    
    谢谢大小老师创作出DN这部作品，荣耀属于原作，ooc属于我XD

    ——以下是个人大篇幅碎碎念——"""
    nvl clear

    nvlmq"""感谢您游玩了《箱庭》的 Happy End！
    本结局的文案分工为：猫饼老师负责撰写告白的前半部分，我负责撰写其余的所有剧情。

    今年已经是我在L月的第三年了，不过因为现实生活繁忙，「箱庭」应该是我第一次投入这么多精力和时间为这对CP创作故事。

    应该有不少人都有想过L活下来，死亡笔记这部作品的走向会如何改变吧？我也是其中的一员。
    
    第二部中的月看上去似乎很寂寞……他失去了唯一一个和自己平等的对象，总是会幻视到逝去的L的幻影。

    在加入「箱庭」的制作工作之前，我曾经和朋友聊过要如何才能在不扭曲角色性格的情况下，去找到属于L和月的Happy End，答案是非常困难、这几乎是不可能的。

    毕竟只要死亡笔记还存在一天，他与L的对峙就是命中注定，会互相角逐、厮杀，直到一方殒命为止。

    但是，如果L对自己的宿敌拥有别样的情愫呢？如果将无法改变世界、注定失败的结局提前告知月呢？

    {clear}

    Happy End 便是融合了这两点的产物，在满足L私欲的情况下、如何小心地不折损月的傲骨———让他们尽可能贴近普世意义上的「幸福」的故事。

    如果你在游玩过程中，有被豪华喂食的美味佳肴馋到过，有为外出活动的剧情感动过，或者十分享受游玩Happy End的过程，我的目标也就达成了。

    「箱庭」不会是 Neko Alliance 的终点，相信我们在不远的未来、还会和大家在另一部L月同人游戏里相遇吧。
    
    如果您还没有玩过BE和TE，我强烈推荐您进行游玩！相关攻略和TE的剧情就在标题页面的“额外内容”中。
    """

    nvl clear

    nvlmb"""结局的写作花费了比我们预计更多的心血，我们全体工作室成员希望您有在游玩中感受到L月的魅力！

    在此po出我的ao3主页：{a=https://archiveofourown.org/users/Delandour/works}https://archiveofourown.org/users/Delandour/works{/a}（需要科学上网）
    
    宣传一下目前我还在写的作品《Killer》，对犯罪心理学者L x 连环杀人犯&警视月感兴趣的可以去我主页看看哦~ 
    
    有生之年希望能把《Killer》也做成游戏呢~
    
    感谢你看到这里，之后有缘再见（挥手）
    
    """

    nvl hide dissolve

    $ renpy.set_return_stack(())
    return  

label bad_end_stuff:
    hide screen stats
    scene black
    play music "audio/Clair de Lune_title.mp3"

    nvl clear
    nvl show dissolve

    nvlpb""" staff名单

    原作：《DEATH NOTE》

    文案：东郊街的猫饼,西城区的猫球（负责豪华喂食和外出文案）

    美术：中心区的烙略，Keshi

    程序：北郊区的猫条

    UI：南城区的猫糕

    {clear}

    图片素材：

    自己拍摄的照片、{a=https://www.pexels.com}pexels{/a}

    音乐：

    Clair de Lune - Claude Debussy

    Funeral March - Frédéric Chopin

    {a=https://maou.audio/}魔王魂{/a}

    DOVA-SYNDROME

    音效：ZAPSPLAT、{a=https://freesound.org/}freesound{/a}、{a=https://taira-komori.net/freesoundcn.html}小森平的免费下载音效{/a}

    {clear}

    英文翻译：Keshi，naynay，费醌，易弦，阿渔，罗森，杜衡，Saric，川原汐泉，水芹王，powder

    日文翻译：カタリテ，西城区的猫球，くぎ，ミチ，千春叶子，灯

    泰文翻译：Keshi

    特别感谢 测试人员：江桐，苦茶，逍遥文游，Eukigrieo，杜衡，唐沐夏轩，2&7，白琊
    """

    nvl clear

    nvlmb"""你好，这里是东郊街的猫饼，是《箱庭》的主策划，并且负责主要文案的写作

    衷心感谢你游玩本游戏，希望你能够在游玩的过程中体会到一丝乐趣~

    欢迎给我留下反馈，无论是bug，游玩体验，想吐槽的内容全都可以！
    
    谢谢大小老师创作出DN这部作品，荣耀属于原作，ooc属于我XD

    ——以下是个人大篇幅碎碎念——"""

    nvl clear

    nvlmb"""感谢您游玩了《箱庭》的 Bad End！

    本结局文案分工为：猫球老师负责撰写夜神月利用交通网络和L进行智斗的剧情，我负责撰写智斗中的L视角和夜神月登上新干线之后的剧情。

    实话实说，智斗部分消耗了相当多的脑细胞呢……

    而且为了测试真实性和实地取景，我和猫球老师也确实前往了东京站和京桥站踩点，所以出现了空镜中路人的服饰不太符合剧情中季节的情况……请多包涵！（鞠躬）

    至于纯白牢房的情节，则完全是个人的性癖大爆发了（笑）

    我个人非常喜欢月被逼迫着承认自己讨厌L，以及之后向欲望屈服的情节。

    月被迫在L面前袒露了全部的真实，他并非完美的神子，而是拥有欲望的人类……所以他永远无法成为神。

    如果您还没有玩过HE和TE，我强烈推荐您进行游玩！相关攻略和TE的剧情就在标题页面的“额外内容”中。"""

    nvl clear

    nvlmb"""结局的写作花费了比我们预计更多的心血，我们全体工作室成员希望您有在游玩中感受到L月的魅力！

    在此po出我的ao3主页：{a=https://archiveofourown.org/users/Delandour/works}https://archiveofourown.org/users/Delandour/works{/a}（需要科学上网）
    
    宣传一下目前我还在写的作品《Killer》，对犯罪心理学者L x 连环杀人犯&警视月感兴趣的可以去我主页看看哦~ 
    
    有生之年希望能把《Killer》也做成游戏呢~
    
    感谢你看到这里，之后有缘再见（挥手）
    
    """

    nvl hide dissolve

    $ renpy.set_return_stack(())
    return  

label true_end_stuff:
    hide screen stats
    scene black
    play music "audio/Clair de Lune_title.mp3"

    nvl clear
    nvl show dissolve

    nvlpb""" staff名单

    原作：《DEATH NOTE》

    文案：东郊街的猫饼,西城区的猫球（负责豪华喂食和外出文案）

    美术：中心区的烙略，Keshi

    程序：北郊区的猫条

    UI：南城区的猫糕

    {clear}

    图片素材：

    自己拍摄的照片、{a=https://www.pexels.com}pexels{/a}

    音乐：

    Clair de Lune - Claude Debussy

    Funeral March - Frédéric Chopin

    {a=https://maou.audio/}魔王魂{/a}

    DOVA-SYNDROME

    音效：ZAPSPLAT、{a=https://freesound.org/}freesound{/a}、{a=https://taira-komori.net/freesoundcn.html}小森平的免费下载音效{/a}

    {clear}

    英文翻译：Keshi，naynay，费醌，易弦，阿渔，罗森，杜衡，Saric，川原汐泉，水芹王，powder

    日文翻译：カタリテ，西城区的猫球，くぎ，ミチ，千春叶子，灯

    泰文翻译：Keshi

    特别感谢 测试人员：江桐，苦茶，逍遥文游，Eukigrieo，杜衡，唐沐夏轩，2&7，白琊
    """

    nvl clear

    nvlmb"""你好，这里是东郊街的猫饼，是《箱庭》的主策划，并且负责主要文案的写作

    衷心感谢你游玩本游戏，希望你能够在游玩的过程中体会到一丝乐趣~

    欢迎给我留下反馈，无论是bug，游玩体验，想吐槽的内容全都可以！
    
    谢谢大小老师创作出DN这部作品，荣耀属于原作，ooc属于我XD

    ——以下是个人大篇幅碎碎念——"""

    nvl clear


    nvlmb"""感谢您游玩了《箱庭》的 True End！

    本结局的文案全部由我撰写。

    TE最初的故事设计其实要更加悲伤，前半段和现在的剧情是一样的，但是在初稿中，月真的死于死刑，
    
    L在月死后才意识到了自己的感情，于脑内构筑了箱庭世界，妄想着如果月存活下来的发展……

    《箱庭》的名称由来是心理学名词“箱庭疗法”，通过在沙箱中制作庭院来投射人的心理活动，将人的无意识/潜意识整合并且具现化。

    L将在一生中无数次摆放着代表月的模型棋子，在一遍一遍的箱庭推演中逐渐明白自己对月的心意，但是现实里的月已经死亡，月将永远存活在他脑内的箱庭中。"""
    nvl clear

    nvlmb"""因为这个结局太过于致郁，被HE爱好者的猫球老师否决了呢qwq
    
    猫球老师坚信L会想办法真的让月存活下来，提出了现在TE计谋部分的雏形，最终我们两人完善了整个剧情框架，由我负责书写。"""

    nvlmq"""
    随着箱庭体量的增长，原先设定的 True End 感觉越来越不适合现在的故事了……
    
    毕竟如果遵照原初的想法，L将会在脑海中构建出一个过于庞大、甚至有些失真的悲哀世界。

    所以在一番思考下，最后将 True End 设定成了“一切结局背后的真相” 。

    是一个有些紧张刺激，却能让人十分享受的故事呢。

    """

    nvlmb"原本《箱庭》的文本量想控制在10w字左右的，现在则是达到了远远超过的20w字左右……真是恐怖的文本量呢（倒下）"
    nvl clear

    nvlmb"""结局的写作花费了比我们预计更多的心血，我们全体工作室成员希望您有在游玩中感受到L月的魅力！

    在此po出我的ao3主页：{a=https://archiveofourown.org/users/Delandour/works}https://archiveofourown.org/users/Delandour/works{/a}（需要科学上网）
    
    宣传一下目前我还在写的作品《Killer》，对犯罪心理学者L x 连环杀人犯&警视月感兴趣的可以去我主页看看哦~ 
    
    有生之年希望能把《Killer》也做成游戏呢~
    
    感谢你看到这里，之后有缘再见（挥手）
    
    """

    nvl hide dissolve

    $ renpy.set_return_stack(())
    return  




label dead_end:
    hide screen stats
    scene black

    play music "audio/Funeral March_bad end1.mp3"

    scene L_sofa with dissolve

    pb""" 面对昔日的仇敌，平分秋色的对手，L看着现在被关押在囚室中任人宰割的青年，突然感到兴意阑珊。

    他对待夜神月就像对待无数个被抛弃的玩具一样，在最初的新奇感褪去之后，将对方扔至杂物箱中。

    就像被遗忘的电子宠物一般，关上监控屏幕，也就切断了联系，等到再想起时，只余一具冰冷腐烂的尸体。

    只是电子宠物在游戏厂商的设计下还可以复活，但是现实世界的人类不行。

    L突然有些烦躁。

    他没有养过宠物，对养成类的游戏也不感兴趣，脑海中的确有养宠物的基础知识：喂食、清洁、适当的娱乐……

    但是当理论变为现实，陌生的负面情绪依然让他无所适从。

    渡知道夜神月的存在，也多次欲言又止地看着他，只不过一切都是他的游戏，他的决策，所以没有插手。

    L不愿意去想象夜神月死前经受着怎样的折磨，可能已经饿得烧心，灌饮自来水来抵抗饥饿感，啃食能入口和不能入口的，甚至是自己的血肉；

    可能由于压力过大产生了自杀倾向，暴力地挣扎手铐直到骨折，或是用头一遍又一遍地撞击墙壁，直到鲜血淋漓；

    可能某天突然发起高烧，免疫系统崩溃，高热杀死了病菌也杀死了生命本身，青年在病痛的折磨下陷入沉眠，意识归于黑暗……

    也可能，这些夜神月都经历过。

    L有些不愿意面对月的尸体，他只是出于恶趣味或者刻意的忽略弄坏了一个玩具，但是并不想背负上一些沉重的东西。

    但是渡平静地看着L的眼睛，跟他说，我现在要去收敛夜神月的尸体，L，你跟我来。

    L没有拒绝，也没有说话，只是默默地跟随在渡的后面。

    自从他成为“L”之后，一直是渡跟在他的后面，这次的路程让L感到陌生、漫长、甚至有些畏惧。

    他不是没有接触过尸体，但是那些尸体的因果并不在他身上，他只是侦探，作为旁观者堪清真相。

    电梯把他们送入地下，这条路L走过很多次，只是第一次怀着这样的心情，连脚步声都变得沉重刺耳，回荡在空旷的地下。"""

    scene room_1 with dissolve

    """

    还没到囚室，L已经闻到尸胺独有的臭味，他又想逃避了，只是按捺住这种冲动，强迫自己冷静下来。

    走到囚室门口，渡掏出钥匙打开了格栅门，金属门发出吱呀的声音，露出夜神月倒在地上的身影。

    L匆匆扫了两眼，已经没办法把这具开始肿胀腐烂的尸体和记忆中的夜神月联系到一起，无论是颜色、气味、还是那双充满恶意的浑浊眼珠。

    已是死不瞑目。

    尸体被装进收尸袋中，然后放上推车，最后会由专门的车辆运送到墓园，下葬立碑。"""

    scene dead_end with dissolve

    """

    L全程没说几句话，虽然他平时在和警方交流之外也不是话多的性子，但是渡能感觉到L的低气压。

    在这种时候，渡觉得L还很孩子气。

    面对由自己导致的死亡，会感到茫然、逃避、愧疚、抑郁，这些都是初次经历者正常的情感反应。

    在这方面，渡也不希望L会有更多的经验。

    L需要学习对生命和死亡保持敬畏。


    葬礼的仪式从简，牧师在墓前诵念《圣经》：

    The Lord is my shepherd, I lack nothing. （耶和华是我的牧者，我必一无所缺。）

    He makes me lie down in green pastures, he leads me beside quiet waters, he refreshes my soul. （他让我躺卧在青草地上，领我到幽静的溪水旁。）

    He guides me along the right paths for his name's sake. （他使我的心灵苏醒，为了自己的名引导我走正路。）

    Even though I walk through the darkest valley, I will fear no evil, for you are with me…（我纵使走过死亡的幽谷，也不怕遭害，因为你与我同在……）

    葬礼当天的天气很凉爽，天色发白，看不见太阳，亦没有浓重的乌云。

    L听着牧师的诵念声发呆，他的目光停留在新做的墓碑上，上面写着：

    【The only puzzle I couldn't solve.】（终局无解）\n
    【Light】\n
    【1986-2004】

    【Game Over. No Rematch.】（对局终止 再无重赛） """
    $ persistent.unlock_dead_end = True

    # 1. 画面渐暗（1秒内变黑，无停留，不淡入新画面）
    with Fade(1.0, 1.0, 0.0, color="#000")  # out_time=1秒（变黑），hold=0，in_time=0

    # 无论是否保存，最终都跳转到标题界面
    $ renpy.set_return_stack(())
    return


