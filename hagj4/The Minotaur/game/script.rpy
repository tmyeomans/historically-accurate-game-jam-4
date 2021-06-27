#The Minotaur by S. Latta and T. Yeomans
#Submission for the Historically Accurate Game Jam 4

init:
     $ thes= Character("Theseus",color = "#3a86ff", what_color = "#3a86ff")

init:
    $ ari= Character("Ariadne", color = "#ac46a1", what_color = "#ac46a1")

init:
    $ hel= Character("Helena", color = "#C7D3BF", what_color = "#C7D3BF")

init:
     $ yc= Character("Yellow",color = "#ffba08", what_color = "#ffba08")

init:
     $ gc= Character("Green",color = "#90be6d", what_color = "#90be6d")

init:
     $ wc= Character("Orion",color = "#FFFFFF", what_color = "#FFFFFF")

init:
     $ rc= Character("Red",color = "#c9184a", what_color = "#c9184a")

init:
     $blc= Character("Blue", color = "#56cfe1", what_color = "#56cfe1")

init:
     $oc= Character("Orange", color = "#ff9e00", what_color = "#ff9e00")

init:
     $pc= Character("Purple", color = "#deaaff", what_color = "#deaaff")

init:
     $bc= Character("Brown", color = "#c38e70", what_color = "#c38e70")

init:
     $grc= Character("Grey", color = "#adb5bd", what_color = "#adb5bd")

init:
     $ajax= Character("Ajax", color = "#DACC3E", what_color = "#DACC3E")



screen stringbar:
    text "String left: [currentstring]/[maxstring]" xalign 0.0 yalign 0.05
    bar value currentstring range maxstring xalign 0.0 yalign 0.1 xmaximum 1280


# The game starts here.
label start:

    $currentstring = 8
    $maxstring = 8

    scene black

    centered "On the island of Crete lives the fearsome minotaur, roaming the passages of Daedalus’s labyrinth."
    centered "As a condition of peace, the people of Athens send 14 youths through the labyrinth gates every seven years."
    centered "None have returned."
    centered "Brave Theseus, you must end this folly. Speak with the princess Ariadne, enter the labyrinth, and…"
    play music "audio/minotaur.mp3"
    centered "SLAY THE MINOTAUR"

    play music "audio/sb_chasingdaylight.mp3"
    centered "{size=100}{color=#f00}The Minotaur{/size}{/color}"

#############


label introduction:
    show open
    show ariadne
    with dissolve

    ari "Theseus, my love, you’ve arrived! Your father allowed this?"
    thes "I gave him no choice. When the Minotaur is dead and I return to Athens, we shall fly the white flag of victory and my father will see me for the King that I am."
    ari "And if you fail?"
    thes "Then the flag shall be black."
    ari "By Zeus! I can’t bear that, Theseus. Let me help!"
    thes "I must go alone, in the footsteps of my countrymen."
    ari "But you need not go unarmed! Take this {u}sword{/u}, that you may slay the beast."
    show sword with dissolve
    ari "Ariadne: And take this length of {u}thread{/u}. If you follow the wrong path through the labyrinth, you can retrace your steps."
    hide sword with dissolve
    show thread with dissolve

    "{i}When you reach a dead end, use the thread to backtrack. With each step forward or back, your thread count will deplete.{/i}"
    hide thread with dissolve

    thes "My thanks, good Ariadne! And now I am ready."
    ari "Wait! There’s something more you must know. Many of the Athenians who’ve entered the labyrinth are still alive, but… changed. A strange madness afflicts them, perhaps caused by the terror of the Minotaur, or perhaps it’s some trickery of Dolos."
    ari "The Athenians inside are demented in one of two ways: some {u}speak only the truth{/u}. Others {u}speak only falsehoods.{/u}"
    thes "How will I know which is which?"
    show helena with dissolve
    ari "You must listen to what they say. I’ve brought my handmaiden, Helena, to demonstrate. We will each say one thing. Listen carefully."


label tutorial:
    hel "Ariadne and I are both truth tellers."
    ari "Helena is a liar."
    ari "Now who is telling the truth? Who is lying? Both of us? Neither of us?"

    menu:
        "{color=#C7D3BF}(Helena: Ariadne and I are both truth tellers){/color}"
        "{color=#ac46a1}(Ariadne: Helena is a liar){/color}"
        "{color=#ac46a1}Now who is telling the truth? Who is lying? Both of us? Neither of us?{/color}"

        "Helena is telling the truth, Ariadne is lying.":
            jump think
        "Ariadne is telling the truth, Helena is lying":
            jump correcttut
        "Both Helena and Ariadne are telling the truth.":
            jump think
        "Both Helena and Ariadne are lying.":
            jump think


label think:
    ari "Think again, Theseus! Consider carefully what each of us say."
    jump tutorial


label correcttut:
    ari "Yes, you understand! And now that you know the truth tellers from the liars, ask one of us for directions to the labyrinth’s entrance."

    menu:
        "Ask Ariadne for directions.":
            jump aridirections

        "Ask Helena for directions.":
            jump heldirections


label aridirections:
    ari "Follow the path to the south."
    menu:
        "Begin walking the path to the north.":
            jump arinorth

        "Begin walking the path to the south.":
            jump arisouth


label arinorth:
    ari "Theseus, do you misunderstand? I am acting as a truth teller. Follow my guidance!"
    jump aridirections


label arisouth:
    ari "Godspeed, my love!"
    jump endtutorial


label heldirections:
    hel "Follow the path to the north."
    menu:
        "Begin walking the path to the north.":
            jump helnorth

        "Begin walking the path to the south.":
            jump helsouth


label helnorth:
    ari "Wait, Theseus! Remember, to help you understand the challenges ahead, Helena is only telling lies."
    jump heldirections


label helsouth:
    ari "Ah, very clever of you, dear Theseus! Now set forth, and may the gods be with you."
    jump endtutorial


label endtutorial:
    hide helena
    hide ariadne
    hide open
    with dissolve
    centered "{i}Theseus follows the wall of the great labyrinth until he finds an opening. And with that, his journey begins.{/i}"

#################### end of tutorial ###########################


label lab1intro:
    centered"{i}As you enter the great labyrinth, you see little more than thick stone walls, dry and crumbling but sturdy. You follow the path as it twists and turns until you reach a junction, with a door on each side.{/i}"
    centered "{i}You unwind the first length of Ariadne’s thread and tie it to a sconce on the wall. If you take a wrong path in the labyrinth, you can use this thread to retrace your steps. However, the thread will deplete as you progress, and once it has run out you can no longer use it. (See the meter at top of screen){/i}"

    show sky1
    show leftright
    show stringback
    show athenians
    show screen stringbar
    with dissolve

    thes "Greetings!"
    "{i}They say nothing.{/i}"
    "{i}You recall Ariadne’s remarks that they are cursed and unable to speak as normal.{/i}"
    "{i}Some will tell only the truth, others will tell only lies. And so the men before you may both be liars, or they may both be truth-tellers, or one may be a liar and the other a truth-teller.{/i}"


label lab1:

#some text about unwinding a length of thread
    $currentstring-=1
    show sky1
    show leftright
    show stringback
    show athenians
    show screen stringbar
    with dissolve

    yc "He and I are both truth-tellers."
    gc "He is a liar."

    menu:
        "{color=#ffba08} (Yellow: He and I are both truth-tellers){/color}"
        "{color=#90be6d} (Green: He is a liar){/color}"
        "{i}You can ask only one of them for directions. Who do you ask?{/i}"

        "Ask Yellow which way to go.":
            jump yellow1


        "Ask Green which way to go.":
            jump green1

label yellow1:
    yc "Go left"

    menu:
        "{color=#ffba08}(Yellow: He and I are both truth-tellers){/color}"
        "{color=#90be6d}(Green: He is a liar){/color}"
        "{color=#ffba08}(Yellow: Go to the left){/color}"

        "Go to the left":
            jump badroom1

        "Go to the right":
            jump correct1


label green1:
    gc "Go to the right."

    menu:
        "{color=#ffba08}(Yellow: He and I are both truth-tellers){/color}"
        "{color=#90be6d}(Green: He is a liar){/color}"
        "{color=#90be6d}(Green: Go to the right){/color}"

        "Go to the left":
            jump badroom1

        "Go to the right":
            jump correct1


label correct1:
    $currentstring-=1
    hide leftright
    hide stringback
    hide athenians
    hide sky1
    with dissolve
    jump lab2intro


label badroom1:
    $currentstring-=1
    hide leftright
    hide stringback
    hide athenians
    show deadend
    show stringback
    with dissolve

    "{i}You have reached a dead end, with no way forward.{/i}"
    if currentstring > 0:
        "{i}You use a length of Ariadne’s thread to retrace your steps, returning to the previous room.{/i}"
        hide deadend
        hide sky1
        hide stringback
        hide screen stringbar
        with dissolve
        jump lab1

    if currentstring <= 0:
        "{i}You reach for Ariadne’s thread but realize in panic that it was exhausted some time ago. You search frantically for the path, but it is as if the halls and passages are new and unrecognizable. Have you fallen victim to the labyrinth’s curse?{/i}"
        "{i}You run, left and right, down the passages, only becoming more lost. You feel confused and dizzy, now unsure of where you are going and why you are here.{/i}"
        thes "These walls are made of wood. At the end of this labyrinth is the fearsome Medusa. I am a truth-teller."
        "{i}Theseus’s journey has come to an end. Try again?{/i}"
        return


label lab2intro:
    hide screen stringbar
    with dissolve
    centered "{i}As you continue further, you see a three-way divide in the path. But there are no nearby Athenians to offer guidance.{/i}"


label lab2:
    show sky1
    show threechoice
    show stringback
    show screen stringbar
    with dissolve
    pause 2.0
    show shapes
    with dissolve
    "{i}Puzzled, you look around, noticing a strange etching on the rock floor adjacent to the forked road.{/i}"


    menu:
        "Go to the left":
            jump lab3intro

        "Go straight ahead":
            jump badroom2

        "Go to the right":
            jump badroom2

        "Look again at the etching":
            jump lab2

label badroom2:
    $currentstring-=1
    hide stringback
    hide threechoice
    show deadend
    show stringback
    with dissolve

    "{i}You have reached a dead end, with no way forward.{/i}"

    if currentstring > 0:
        "{i}You use a length of Ariadne’s thread to retrace your steps, returning to the previous room.{/i}"
        hide deadend
        hide shapes
        hide sky1
        hide stringback
        with dissolve
        jump lab2

    if currentstring <= 0:
        "{i}You reach for Ariadne’s thread but realize in panic that it was exhausted some time ago. You search frantically for the path, but it is as if the halls and passages are new and unrecognizable. Have you fallen victim to the labyrinth’s curse?{/i}"
        "{i}You run, left and right, down the passages, only becoming more lost. You feel confused and dizzy, now unsure of where you are going and why you are here.{/i}"
        thes "These walls are made of wood. At the end of this labyrinth is the fearsome Medusa. I am a truth-teller."
        "{i}Theseus’s journey has come to an end. Try again?{/i}"
        return


label lab3intro:
    hide threechoice
    hide sky1
    hide stringback
    hide screen stringbar
    hide shapes
    with dissolve

    centered "{i}Again, the path forks, with no evidence as to which path leads to the minotaur, and no Athenians to give guidance.{/i}"

    show sky1
    show leftright
    show stringback
    show screen stringbar
    with dissolve
    $currentstring-=1
    pause 2.0


label lab3:
    show sky1
    show leftright
    show stringback
    show maze
    show screen stringbar
    with dissolve
    "{i}A maze is etched on to the wall in front of you. You jump forward with excitement, believing this to be a map of the labyrinth itself, but you quickly realize its passageways don’t match those you’ve traversed. Perhaps if you trace its path, it will point you in one direction or the other?{/i}"

    menu:
        "Go to the left":
            jump lab4intro

        "Go to the right":
            jump badroom3

        "Look again at the maze":
            jump lab3


label badroom3:
    $currentstring-=1
    hide leftright
    hide maze
    show deadend
    with dissolve

    "{i}You have reached a dead end, with no way forward.{/i}"

    if currentstring > 0:
        "{i}You use a length of Ariadne’s thread to retrace your steps, returning to the previous room.{/i}"
        hide deadend
        hide sky1
        hide stringback
        hide screen stringbar
        with dissolve
        jump lab3

    if currentstring <= 0:
        "{i}You reach for Ariadne’s thread but realize in panic that it was exhausted some time ago. You search frantically for the path, but it is as if the halls and passages are new and unrecognizable. Have you fallen victim to the labyrinth’s curse?{/i}"
        "{i}You run, left and right, down the passages, only becoming more lost. You feel confused and dizzy, now unsure of where you are going and why you are here.{/i}"
        thes "These walls are made of wood. At the end of this labyrinth is the fearsome Medusa. I am a truth-teller."
        "{i}Theseus’s journey has come to an end. Try again?{/i}"
        return


label lab4intro:
    hide maze
    hide sky1
    hide leftright
    hide stringback
    hide screen stringbar
    with dissolve
    centered "{i}That seems to have been the correct path, for you encounter yet another intersection, with two more Athenians idling nearby.{/i}"


label lab4:
    $currentstring-=1
    show sky1
    show leftright
    show stringback
    show orangepurple
    show stringback
    show screen stringbar
    with dissolve

    oc "I am a truth-teller or she is a liar."
    pc "One of us is a truth-teller, but not both of us."

    "{i}You can ask only one of them for directions. Who do you ask?{/i}"

    menu:
        "{color=ff9e00}(Orange: I am a truth-teller or she is a liar){/color}"
        "{color=deaaff}(Purple: One of us is a truth-teller, but not both of us){/color}"
        "{i}You can ask only one of them for directions. Who do you ask?{/i}"

        "Ask Orange which way to go":
            jump orange1


        "Ask Purple which way to go":
            jump purple1


label orange1:
    oc "Go to the left."

    menu:

        "{color=ff9e00}(Orange: I am a truth-teller or she is a liar){/color}"
        "{color=deaaff}(Purple: One of us is a truth-teller, but not both of us){/color}"
        "{color=ff9e00}(Orange: Go to the left){/color}"

        "Go to the left":
            jump badroom4

        "Go to the right":
            jump lab5


label purple1:
    pc "Go to the right."

    menu:

        "{color=ff9e00}(Orange: I am a truth-teller or she is a liar){/color}"
        "{color=deaaff}(Purple: One of us is a truth-teller, but not both of us){/color}"
        "{color=deaaff}(Purple: Go to the right){/color}"

        "Go to the left":
            jump badroom4

        "Go to the right":
            jump lab5


label badroom4:
    $currentstring-=1
    hide leftright
    hide orangepurple
    hide stringback
    show deadend
    show stringback
    with dissolve

    "{i}You have reached a dead end, with no way forward.{/i}"

    if currentstring > 0:
        "{i}You use a length of Ariadne’s thread to retrace your steps, returning to the previous room.{/i}"
        hide deadend
        hide sky1
        hide stringback
        hide screen stringbar
        with dissolve
        jump lab4

    if currentstring <= 0:
        "{i}You reach for Ariadne’s thread but realize in panic that it was exhausted some time ago. You search frantically for the path, but it is as if the halls and passages are new and unrecognizable. Have you fallen victim to the labyrinth’s curse?{/i}"
        "{i}You run, left and right, down the passages, only becoming more lost. You feel confused and dizzy, now unsure of where you are going and why you are here.{/i}"
        thes "These walls are made of wood. At the end of this labyrinth is the fearsome Medusa. I am a truth-teller."
        "{i}Theseus’s journey has come to an end. Try again?{/i}"
        return



label lab5:
    $currentstring-=1
    hide sky1
    hide leftright
    hide orangepurple
    hide stringback
    hide screen stringbar
    with dissolve

    centered "{i}A long straightway lays before you. In the distance, you see another branching path. But first, immediately before you, is a man you’ve not seen before.{/i}"

    show sky1
    show straight
    show ajax
    with dissolve

    ajax "Greetings, fellow traveller of the labyrinth. I am Ajax."
    thes "And are you among the honest or the dishonest of this maze’s inhabitants?"
    ajax "I am of course, among the honest."
    thes "But why should I believe that? The same would be said by a liar."
    ajax "Ah yes, but as I’m sure you now know, the liars of this maze can speak only lies and never truth. So to prove my honesty, I tell you this: the sky is blue, your sword is sharp, and Zeus is mighty."
    thes "Very well then! I agree that you must be an honest man. But the path ahead is straight, so I have no need of your advice. Please step aside and I shall be on my way."
    ajax "But I have a gift for you. And I will give it, so long as you can assure me that you are indeed Theseus, my prince. If you are him, I trust you have met the Cretan princess Ariadne. As it happens, so have I."
    ajax "Now tell me, Theseus, so that I may be reassured – what does Ariadne look like?"
    "{i}You feel the effects of the labyrinth clouding your mind, and even the recent image of Ariadne is as hazy as an encounter from childhood.{/i}"

label maidens:
    "{i}You recall the appearances of maidens you’ve met recently. Which of them is the princess Ariadne?{/i}"

    hide ajax
    show ariadne
    show helena
    show redblue
    with dissolve

    menu:
        "{i}Which of them is the princess Ariadne?{/i}"

        "Describe the left-most person":
            $ goosevar = "won"
            jump gooseright
        "Describe the person second from left":
            $ goosevar = "loss"
            jump goosewrong
        "Describe the person second from right":
            $ goosevar = "loss"
            jump goosewrong
        "Describe the right-most person":
            $ goosevar = "loss"
            jump goosewrong
        "Look at the maidens again":
            $ goosevar = "loss"
            jump maidens


label gooseright:
    hide ariadne
    hide helena
    hide redblue
    show ajax
    with dissolve
    ajax "Exactly as I remember her! You are indeed Theseus, come to save us. And so I shall give you this gift, that it may bring you good fortune and many eggs."
    "{i}Ajax reveals a large goose from under his robes, which he must have hidden at some discomfort to both himself and the goose.{i}"
    thes "I don’t understand this strange gift. Nonetheless, you have my gratitude, fellow Athenian! I will repay you in coin once we’ve escaped the bounds of this labyrinth."
    hide ajax
    with dissolve
    jump lab6intro


label goosewrong:
    hide ariadne
    hide helena
    hide redblue
    show ajax
    with dissolve

    ajax "That is not the Ariadne I know of. Perhaps you are not the honest hero I expected. No, you are as confused as all the others in this maze."
    "{i}The man turns away from you and strolls off in the direction you came. From behind, you hear a strange bird sound– the honk of a goose? – but continue down the hall.{/i}"

    hide ajax
    hide straight
    hide sky1
    hide screen stringbar
    hide stringback
    with dissolve
    jump lab6intro


label lab6intro:
    hide straight
    hide sky1
    hide stringback
    with dissolve

    centered "{i}As you follow the path, you encounter a pair of Athenian men. They have a strange look to their faces, as if their minds are already returned to Athens, eating olives in the agora.{/i}"


label lab6:
    show sky1
    show leftright
    show stringback
    show browngrey
    with dissolve
    show screen stringbar
    $currentstring-=1

    bc "He and I are both truth-tellers, or we’re both liars."
    grc "He would say that I’m a truth-teller."
    "{i}You can ask only one of them for directions. Who do you ask?{/i}"

    menu:
        "{color=c38e70}(Brown: He and I are both truth-tellers, or we’re both liars){/color}"
        "{color=adb5bd}(Grey: He would say that I’m a truth-teller){/color}"
        "{i}You can ask only one of them for directions. Who do you ask?{/i}"

        "Ask Brown which way to go":
            jump brown1
        "Ask Grey which way to go":
            jump grey1

label brown1:
    bc "Go to the right."

    menu:
        "{color=c38e70}(Brown: He and I are both truth-tellers, or we’re both liars){/color}"
        "{color=adb5bd}(Grey: He would say that I’m a truth-teller){/color}"
        "{color=c38e70}(Brown: Go to the right){/color}"

        "Go to the left":
            jump badroom6
        "Go to the right":
            jump lab7intro

label grey1:
    grc "Go to the right."

    menu:
        "{color=c38e70}(Brown: He and I are both truth-tellers, or we’re both liars){/color}"
        "{color=adb5bd}(Grey: He would say that I’m a truth-teller){/color}"
        "{color=adb5bd}(Grey: Go to the right){/color}"

        "Go to the left":
            jump badroom6
        "Go to the right":
            jump lab7intro


label badroom6:

    $currentstring-=1
    hide leftright
    hide stringback
    hide browngrey
    show deadend
    show stringback
    with dissolve

    "{i}You have reached a dead end, with no way forward.{/i}"

    if currentstring > 0:
        "{i}You use a length of Ariadne’s thread to retrace your steps, returning to the previous room.{/i}"
        hide deadend
        hide sky1
        hide screen stringbar
        hide stringback
        with dissolve
        jump lab6

    if currentstring <= 0:
        "{i}You reach for Ariadne’s thread but realize in panic that it was exhausted some time ago. You search frantically for the path, but it is as if the halls and passages are new and unrecognizable. Have you fallen victim to the labyrinth’s curse?{/i}"
        "{i}You run, left and right, down the passages, only becoming more lost. You feel confused and dizzy, now unsure of where you are going and why you are here.{/i}"
        thes "These walls are made of wood. At the end of this labyrinth is the fearsome Medusa. I am a truth-teller."
        "{i}Theseus’s journey has come to an end. Try again?{/i}"
        return

label lab7intro:
    hide sky1
    hide browngrey
    hide leftright
    hide straight
    hide stringback
    hide screen stringbar

    centered "{i}You continue onward, following one winding path after another. You sense that the endpoint of the labyrinth is near and that you will soon encounter the minotaur.{/i}"
    centered "{i}You reach another split road.{/i}"


label lab7:
    show sky1
    show leftright
    show stringback
    show screen stringbar
    with dissolve

    "{i}You look to the floor to see if another etching is marked there, but the stones appear flat and unscratched. You peer down each path but see nothing to distinguish between them.{/i}"

    show stereogram
    with dissolve

    "{i}Frustrated and tired, you sit down to meditate, relaxing your eyes as you peer at the stone wall before you…{/i}"

    menu:
        "Go to the left":
            jump badroom7

        "Go to the right":
            jump endinstructions

        "Look again at the stone wall":
            jump lab7


label badroom7:
    $currentstring-=1
    hide leftright
    hide stereogram
    hide stringback
    show deadend
    show stringback
    with dissolve

    "{i}You have reached a dead end, with no way forward.{/i}"

    if currentstring > 0:
        "{i}You use a length of Ariadne’s thread to retrace your steps, returning to the previous room.{/i}"
        hide deadend
        hide sky1
        hide stringback
        hide screen stringbar
        with dissolve
        jump lab7

    if currentstring <= 0:
        "{i}You reach for Ariadne’s thread but realize in panic that it was exhausted some time ago. You search frantically for the path, but it is as if the halls and passages are new and unrecognizable. Have you fallen victim to the labyrinth’s curse?{/i}"
        "{i}You run, left and right, down the passages, only becoming more lost. You feel confused and dizzy, now unsure of where you are going and why you are here.{/i}"
        thes "These walls are made of wood. At the end of this labyrinth is the fearsome Medusa. I am a truth-teller."
        "{i}Theseus’s journey has come to an end. Try again?{/i}"
        return


###################### getting advisors ######################################################
label endinstructions:

    hide stereogram
    hide sky1
    hide sky2
    hide screen stringbar
    hide leftright
    hide athenians
    with dissolve

    centered "{i}As you venture further into the labyrinth, the winding corridors and intersections give way to a straight path – a hallway at the end of which you can faintly see a series of doors. An Athenian clad in white approaches:{/i}"

    show sky3
    show straight
    show white
    with dissolve

    wc "Ah! The brave prince Theseus! I am Orion. You have no doubt come to save us from this torturous maze?"
    thes "I have. And from your words I know that you are among the truth-tellers of my kin. So tell me: where is the minotaur, that I may slay it?"
    wc "The minotaur is at the end of this hall; that much is known. But as noble as you are, you cannot defeat it in combat, for its strength far exceeds that of any man."
    thes "So what must I do?"
    wc "As night comes, the minotaur rests, laying behind a curtained door. One swift strike of your sword through the curtain may – if Tyche favours you - end its life."
    thes "Then that is what I shall do!"
    wc "But wait! For Daedalus created several other such rooms, each of which holds a great treasure of the land: the Golden Fleece, Heracles’s Bow, the Shield of Achilles, and the Sword of Peleus."
    wc "I fear that if you strike into one of these rooms of treasure you’ll succeed only in awakening the beast, and shall soon thereafter be devoured."
    thes "Do you know which room is which?"
    wc "Alas, I do not. But our fellow Athenians, who rest in this hallway, surely do."
    wc"Choose among them they will surely off the knowledge you need. But choose these advisors carefully, for among them are deceivers who will just as surely lead you astray."
    thes "Many thanks for this wisdom, dear friend!"
    wc "Godspeed, Theseus!"

    hide white
    hide sky3
    hide straight
    with dissolve


label advisor1:
    centered "{i}As you depart from the honest man, you see a pair of Athenians down the hall and stop to hear their words.{/i}"
    show sky3
    show straight
    show athenians
    with dissolve

    yc "Either I’m a truth-teller or Green is."
    gc "Yellow is a liar."
    "{i}You can ask only one of these Athenians to join you as an advisor. Who do you choose?{/i}"

    menu:
        "{color=#ffba08}(Yellow: Either I’m a truth-teller or Green is){/color}"
        "{color=#90be6d}(Green: Yellow is a liar){/color}"
        "{color=#FFFFFF}{i}You can ask only one of these Athenians to join you as an advisor. Who do you choose?{/i}{/color}"


        "Ask Yellow to join you.":
            $ comp1 = "Correct"
            "{i}The Athenian joins you.{/i}"

        "Ask Green to join you.":
            $ comp1 = "Incorrect"
            "{i}The Athenian joins you.{/i}"


label advisor2:
    hide athenians
    hide sky3
    hide straight
    with dissolve

    centered "{i}You venture further along the path, seeing another pair of captives. Neither speaks as you approach. However, upon the stone floor of the path you notice an unusual pattern.{/i}"

    show sky3
    show straight
    show redblue with dissolve

label advisor2puzzle:

    "{i}You attempt to relax your eyes and meditate, since this approach provided guidance earlier, but no image appears. Perhaps you should look more closely at the rocks.{/i}"

    hide redblue
    with dissolve
    show upside
    with dissolve

    "{i}You can ask only one of these Athenians to join you as an advisor. Who do you choose?{/i}"

    menu:
        "{i}You can ask only one of these Athenians to join you as an advisor. Who do you choose?{/i}"

        "Ask Red to join you":
            $ comp2 = "Correct"


        "Ask Blue to join you":
            $ comp2 = "Incorrect"

        "Look at the wall again":
            jump advisor2puzzle

label advisor3:
    hide upside
    hide redblue
    hide sky3
    hide straight
    with dissolve

    centered "{i}You proceed down the passage, now with two of your people following. Again you encounter a pair of Athenians.{/i}"

    show sky3
    show straight
    show orangepurple
    with dissolve

    oc "Either we’re both truth-tellers or we’re both liars."
    pc "One of us is a truth-teller and the other is a liar."
    "{i}You can ask only one of these Athenians to join you as an advisor. Who do you choose?{/i}"

    menu:
        "{color=ff9e00}(Orange: Either we’re both truth-tellers or we’re both liars){/color}"
        "{color=#deaaff}(Purple: One of us is a truth-teller and the other is a liar){/color}"
        "{i}You can ask only one of these Athenians to join you as an advisor. Who do you choose?{/i}"

        "Ask Orange to join you":
            $ comp3 = "Incorrect"

        "Ask Purple to join you":
            $ comp3 = "Correct"


label advisor4:
    hide sky3
    hide orangepurple
    hide straight

    centered "{i}The third Athenian joins your growing band. Though you are nearing the end of the passageway, two more people stand between you and the sleeping minotaur.{/i}"

    show sky3
    show straight
    show browngrey
    with dissolve

label advisor4puzzle:

    "{i}Neither speaks, but again you see a mysterious pattern on the ground.{/i}"

    hide browngrey
    show stereo2
    with dissolve

    "{i}You can ask only one of these Athenians to join you as an advisor. Who do you choose?{/i}"

    menu:
        "{i}You can ask only one of these Athenians to join you as an advisor. Who do you choose?{/i}"

        "Ask Brown to join you":
            $ comp4 = "Correct"

        "Ask Grey to join you":
            $ comp4 = "Incorrect"

        "Look at the ground again":
            jump advisor4puzzle

label curtains:
    hide stereo2
    hide straight
    hide sky3
    hide browngrey
    with dissolve
    play music "audio/sb_pathfinder.mp3" fadein 2

    centered "{i}With four fellow Athenians at your side, you tread cautiously to the end of the hall.{/i}"

    centered "{i}The passage widens, and a wall stands before you, with five doorways and five curtains.\n
    Behind one of those doorways lies the minotaur. Behind the others are the lost treasures of the gods.\n
    Though the treasures are tempting, they cannot distract from your mission.{/i}\n"

    show doors
    with dissolve

    "{i}You turn to the other Athenians for guidance. {u}Remember: the advice they provide will only be accurate if they are indeed truth-tellers. If there are liars among them, they may lead you astray.{/u}"
    "{i}To succeed in slaying the minotaur and saving your people, {u}correctly identify the minotaur’s room or all will be lost.{/u}{/i}"

    if comp1 == "Correct":
        yc "The Shield is to the immediate right of the Fleece."

    if comp1 == "Incorrect":
        gc "The Shield is to the immediate left of the Fleece."

    if comp2 =="Correct":
        rc "Neither the Sword nor the Minotaur are next to the Bow."

    if comp2 == "Incorrect":
        blc "Neither the Sword nor the Shield are next to the Bow."

    if comp3 =="Correct":
        pc "Neither the Minotaur nor the Sword are next to the Shield."

    if comp3 == "Incorrect":
        oc "Neither the Shield nor the Sword are next to the Minotaur."

    if comp4 =="Correct":
        bc "Neither the Sword nor the Bow are next to the Fleece."

    if comp4 == "Incorrect":
        grc "Neither the Fleece nor the Bow are next to the Shield."


label decision:


    menu:


        "Stab your sword through the 1st door":
            jump wrongstab

        "Stab your sword through the 2nd door":
            jump foundminotaur

        "Stab your sword through the 3rd door":
            jump wrongstab

        "Stab your sword through the 3rd door":
            jump wrongstab

        "Stab your sword through the 5th door":
            jump wrongstab

        "You need to hear from the advisors again":
            jump advisorsum

label advisorsum:

    if comp1 == "Correct":
        yc "The Shield is to the immediate right of the Fleece."

    if comp1 == "Incorrect":
        gc "The Shield is to the immediate left of the Fleece."

    if comp2 =="Correct":
        rc"Neither the Sword nor the Minotaur are next to the Bow."

    if comp2 == "Incorrect":
        blc "Neither the Sword nor the Shield are next to the Bow."

    if comp3 =="Correct":
        pc "Neither the Minotaur nor the Sword are next to the Shield."

    if comp3 == "Incorrect":
        oc "Neither the Shield nor the Sword are next to the Minotaur."

    if comp4 =="Correct":
        bc "Neither the Sword nor the Bow are next to the Fleece."

    if comp4 == "Incorrect":
        grc "Neither the Fleece nor the Bow are next to the Shield."


    jump decision

label wrongstab:
    hide doors
    hide athenians

    centered "{i}You step toward the door and slowly unsheathe Ariadne’s sword. Saying a silent prayer to Athena, you draw the sword back and plunge it through the curtain…{/i}"

    show empty
    with dissolve

    "{i}…only to strike the empty air! Below, you see a glorious treasure of the gods, and reach to take it.{/i}"

    play sound "audio/minotaur.mp3"
    show minotaur
    with dissolve

    "{i}Theseus, the brave would-be hero of Athens, has fallen.{/i}"

    jump badend


label foundminotaur:
    hide doors
    hide athenians
    play sound "audio/minotaur.mp3"
    show empty
    show deadminotaur
    with dissolve
    pause 3.0
    "{i}…and the minotaur falls in a grotesque heap of man and beast!{/i}"
    "{i}A gasp arises from the surrounding Athenians.{/i}"

    wc "Theseus, you have done it! The minotaur is defeated, and the terrible burden of Athens is lifted!"
    thes "As was my destiny."
    wc "Now, let us leave, for the labyrinth’s exit is through the minotaur’s room."
    thes "Follow me, then, and we shall fly the white flag of victory as we return to our home."

    jump goodend


label badend:

    hide empty
    hide minotaur
    with dissolve
    play music "audio/sb_reverie.mp3"
    show sea
    show blackship
    with dissolve
    pause 2.0
    jump attribution

label goodend:
    hide deadminotaur
    hide empty
    with dissolve
    play music "audio/sb_reverie.mp3"
    show sea
    show whiteship
    with dissolve

    "{i}You, Theseus, have rescued the prisoners of Daedalus’s labyrinth. You return to Athens as the future king, bringing with you the surviving Athenians as well as the treasure of the labyrinth:{/i}"
    "{i}The Golden Fleece{/i}"
    "{i}Heracles’s Bow{/i}"
    "{i}The Shield of Achilles{/i}"
    "{i}The Sword of Peleus{/i}"

    if goosevar == "won":
        jump goosescreen
    jump attribution

    if goosevar == "loss":
        jump attribution


label goosescreen:
    hide sea
    hide whiteship
    with dissolve

    "{i}and the greatest treasure of all,{/i}"

    show open
    show goose
    with dissolve
    play sound "audio/goose.mp3"

    "{i}one gorgeous goose!{/i}"
    jump attribution


label attribution:
    hide goose
    hide open
    hide sea
    hide whiteship
    hide blackship

    centered "Credits\n
    Written by Stephen Latta\n
    Programmed by Tanya Yeomans"
    centered "Voice Acting by Kevin Buchanan"

    centered "Music by Scott Buckley:\n
    Chasing Daylight - {a=https://www.scottbuckley.com.au/library/chasing-daylight/}https://www.scottbuckley.com.au/library/chasing-daylight/{/a}\n
    Pathfinder - {a=https://www.scottbuckley.com.au/library/pathfinder/}https://www.scottbuckley.com.au/library/pathfinder/{/a}\n
    Reverie - {a=https://www.scottbuckley.com.au/library/reverie/}https://www.scottbuckley.com.au/library/reverie/{/a}"

    centered "Backgrounds\n
    \n
    \"Ancient wall from Constantinople\” by ashabot is licensed under CC BY-NC-SA 2.0, {a=https://www.flickr.com/photos/37912373962@N01/17722884819}https://www.flickr.com/photos/37912373962@N01/17722884819{/a}. Image extensively modified; revised version available at {a=https://www.flickr.com/photos/193346300@N06/51274002784/}https://www.flickr.com/photos/193346300@N06/51274002784/{/a}\n
    \“Agios Andreas, Epidavros, Greece: South room of the ruined house at the Arvanitian Vlachokiriakeika\” by Schuppi is licensed under CC BY-SA 4.0, {a=https://commons.wikimedia.org/wiki/File:Vlachokiriakeika_06.JPG}https://commons.wikimedia.org/wiki/File:Vlachokiriakeika_06.JPG{/a}. Image extensively modified; revised version available at {a=https://www.flickr.com/photos/193346300@N06/51272530927/}https://www.flickr.com/photos/193346300@N06/51272530927/{/a}
    \“The Brimstone Hill Fortress on the island of St. Kitts, which was recognized World Heritage Site by the UNESCO in 1999\” by Martin Falbisoner is licensed under CC BY-SA 4.0, {a=https://commons.wikimedia.org/wiki/File:Saint_Kitts_-_Brimstone_Hill_Fortress_05.JPG}https://commons.wikimedia.org/wiki/File:Saint_Kitts_-_Brimstone_Hill_Fortress_05.JPG{/a}. Image extensively modified; revised version available at {a=https://www.flickr.com/photos/193346300@N06/51273459018/}https://www.flickr.com/photos/193346300@N06/51273459018/{/a}\n
    \“Ancient Corinth Ruins\” by Erik Drost is licensed under CC BY 2.0, {a=https://flickr.com/photos/62091376@N03/5987150330}https://flickr.com/photos/62091376@N03/5987150330{/a}. Image extensively modified\n
    \“mirrored curtains\” by glasseyes view is licensed under CC BY-NC-SA 2.0, {a=https://www.flickr.com/photos/74708580@N00/9968216153}https://www.flickr.com/photos/74708580@N00/9968216153{/a}. Image extensively modified; revised version available at {a=https://www.flickr.com/photos/193346300@N06/51274295995}https://www.flickr.com/photos/193346300@N06/51274295995{/a}\n
    Hallway: CC0 1.0, {a=https://pxhere.com/en/photo/1351365}https://pxhere.com/en/photo/1351365{/a}\n
    Wall: CC0 1.0, {a=https://pxhere.com/pt/photo/1616354}https://pxhere.com/pt/photo/1616354{/a}\n
    Sky Texture 1: CC0 1.0,{a=https://pxhere.com/pt/photo/1616354}https://pxhere.com/pt/photo/1616354{/a}\n
    Sky Texture 2: CC0 1.0, {a=https://pxhere.com/en/photo/667822}https://pxhere.com/en/photo/667822{/a}\n
    Sky Texture 3: CC0 1.0, {a=https://pxhere.com/en/photo/1643067}https://pxhere.com/en/photo/1643067{/a}\n
    Sky Texture 4: CC0 1.0, {a=https://pxhere.com/en/photo/804994}https://pxhere.com/en/photo/804994{/a}"

    centered "People\n
    \n
    Beach, Chandler B. The New Student’s Reference Work: for teachers, students and families. F.E. Compton and Company, 1914. {a=https://commons.wikimedia.org/wiki/File:LA2-NSRW-2-0064_(1-7).jpg}https://commons.wikimedia.org/wiki/File:LA2-NSRW-2-0064_(1-7).jpg{/a}\n
    Kretschmer, Albert, and Dr. Carl Rohrbach, The Costumes of All Nations, Henry Sotheran & Co, 1882. {a=https://commons.wikimedia.org/wiki/File:Ancient_Times,_Greek._-_009_-_Costumes_of_All_Nations_(1882).JPG}https://commons.wikimedia.org/wiki/File:Ancient_Times,_Greek._-_009_-_Costumes_of_All_Nations_(1882).JPG{/a} and {a=https://commons.wikimedia.org/wiki/File:Ancient_Times,_Greek._-_011_-_Costumes_of_All_Nations_(1882).JPG}https://commons.wikimedia.org/wiki/File:Ancient_Times,_Greek._-_011_-_Costumes_of_All_Nations_(1882).JPG{/a}."

    centered "Other Images\n
    \n
    \“1:10 models Roman ships, 1: cargo ship based on the London-Blackfriars wreck dated to about 150 AD, 3: model based on the Oceanus mosaic fom Bad Kreuznach, Museum für Antike Schiffahrt, Mainz\” by Carole Raddato is licensed under CC BY-SA 2.0, {a=https://commons.wikimedia.org/wiki/File:Blackfriars_I_ship_model.jpg}https://commons.wikimedia.org/wiki/File:Blackfriars_I_ship_model.jpg{/a}. Image extensively modified; revised version available at {a=https://www.flickr.com/photos/193346300@N06/51273483043}https://www.flickr.com/photos/193346300@N06/51273483043{/a}\n
    \“A Greylag Goose\” by Jdforresteris licensed under CC BY 1.0, {a=https://commons.wikimedia.org/w/index.php?curid=26109}https://commons.wikimedia.org/w/index.php?curid=26109{/a}. Image extensively modified.\n
    Minotaur: by Parker_West, licensed under Pixabay License, {a=https://pixabay.com/ko/illustrations/%%ec%%bc%%84-%%ed%%83%%80-%%ec%%9a%%b0-%%eb%%a3%%a8%%ec%%8a%%a4-%%eb%%af%%b8%%eb%%85%%b8%%ed%%83%%80%%ec%%9a%%b0%%eb%%a1%%9c%%ec%%8a%%a4-3329266}https://pixabay.com/ko/illustrations/%%ec%%bc%%84-%%ed%%83%%80-%%ec%%9a%%b0-%%eb%%a3%%a8%%ec%%8a%%a4-%%eb%%af%%b8%%eb%%85%%b8%%ed%%83%%80%%ec%%9a%%b0%%eb%%a1%%9c%%ec%%8a%%a4-3329266/{/a}\n
    \“Bull Head - symbol of Baal Hadad\” by Camocon licensed under CC0 1.0, {a=https://commons.wikimedia.org/wiki/File:Bull_head.png}https://commons.wikimedia.org/wiki/File:Bull_head.png{/a}"

    centered "Puzzles\n
    \n
    Knights and Knaves Puzzles adapted from those on Dr. Joe Lau and Dr. Jonathan Chan’s Critical Thinking website: {a=https://philosophy.hku.hk/think/logic/knights.php}https://philosophy.hku.hk/think/logic/knights.php{/a}\n
    Stereogram created with {a=https://www.easystereogrambuilder.com/}https://www.easystereogrambuilder.com/{/a}\n
    Maze created with {a=http://www.mazegenerator.net/}http://www.mazegenerator.net/{/a}\n
    \n
    Some puzzles inspired by Nintendo’s Professor Layton video game series."


    return
