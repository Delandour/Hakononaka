default bath_points = 0  # 清洁次数计数器
default clean = 80          # 清洁度 (0 到 100)
default clean_max = 100        
default bath_allowed = False
default random_bath = []

# 预定义清洁次数到标签的映射
init python:
    import random


label daily_bath:

    $ Y_room = False
    if health <= 40:
        sy"夜神月看起来身体不适，需要尽快喂食药物。"
        menu:
            "需要返回行动菜单吗？"
            "返回":
                sy"不消耗行动点数，你还剩下[action_points]点行动点数。"
                $ Y_room = True
                jump action_menu

            "继续行动":
                $ bath_allowed = (clean + 25 <= clean_max)  # 直接计算，无需单独标签
                if bath_allowed:
                    $ bath_points += 1
                    if unlock_the_handcuffs:
                        $ clean = min(clean + 25, 100)
                        jump bath5
                    jump handle_bath
                else:
                    "月对拿着洗漱用具的L露出无奈的表情。"
                    Y "我已经很干净了，不需要清洁。"
                    jump after_bath



    $ bath_allowed = (clean + 25 <= clean_max)  # 直接计算，无需单独标签
    if bath_allowed:
        $ bath_points += 1
        if unlock_the_handcuffs:
            $ clean = min(clean + 25, 100)
            jump bath5
        jump handle_bath
    else:
        "月对拿着洗漱用具的L露出无奈的表情。"
        Y "我已经很干净了，不需要清洁。"
        jump after_bath

label handle_bath:
    $ clean = min(clean + 25, 100)
    if not random_bath:
        if unlock_the_handcuffs:
            jump bath5
        else:
            $ random_bath = random.sample(["bath1","bath2","bath3","bath4"],4)
    $ current_bath = random_bath.pop(0)
    jump expression current_bath

label bath1:
    """
    L拿来了换洗衣服，漱口水，水盆和毛巾，囚室里装有热水管道，对于洗漱来说方便很多。

    先把脏衣服换掉吧，L想，不过夜神君如果趁机攻击自己会很苦恼啊。"""

    L order2"""夜神君，为了换衣服和擦身我会分别解开你的手铐和脚铐，
    
    我建议他放弃趁机攻击我的念头，渡在那边实时监控着，如果我有什么意外夜神君也不会得到好结果的。"""

    Y"我不会做没有成功率的蠢事的。只要你别对我动手动脚就行。"

    "月的嫌恶显而易见。"

    "L首先解开了月的手铐。"

    Y"我可以自己换衣服和擦身。"

    scene bath_4 with dissolve
    $ persistent.unlock_bath_4 = True

    """L注视着月自己换了上衣，用湿毛巾擦了身体，脸和脖子，顺便漱了口。

    L重新把月的双手铐在背后。

    L解开了月的脚铐，脱掉了月的囚裤。"""

    Y"不用帮我擦了，直接换衣服就行。"

    menu:

        "那就算了，只换衣服吧":

            L"夜神君不愿意就算了。"

            scene black with dissolve

            """L拿出换洗衣服，帮月换上。
            
            期间月好像是在逃避现实似的，干脆闭上了眼睛。"""

            scene main bg_1 with dissolve

            """

            衣服很快就换好了。

            新衣服有淡淡的洗涤剂的清香。

            但是月还是感觉身上和头发有些油腻，现在只能忍耐下来。
            
            """
            $ stress = max(0, stress - 5)
            if unlock_the_handcuffs:
                $ affection = min(affection + 5, 75)
            else:
                $ affection = min(affection + 5, 70)
            $ clean = max(0, clean - 10)
            jump after_bath


        "清洁是必要的，不听":      

            L"不行，清洁必须做彻底才可以。"
            
            play sound "audio/sound/short_punch1.mp3"
            Y"你能不能听人说话啊！？"

            scene bath_2 with dissolve  
            $ persistent.unlock_bath_2 = True


            """月抬腿就想踹L，被一把捉住了脚腕，另一条腿还想踹，但是被L躲过去了，站在了踹不到的死角。

            月因为失衡，上半身后仰躺在了床上。"""

            L"如果夜神君配合的话很快就好了。"

            """温热的毛巾从内裤下缘的大腿根部下行，一直到脚腕，
            
            然后L在水盆里拧了一把毛巾，把月的脚背脚心脚趾间也擦了一遍。"""
            
            scene bath_2 with vpunch

            show fondle_jiao at jubu with dissolve

            """在捏到脚心的时候，月浑身颤了一下。"""

            Y jiaoji2"……变态。（咬牙切齿）"

            L"……？"

            hide fondle_jiao with dissolve

            "清洁完之后，L给月换上了新的囚裤，重新铐好脚铐，把脏衣服和清洁器具带出了房间。"

            $ stress = min(100, stress + 5)
            jump after_bath

label bath2:


    "L拿来了洗发水，梳子，吹风机，漱口水，水盆和毛巾，囚室里装有热水管道和插座，对于洗漱来说方便很多。"

    L"夜神君已经知道该怎么做了吧？"

    Y"我也很好奇你是怎么做到把每句话都说得这么恶心的。"

    L"我可没说什么，是夜神君自己理解歪了。今天要给夜神君洗头，麻烦站到洗手池这边来。"

    play sound "sound/washing hair.mp3"

    scene bath_1 with dissolve

    $ persistent.unlock_bath_1 = True

    "月不情不愿地站到洗手池旁边，弯下腰。头皮确实有些油腻了，出于洁癖他也只能配合L的行动。"


    L"我还没有给别人洗过头呢。"

    Y"那我可真是荣幸啊。"

    L"我的意思是如果水温和力道不合适麻烦夜神君说出来。"
    voice "audio/sound/short_punch1.mp3"
    Y renzhen"……喂，这是冷水啊！"


    L unhappy"抱歉。"

    Y Light"……烫了。"

    L unhappy"好麻烦。"



    """总算调到了合适的水温，L挤了一泵洗发水在手上，揉搓出泡沫，再抹到月的头发上。

    青年的发丝很柔顺，打湿了之后像某种动物的毛发，贴在头皮上。
    
    L笨拙地按摩了几下，不得要领，就草草把所有的发丝打上泡沫了事。

    用水流把泡沫冲掉之后，L先用干毛巾把月的头包起来，挤压了一下水分，然后插上吹风机帮忙把头发吹干。"""

    scene room_1 with dissolve
    stop sound fadeout 1.0

    play sound "sound/dry hair.mp3"

    "月的声音在吹风机的隆隆声中有些听不清。"

    Y"你照顾人的手法真的是有够烂。"

    L"所以我提前说了请多包涵。"

    Y"那你把手铐解开让我自己做不就行了。"

    L unhappy"总感觉夜神君会揍我。"

    "月哼笑一声。"
    
    Y smile2"你还挺有自知之明。"

    stop sound fadeout 1.0  


    """吹完头发，L用梳子简单地帮月梳了头发，感觉有点长长了。
    
    L想起这种既视感是在宠物美容店，店员给小猫小狗洗完澡之后吹干梳毛。
    
    不过这个不能告诉夜神君吧，他肯定会生气的。"""

    scene bath_2 with dissolve

    L pt"今天的擦身就由我代劳吧。"
    play sound "audio/sound/short_punch1.mp3"
    Y renzhen"……喂！"

    """ 无视月的反抗，L把囚衣的下摆撩到月的锁骨处，白皙柔软的腹部露了出来。

    腹部是所有动物的弱点呢。L漫不经心地想。
   
    用浸湿的毛巾快速擦拭了月的前胸、腹部和后背，又拧了一次水擦拭了月的脖子和脸颊。

    接下来应该擦下半身了。"""

    L"夜神君要帮忙擦下面吗？"

    Y angry"这还用问吗？你觉得我像是想跟你肢体接触的样子？"

    L"下次清洁要等到几天后了，如果夜神君不会难受也可以。"

    Y"……"

    Y"你如果敢乱摸我就杀了你。"

    L"好可怕啊，夜神君。（无感情）"


    menu:
        "(此处行动点数>=2会有额外选项)"

        "不擦了收工":

            L"算了，既然夜神君这么不情愿，我也不勉强你了。"

            scene room_1 with dissolve

            """ L把洗漱用具收拾好离开了囚室。

            月松了一口气，虽然感觉身上没有清洁干净不太舒服，但是也只能忍耐了。 """

            if unlock_the_handcuffs:
                $ affection = min(affection + 5, 75)
            else:
                $ affection = min(affection + 5, 70)
            $ stress = max(0, stress - 5)
            $ clean = max(0, clean - 5)
            jump after_bath


        "只脱掉长裤":

            """ L把月的黑色长裤脱到脚踝的位置，用浸湿的毛巾擦过月笔直修长的双腿。

            毛巾在蹭过敏感的大腿内侧和足心的时候令月有些不适，不过L确实没有乱摸，他也没理由说什么。

            擦完之后他松了一口气，等L帮他把裤子穿上。

            当囚裤的面料重新覆盖皮肤，月感到了一丝安全感。 """

            L"今天先到这里吧。"

            """ L离开了囚室。 """

            if unlock_the_handcuffs:
                $ affection = min(affection + 5, 75)
            else:
                $ affection = min(affection + 5, 70)
            $ stress = max(0, stress - 10)
            jump after_bath

        "内裤也脱掉"if action_points >= 2:

            """L把月的黑色长裤脱到脚踝的位置，用浸湿的毛巾擦过月笔直修长的双腿。

            毛巾在蹭过敏感的大腿内侧和足心的时候令月有些不适，不过L确实没有乱摸，他也没理由说什么。

            擦完之后他松了一口气，等L帮他把裤子穿上。

            但是与他的预料相反，布料没有重新包裹住他的双腿，反而是贴身的布料也被扯下，褪到膝弯。

            月的脸上染上了一层薄红，不知道是羞得还是气得。"""

            Y yaoya2"喂，你在干什么？？"

            "L拿来一条毛巾。"
            
            L smile1"帮夜神君清洁啊，生殖器官会分泌很多分泌物，如果不定时清洁也会很脏的。"

            Y "你已经让我感觉不适了，L，你这是性骚扰！"

            L"麻烦夜神君忍耐一下吧，毕竟如果发炎了会很麻烦呢。"

            show clean_sex at jubu with dissolve

            "L拿着毛巾的手握住了月的阴茎，揉搓清洁起来。"

            Y "（简直就像是在帮忙手淫一样……真的是疯了……）"

            "已经长期禁欲的身体根本经不起挑拨，在清洁到敏感的龟头时，月已经完全勃起了，前列腺液也缓缓溢出。"

            L"夜神君勃起了，没关系吗？"

            Y "你这……混账……"


            """情欲的火焰久违地在身体里燃烧起来，月甚至不敢过多开口，害怕直接在L面前呻吟出声。
            
            大脑被刺激得头皮发麻，小腹也紧缩着，抵抗想要更多的抚摸然后射精的想法。

            L用食指和拇指捏住月挺立的龟头，语调还是一样平静。"""

            L"夜神君，你想射出来吗？出于对生理健康的建议，我觉得射出来比较好。"

            """囚室里回荡着月急促的喘息声。
            
            他闭上眼睛，不愿意去看自己被宿敌拿捏的丑态。

            他知道L在逼迫自己屈服。"""

            if affection < 60:

                Y yaoya"不需要。"

                L order2"我知道了。"

                hide clean_sex with dissolve

                """脆弱部位传来一阵疼痛，立刻浇熄了欲火。

                L用纸巾擦干净溢出的前液，帮月穿好了裤子，拿着洗漱器具离开了囚室。

                月瘫在床上，后知后觉地出了一身细汗，欲望被强行打断，所以并没有满足的感觉，而是一种空虚感。
                
                他无意识地摩擦了几下大腿，脚铐被挣出稀碎的响声。"""
            else:
                """ 月只不过是犹豫了几秒钟，L就自顾自地手上动作起来。

                那双修长而骨节分明的手握住青年的性器，用更色情的手法撸动起来。 """

                Y jiaoji3"喂，龙……哈啊！"

                """ 月下意识睁开眼睛想要斥责L，映入视野的是L肌肤苍白的双手与性器深粉色强烈的色彩对比，刚好龟头擦过了指腹，敏感的地方被蹭到，让他不禁发出一声呻吟。"""
                Y"快……哈、快停下来……嗯唔！"

                """ 被侦探手淫的羞耻感让月的脸颊烧了起来，红晕从耳尖、面颊一直蔓延到脖颈，他几乎无法抵抗来势汹汹的快感，腰肢都因为下半身的刺激软了下去。
                """
                L order2"夜神君明明很舒服吧，不用抵抗，就这样射出来也可以哦。"

                """ L低沉的声音在月的耳边响起，简直就像在诱惑他堕入地狱的魔鬼。
                """
                Y yaoya"哈啊……闭嘴！"

                """ 月咬着嘴唇，不想泄露出更多丢人的呻吟声。

                他用所有的意志力抵抗着身下想要射精的欲望，但是意识本身仿佛也在L的手下被揉捏着，染上灼热的温度。

                柱身被手掌握着撸动，旋转着要榨精一般收紧，拇指的指腹按揉着敏感的龟头，甚至用指甲轻轻扣弄铃口。 """

                Y yaoya2"……嗯、嗯呜呜……"

                """ 褐发青年的呼吸变得粗重，发出难以抑制的闷哼。 """

                Y"（已经不行了……要、要去了……）"

                """ 月颤栗着身体，下腹一阵一阵地收紧，指甲深深刺入掌心，眼前因为射精高潮变得空白一片。 """

                Y"哈啊、嗯啊啊啊——"

                """ 青年的眼睛因为快感失焦，肌肉在高潮中放松，发出了甜腻又高昂的呻吟声，这种舒爽感让他失神了好几秒才缓缓回神。

                月喘息着，低头看见L的掌心正拢着一滩乳白色的液体，一只手还捏着自己软掉的阴茎不放，羞耻心又涌了上来。 """
                hide clean_sex with dissolve

                Y jiaoji3"已经够了吧！你这家伙还要戏弄我到什么时候！"

                L smile3"积攒了很多呢……夜神君对待刚服务过自己的人就这种态度吗？"

                Y "又不是我想要你这么做的！……快去洗手。"

                """ 被月连声催促，L才慢悠悠地起身，洗了手之后帮月重新做了事后清理，整理好了衣服。 """

            $ affection = max(0, affection - 5)
            $ stress = min(100, stress + 10)
            
            
            jump after_bath

label bath3:

    """L拿来了漱口水，水盆和毛巾，囚室里装有热水管道，对于洗漱来说方便很多。

    月看着L倒了一瓶盖漱口水递过来，皱起眉头："""

    Y "龙崎，能把手铐和脚铐解开让我自己洗漱吗？"
    
    menu:
        "要怎么做？"

        "不解开":

            Y"好吧，如果你坚持我也没办法。"

            "月在L的帮助下用漱口水漱了口，用毛巾擦了脸和脖子。"

        "解开":
            Y"谢谢。"
            "月活动了一下手腕和脚腕，用漱口水漱了口，用毛巾擦了脸和脖子。"
            if unlock_the_handcuffs:
                $ affection = min(affection + 5, 75)
            else:
                $ affection = min(affection + 5, 70)

    "结束之后，月被重新带上了镣铐。"

    L"需要帮忙擦身吗？"
    
    Y"不用了。"

    menu:
        "L看着月冷淡的侧脸，准备……"

        "离开":
            
            "L闻言没有强迫月，而是直接离开了。"
            $ clean = max(0, clean - 10)
            jump after_bath

        "强制擦身":
            scene bath_2 with dissolve
            $ persistent.unlock_bath_2 = True
            "L无视月的拒绝，强行把衣服撩了起来，用温热的毛巾擦洗月的身体。"
            
            play sound "audio/sound/short_punch1.mp3"
            Y jiaoji1"喂！你是听不懂人话吗！"
            "夜神月显得非常气愤。"
            "不过受到镣铐的限制，他没法做出有效的反抗，只能忍耐……"

            $ affection = max(0, affection - 5)            
            jump after_bath            

label bath4:
    

    "L拿来了换洗衣服，牙缸，牙膏和牙刷，水盆和毛巾，囚室里装有热水管道，对于洗漱来说方便很多。"

    Y"你还要坚持让我带着手铐和脚铐换洗吗？我不会袭击你的，我只想好好清洗自己。"

    """看着月诚恳的脸，L放软了态度，给月解开手铐和脚铐。

    月先刷了牙，漱过口之后，把洗具整理整齐，然后看了L一眼。

    L意识到月要脱衣服擦身了。"""

    menu:
        "现在要怎么做？"

        "当做不知道，继续看月脱衣服":
            scene bath_4 with dissolve
            $ persistent.unlock_bath_4 = True
            "月有些不高兴，但是也没有说什么，迅速换完了衣服。"
            
            $ affection = max(0, affection - 5)

        "转过身去不看":

            scene bath_3 with dissolve
            $ persistent.unlock_bath_3 = True

            """L会意地转过身去，背对着月。

            身后传来细碎的脱衣服的声音。

            然后是水流声，蓄满了水盆。毛巾在水盆里被浸湿，然后拿起来拧干，发出哗啦啦的水声。

            湿润的毛巾擦拭身体的声音几近于无。

            L无聊地盯着自己的脚趾甲盖看。"""

            Y"已经可以了。"

            scene main bg_1 with dissolve

            """L转身，看见月换上了新的囚服，洗具和换洗下来的衣服已经整理好了，叠放在水盆里。

            L拿起盆离开了囚室。 """

    jump after_bath

label bath5:

    """ L拿来了换洗衣服与洗发水、沐浴液、毛巾和水盆等洗漱用品，囚室里装有热水管道和插座，对于洗漱来说方便很多。

    经历过戴着手铐被L擦身和洗头的“服务”，月对于能够自己清洁自己感到了自由的可贵。

    L看见月迫不及待把装着洗漱用品的水盆接过去，直接忽略他开始在洗手池边开始洗头，心中感到了一丝郁闷。 """
    play sound "sound/washing hair.mp3"
    scene room_1 with dissolve
    L"（我帮夜神君擦身洗头的手法有那么差吗……）"

    """ 虽然环境很简陋，但是月每次在清洁自己时都能体会到放松和愉悦感。

    他自小就拥有良好的卫生习惯，夏天每天都会洗澡，贴身的衬衫从不隔夜穿，更别说内裤和袜子。

    所以在囚室内最令他不能接受的就是卫生问题，和马桶共处一室也就算了，L有时一忙起来三四天忘了带清洁用具过来，这才真的令人崩溃。

    能自己控制舒适的水温真好，能仔细用指腹把头皮也清洁干净真好。"""

    stop sound fadeout 1.0

    play sound "sound/dry hair.mp3"
    
    """把头发洗了两遍之后，月仔细地用毛巾把头发包起来吸干水分，然后用吹风机把头发吹干。

    在吹风机的隆隆声中，月手法熟练地翻动着头发，确保吹风机先吹干发根，然后才是发梢。

    啊啊，再也不用忍受L使用吹风机时糟糕的手法了，他可不喜欢被热风烫到头皮啊。

    吹完头发，月用余光往L的方向瞟去，发现对方正在百无聊赖地盯着墙上的污点看，察觉到月的目光后看了回来。 """
    stop sound fadeout 1.0
    L"怎么了，夜神君？"

    Y"……没什么。（真是敏锐的家伙。）"

    L"嗯嗯，我知道的，夜神君肯定在心里想“这家伙的服务手法真烂”之类的话吧。"

    Y"（这不是事实吗……说得这么有气无力、充满哀怨的是要怎样。）"

    Y"没有哦，龙崎也没有伺候别人的经验吧，所以这样不是很正常吗。不如说我会感到荣幸呢。"

    L"……"

    """ 被L用“肯定又是在花言巧语”的眼神注视着，月也不在意，事到如今他们对对方也算是知根知底了。 """

    Y"接下来我要换衣服擦身了，可以请你转过去吗，龙崎？"  
    menu:
        "现在要怎么做？"

        "继续看月脱衣服":
            scene bath_4 with dissolve
            $ persistent.unlock_bath_4 = True
            L"夜神君，我在这里的职责就是监视你，包括这种情况。"

            """
            月有些不高兴，但是也没有说什么，自己转过身去开始脱衣服擦身。
            
            他背对着L褪去了黑色的囚服上衣，形状优美的蝴蝶骨连着肩颈纤细的肌肉暴露在L的视线下，来自他人的目光直勾勾地盯着自己的后背，不禁让月有些发毛。
            
            月把毛巾在水盆里浸湿，随后拎起拧干，用湿润的毛巾擦拭过皮肤。在水分消耗殆尽后又将毛巾重新打湿，周而复始地重复着这一简单的举动。
            
            很快上半身的清洁工作就进入了尾声，月从床铺上拿起替换的干净囚服，快速穿上后才感觉那种被L盯着的紧张感有所缓解。
            
            他将手指搭上囚裤的松紧带，踌躇了一会才硬着头皮把黑色的长裤脱掉，
            
            他还是很在意L的视线，但长期被束缚着的膝弯和大腿内侧的确积攒了一些新陈代谢产生的污垢，如果不用湿毛巾清洁的话，恐怕身体会变得黏腻起来吧。
            
            月用清洁的必要性催眠着自己，用最快的速度打湿毛巾擦拭了一遍下半身，随后抓起搭在床头的替换囚裤穿了上去，草草结束这场奇怪的活动。
            """
            Y"已经可以了。"
            """L看见月把洗漱用具和换洗下来的衣服已经整理好了，叠放在水盆里，便拿起盆离开了囚室。 """
            $ affection = max(0, affection - 5)

        "转过身去不看":

            scene bath_3 with dissolve
            $ persistent.unlock_bath_3 = True

            """L会意地转过身去，背对着月。

            身后传来细碎的脱衣服的声音。

            然后是水流声，蓄满了水盆。毛巾在水盆里被浸湿，然后拿起来拧干，发出哗啦啦的水声。

            湿润的毛巾擦拭身体的声音几近于无。

            L无聊地盯着自己的脚趾甲盖看。"""

            Y"已经可以了。"

            scene main bg_3 with dissolve

            """L转身，看见月换上了新的囚服，洗漱用具和换洗下来的衣服已经整理好了，叠放在水盆里。

            L拿起盆离开了囚室。 """

    jump after_bath
  

screen clean_notify(current, max_val, action_points):
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
                text _("清洁完毕"): 
                    xalign 0.5

                hbox:
                    text _("清洁度："):
                        min_width 80  # 固定标签宽度，对齐更整齐
                        yalign 0.5
                    bar:
                        value AnimatedValue(clean, clean_max, 1.0)  # 动画过渡效果
                        xmaximum 200  # 进度条宽度
                        ysize 26      # 进度条高度
                        yalign 0.5
                    text " [clean]/[clean_max] ([get_status_description(clean, clean_descriptions)])":
                        yalign 0.5
    
        # 确认按钮
        textbutton _("确认"):
            action Return()  
            xalign 0.5
            ypos -90



label after_bath:
    
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

    if bath_allowed:  # 仅成功清洁时扣除
        $ action_points -= 1
    else:
        sy"无需清洁，行动点不扣除"
    call screen clean_notify(clean, clean_max, action_points)
    # 弹窗关闭后，检查行动点是否归零
    if action_points <= 0:
        call next_day from _call_next_day
    else:
        $ Y_room = True
        jump action_menu 