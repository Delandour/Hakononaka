
default fondle_points = 0  # fondle次数计数器（全局）
default fondle2_points = 0 #当天fondle次数（每日重置）
default random_fondle = []

# 预定义fondle次数到标签的映射
init python:
    import random


label sex_fondle:
    play music "pink action.mp3"
    $ Y_room = False
    if health <= 40:
        "夜神月看起来身体不适，需要尽快喂食药物。"
        menu:
            "需要返回行动菜单吗？"
            "返回":
                sy"不消耗行动点数，你还剩下[action_points]点行动点数。"
                $ Y_room = True
                jump action_menu

            "继续行动":
                if stamina < 20:
                    "夜神月看起来很疲惫，今天先让他休息吧。"
                    sy"不消耗行动点数，你还剩下[action_points]点行动点数。"
                    $ Y_room = True
                    jump action_menu

                if fondle2_points >= 1:
                    "这种事情一天做一次就好了。"
                    "去做点别的事情吧。"
                    sy"你还剩下[action_points]点行动点数。"
                    $ Y_room = True
                    jump action_menu

                $ fondle_points += 1  # 总fondle次数+1
                $ stamina -= 20

                jump handle_fondle



    if stamina < 20:
        "夜神月看起来很疲惫，今天先让他休息吧。"
        sy"不消耗行动点数，你还剩下[action_points]点行动点数。"
        $ Y_room = True
        jump action_menu


    if fondle2_points >= 1:
        "这种事情一天做一次就好了。"
        "去做点别的事情吧。"
        sy"你还剩下[action_points]点行动点数。"
        $ Y_room = True
        jump action_menu

    $ fondle_points += 1  # 总fondle次数+1
    $ fondle2_points += 1 
    $ stamina -= 20
    jump handle_fondle

label handle_fondle:

    if fondle_points == 1:
        jump fondle1
    else:
        if not random_fondle:
            if unlock_the_handcuffs:
                $ random_fondle = random.sample(["fondle1","fondle2","fondle3","fondle5"],4)
            else:
                $ random_fondle = random.sample(["fondle1","fondle2","fondle3","fondle4","fondle5"],5)
        $ current_fondle = random_fondle.pop(0)
        jump expression current_fondle

label fondle1:

    "L打开囚室的门，月正坐在床上看着某一点发呆，听见动静看了L一眼，又移开了视线。"

    show fondle_yao at jubu with dissolve

    "L径直走上前，伸手轻松撩起月的上衣一摆，把手掌贴在了对方劲瘦的腰侧，收获了意料之中的反射性一颤。"

    #voice "voice/light/Y_chuan1.mp3"

    Y jiaoji1"你在干什么？龙崎！"

    L"按理来说夜神君现在是我的私人财产，所以我想对他做什么都可以。"

    Y"你不要欺人太甚了！！"

    """青年因为手脚受缚，只能腰部发力试图用头和肩膀把L撞开，但是因为平衡性太差轻易地就被推倒在床上。
    
    衣服的下摆因为受力被掀起了一截，反而暴露出了更多白皙的肌肤。

    L伸出食指在月的肚脐处画了个圈，看见对方腹部的肌肉猛地一缩，青年的目光已经凶狠得要吃人一般了。"""

    Y jiaoji2"……龙崎！"

    L"夜神君准备在这种不利的条件下反抗我吗？"

    #voice "voice/light/Y_zhe jia huo.mp3"

    Y angry"你这混蛋……"

    L"如果夜神君是识时务的人，就应该搞清楚自己的位置。放心，我今天没打算对你做什么。"

    hide fondle_yao with dissolve

    "L离开了，留下月躺在床上，呼吸中都透露着怒意。"

    $ stress = min(100, stress + 5)
    jump after_fondle

label fondle2:

    if satiety < 60:

        """L再次进入囚室的时候，月仍然是躺在床上背对着他的姿势，只是双腿蜷缩了起来。

        可能是因为饥饿吧，毕竟这两天摄入的食物很少，L猜测。"""

        L"夜神君，醒着吗？"

        """月没有反应。

        L探身去看，月好像察觉到了他的视线，不耐烦地睁开眼睛，翻过身来。"""



    Y"你又来干什么？"

    L"夜神君，其实我很会做足底按摩。"

    #voice "voice/light/Y_chuan1.mp3"

    Y jiaoji2"哈？你跟我说这个干什么？……喂你不要乱摸！"

    show fondle_jiao at jubu with dissolve

    """L坐在床边，抓住了月的脚放在自己的膝头。

    青年的脚和他的身体一样，完美得像一件艺术品一般，因为瘦削，青色的静脉血管很明显，如同白玉上的墨线。
    
    指甲有些稍长了，不过能看得出之前修剪整齐，透出樱花一样的淡粉色。唯一美中不足的是脚腕因为镣铐摩擦留下的红痕。

    L的手指捏上了月的足心，让青年发出了一声猝不及防的闷哼，浑身一颤。"""

    L smile2"夜神君的脚果然很敏感呢。"

    Y"你是变态吗！快放开！！"

    """月挣扎了起来，L置若罔闻，左臂压住了对方不断动弹的小腿，右手依然把对方的赤足捏在掌中。

    也许是因为长时间不运动血液循环不通，月的脚是冰凉的，握在手里就真的如同软玉一般。"""

    L"考虑到夜神君这样躺久了会脚麻，我也是好心帮忙呢。"

    Y"我不需要这种帮忙！你能不能滚啊！！"

    L smile1"仔细看看夜神君的脚也是精致得如同艺术品一般呢。"

    "月倒吸一口冷气，浑身起满了鸡皮疙瘩。"

    Y yaoya"龙崎，你能不能正常一点！我承认你成功恶心到我了！！"

    L pt"哪里，我明明是实话实说。"

    """L面无表情地又挠了一下月的脚心。

    月被这股痒意逼得抠紧了脚趾，只能暂退一步。"""

    Y"……我知道了，谢谢你的好意，你按摩完就快走。"

    """L一边把玩月的脚，捏捏脚趾、脚掌或脚心，一边饶有兴趣地观察月的表情，
    
    在月忍不住要爆发的时候结束了这次的“按摩”，在月想杀人的注目礼下离开了。"""

    hide fondle_jiao with dissolve

    $ stress = min(100, stress + 5)
    jump after_fondle

label fondle3:

    """L再次进入囚室的时候，月正侧躺在床上，似乎已经睡着了。

    L蹲坐在了床边上，月也没有醒来的迹象。看来睡得很熟呢。

    如果捉弄一下，月会醒来吗？L突然好奇地想到。"""

    show fondle_rt1 at jubu with dissolve


    """

    L把手掌覆在了月的前胸上，掌下传来心脏规律的跳动。

    然后他移动手掌，蹭到了一个凸起。是夜神君的乳头吧。L想。

    他用手指隔着衣服拨弄按压起了那个小小的凸起，很快感到手指下原本柔软的乳头开始因为受到刺激充血挺立起来。
    
    现在即使拿开手指，也能在衣服上观察到非常明显的凸起。"""

    L order2"（夜神君的身体真敏感呢。）"

    "月闭着眼皱起眉，发出了几声梦呓，但是并没有醒过来。"

    menu:
        "现在要怎么做？(此处行动点数>=2会有额外选项)"

        "结束":

            hide fondle_rt1 with dissolve

            """今天就先到这里吧。

            L离开了囚室。"""

            jump after_fondle

        "玩弄另一边":

            """似乎对这种游戏上了瘾，L开始揉弄另一边还处于柔软状态的乳头。

            这一次，他下手稍微重了些，隔着衣服用指甲掐了一下，月发出了一声哼吟，但是依然没有醒。

            L能感受到月的另一颗乳豆也在自己的手指下变硬。

            今天就先到这里吧。

            L离开了囚室。"""
            hide fondle_rt1 with dissolve

            jump after_fondle 

        "撩起衣服继续爱抚（消耗额外的行动点）"if action_points >= 2:


            """L突然好奇月挺立的乳头变成了什么样子。
            
            他见过月的裸体，在搜查总部戴着手铐同居的时候就见过。
            
            但是现在的情况和那时不同，而是加上了一层旖旎暧昧的滤镜。

            L把囚衣的下摆撩到了锁骨处，月有些红肿的乳头暴露在了空气中，在白皙的皮肤上显得格外艳丽。

            就像是奶油蛋糕上的草莓。L想。

            他用大拇指摁在乳头上，感受到这个小东西硬硬地硌着自己，又用指甲盖拨弄了几下。
            
            月又发出了轻微的鼻音。"""

            hide fondle_rt1 with dissolve

            show fondle_rt2 at jubu with dissolve
            play sound "voice/kiss2.mp3"

            """

            L伏下身，尝试性地把舌面贴在月红艳艳的乳头上，用唇舌把它包裹起来。

            没有甜味，但是L莫名地兴奋了起来，联想到了草莓味的硬糖。
            
            他用力吸住这枚“草莓味硬糖”，然后听见月发出了更为缠绵的泣音。

            等到L把两边都品尝了个遍之后，他抬头，看见月已经满脸红潮，甚至额头都渗出了一层细汗。
            
            L瞟了一眼月的裆部，发现那里已经鼓了起来。"""

            L"（做春梦了吗。）"

            hide fondle_rt2 with dissolve

            """不过L没想顺便帮月解决生理需求，他给被自己蹂躏过的红肿乳头上了消肿的清凉药膏，就拉下衣服离开了。

            在监控里，L看见了月发现他自己梦遗后尴尬的反应，然后不得不向宿敌提出换内裤的请求。"""

            sy"【临时行动事件：梦遗】"

            menu:
                "要怎么做？"

                "追问原因":

                    L"夜神君做了奇怪的梦吗？"

                    "夜神月的脸上难得露出了尴尬的表情。"

                    Y renzhen"和你没关系吧！"

                    "L耸耸肩，拿出干净的内裤，并且暂时解开了对方的镣铐。"

                "不追问原因":
                    """L深知欲擒故纵的道理，什么也没问，为月带来了干净的内裤，并且暂时解开了对方的镣铐。

                    夜神月抿着嘴，拿起内裤，用眼神示意L避嫌。"""
                    if unlock_the_handcuffs:
                        $ affection = min(affection + 5, 75)
                    else:
                        $ affection = min(affection + 5, 70)

            menu:
                "夜神月不希望你看着他换内裤，你要怎么做？"

                "看着对方换":
                    "L没有要避嫌的意思，直勾勾地盯着夜神月换衣服的行为。"

                    Y Light"我要换衣服了，请你自重。"

                    L"囚犯是没有隐私的，夜神君很清楚这点吧？"

                    scene bath_4 with dissolve

                    """夜神月的脸上带上了怒气。

                    他一声不吭地开始脱去下裤，用L带来的湿纸巾清理下体，然后穿上新的内裤。

                    L看见他的性器与内裤上白浊的粘液被一点点擦干净，因为被注视着产生了羞意，所以只是草草清理了一下。"""

                    if unlock_the_handcuffs:
                        scene main bg_3 with fade
                    else:  
                        scene main bg_1 with fade

                    Y"谢谢。"

                    "夜神月的声音相当冷淡。"

                    L"不客气，夜神君，这是我应该做的。"

                    "L带着垃圾离开了囚室。"

                    jump after_fondle

                "转过身去":

                    scene bath_3 with dissolve

                    """L转过身去，给月留了一点个人空间。

                    背后传来细碎的穿衣服的声音。

                    L拿走了被弄脏的内裤，转身的时候听见月低低地说了一句：“谢谢。”

                    L背对着月勾起嘴角。"""

                    if unlock_the_handcuffs:
                        scene main bg_4 with fade
                    else:  
                        scene main bg_2 with fade

                    L smile1"不客气，夜神君，这是我应该做的。"

                    "L离开了囚室。"

                    if unlock_the_handcuffs:
                        $ affection = min(affection + 5, 75)
                    else:
                        $ affection = min(affection + 5, 70)
                    jump after_fondle



label fondle4:
    L"夜神君手被一直铐住肯定很不好受吧？"

    Y angry"……"

    """ 月一脸“你在说废话吗”的眼神。 """

    L order2"这是为了防止夜神君逃跑所做的必要措施，请你体谅一下。"

    Y"如果你过来只是说这些话，那你可以走了。"

    L"我还没说完呢。但是为了夜神君的健康，今天我可以短暂的解开夜神君的手铐。"

    L"不过夜神君如果趁机攻击我，我会很困扰啊。"

    Y"……"

    L"夜神君，就是你这种眼神才NG哦。"

    Y"（好想揍人……）"

    L pt"别这样看着我，我只是好心过来帮你按摩一下啊？请转过身去。"

    """ 月搞不懂L想干什么，但是也只能听他的话转过身去。

    月听见身后传来金属轻微的咔嚓声，原本紧缚着手腕的手铐一松，然后又是咔嚓一声。

    月能感受到自己的一只手已经被解放出来，所以他的第一反应就是把胳膊抬起来活动了一下僵硬的肌肉。

    等他转过身来，看见金属色的手铐另一端被铐在了L手上。 """

    Y Light"（这家伙……有必要这样吗？）"

    Y"我不会跑的。据你所说，如果我原本的死刑一直没有被执行是多亏了你，那么把你打晕了跑出去对我一点好处也没有，不是吗？"

    Y"而且你每次过来都不是用钥匙打开的牢房的门，是指纹解锁吧？就算我能用你的指纹打开牢房的门，再往其他地方走就很困难了。"

    L smile3"夜神君果然很聪明呢。"

    L thinking"其实也没什么特别的用意……就是突然想到夜神君之前失忆的时候也是这样和我铐在一起吧？虽然那时候的链子更长。"

    L"只是想到了失忆的夜神君之前让我困扰过一段时间……觉得夜神君真的很有意思呢。"

    Y han"（什么莫名其妙的。）"

    show fondle_4 at jubu with dissolve

    """ 当L突然伸手抓住他的手，指腹揉上被手铐勒出的红痕时，月被吓了一跳。 """

    #voice "voice/light/Y_wei.mp3"

    Y renzhen"……喂，你在干什么呢！"

    L"新的痕迹和旧的痕迹叠加起来了呢。"

    Y Light"（那是因为我一直在被迫戴着手铐吧……真是讨厌。）"

    L order2"如果活下来的代价是丧失自由，把这痕迹永远留在手上，夜神君会选哪个？"

    Y"……那当然是活下来。"

    Y"我活着能比死去创造更多的价值吧？而且我不想死。"

    """ 月的手被L握住，他能感受到L温暖的体温，和血液循环不通的他温差明显。

    L像是在思考着什么，一句话也没有说，只是手指像在捏解压玩具一样揉捏着月的手。

    那道红痕像是一圈代表怀疑的诅咒，逐渐扎根在青年白皙的手腕上。

    月的手比起之前要瘦了些，骨节明显，指甲也有些长了，甲床的血色要更淡些，像樱花一样的浅粉。

    这双手没有茧子，掌心柔嫩，只有右手中指关节上因为常年拿笔写字有着一层薄茧。

    L的拇指指腹缓缓滑过月手腕部磨损发红的地方，月因为有些刺痛皱起了眉，但是也没说什么。 """

    Y"（这家伙……癖好真是令人不敢恭维。）"

    """ 因为手一直被L握着，原本微凉的手也逐渐被传染了体温，变得温暖起来。

    真是漂亮的一双手啊，L想。

    就是这双手在死亡笔记上写了数千人的姓名，然后夺取了他们的生命吗？

    夜神月应当是不会后悔的吧，他可能唯一后悔的事只有没有早点杀死自己，扫除障碍。 """

    L pt"今天就到这里吧。"

    hide fondle_4 with dissolve

    """ L重新把手铐给夜神月铐上，离开了囚室。 """
    jump after_fondle
    
label fondle5:

    show fondle_5 at jubu with dissolve
    """ 虽然说月已经习惯了L会神出鬼没地出现在囚室里，有时候还会对他动手动脚……

    但是果然，不管怎么样都无法习惯后者啊！

    一般来说，会有同性突然捧着人的脸盯着看吗？

    黑发青年瘦削修长的手皮肤苍白，和褐发青年的肤色呈现出暧昧的差色。

    这双手捧起脸颊的方式像是在捧起一件艺术品，从那双纯黑眼瞳中透露出来的视线也是，让月比起难为情更多是一种怪异的被审视感。

    月的目光短促地上下扫了两下，不想和L对视，干脆把视线留在L锁骨处的衣领上。 """

    #voice "voice/light/Y_wei.mp3"

    Y"喂……龙崎，还没看够吗？"

    L"夜神君的头发有点长长了呢。"

    Y fadai"啊？……嗯，感觉有一个多月没剪了吧。"

    Y Light"话说不要转移话题啊，干嘛这样盯着我看？"

    L"夜神君现在跟我说话都不带敬语了呢。"

    Y"（谁要对你这家伙说敬语……）"

    """ 比起目测，双手的触摸确实更合实际，L将手下的触感与记忆中的夜神月对比，确认月确实瘦了许多。 """

    if food_h_points >= 3:

        """ 就算他尽量提高了饮食标准，但是之前在被日本政府拘留关押的期间，伙食肯定不会太好。

        加上极大的心理压力，月现在还算保持着正常的体重。 """

    # 分歧点结束

    """ 褐发青年原本弧度完美的脸颊曲线微微凹陷了一些，让骨相显现出来，五官变得更加锋利。

    鬓角的头发也略微长长到盖住耳朵，此时棕褐色的发丝因为受力在L的指间穿插弯曲着。

    L的手指轻轻一动，用中指搔了一下月的右耳，那双焦糖色的眼睛瞳孔微扩，像是小动物受到惊吓一般。 """
    #voice "voice/light/Y_en a.mp3"
    Y jiaoji2"……唔！你在干什么呢？！"

    L"夜神君的耳朵很敏感呢。"

    Y"那是因为你突然摸吧！"

    #voice "voice/light/Y_chuan1.mp3"

    Y yaoya2"……喂！别这样……"

    """ 似乎是觉得月的反应很有趣，L非但没有停下手上的动作，反而变本加厉地玩弄起了月的耳朵。

    月能感受到L的手指关节蹭过自己的耳廓，带起一阵酥麻的电流感，柔软的耳垂被L用中指和食指夹住缓缓揉捏；

    当食指过分地开始顺着外耳道描摹的时候，月终于忍不住猛地后撤，从L的掌中逃离。

    褐发青年的耳朵已经红透了，胸膛随着呼吸大幅度地起伏、颤抖着。 """

    Y jiaoji3"都说了不要这样了！你是变态吗！"

    L confused"我是……变态？"

    """ L露出了困惑的表情。 """

    L pt"没想到夜神君会这么讨厌被触摸啊，是我失礼了。"

    hide fondle_5 with dissolve

    Y jiaoji2"那是当然的吧！难道你还这样摸过别人吗？"

    L"……这倒没有。我没有那种兴趣。"

    Y Light"……"

    Y yaoya"（那你对我就有这种变态的兴趣吗！）"

    "他干脆转过身去不看L，没过一会，就听见了囚室的门被打开又关上的声音。"

    if unlock_the_handcuffs:
        "月松了口气，感到自己耳朵处的热意久久不散，还有些发痒，让他很想伸手挠一挠。 "
    else:
        "月松了口气，感到自己耳朵处的热意久久不散，还有些发痒，让他很想伸手挠一挠，只是碍于手铐无法如愿。 "

    jump after_fondle



label fondle_repeat:
    "（重复fondle）"
    jump after_fondle

label after_fondle:
    play music "audio/daily.mp3"
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
    
    # 检查行动点数是否归零
    if action_points <= 0:
        call next_day from _call_next_day_4
    else:
        sy"你还剩下 [action_points] 点行动点数。"
    $ Y_room = True
    jump action_menu