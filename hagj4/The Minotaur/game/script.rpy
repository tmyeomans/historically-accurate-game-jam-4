# The script of the game goes in this file.



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
     $ wc= Character("White",color = "#FFFFFF", what_color = "#FFFFFF")


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



screen stringbar:
    text "String left: [currentstring]/[maxstring]" xalign 0.0 yalign 0.05
    bar value currentstring range maxstring xalign 0.0 yalign 0.1 xmaximum 1280


# The game starts here.
label start:


    $currentstring = 10
    $maxstring = 10

    scene black

    centered "On the island of Crete lives the fearsome minotaur, roaming the passages of Daedalus’s labyrinth."
    centered "As a condition of peace, the people of Athens send 14 youths through the labyrinth gates every seven years."
    centered "None have returned."
    centered "Brave Theseus, you must end this folly. Speak with the princess Ariadne, enter the labyrinth, and…"
    play music "audio/minotaur.mp3"
    centered "SLAY THE MINOTAUR"

    play music "audio/sb_chasingdaylight.mp3"
    centered "{size=100}{color=#f00}The Minotaur{/size}{/color}"




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

    "{i}When you reach a dead end, use the thread to backtrack. With each step forward or back, your thread count will deplete (see the meter at top of screen).{/i}"
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
    ari "Ariadne: Ah, very clever of you, dear Theseus! Now set forth, and may the gods be with you."
    jump endtutorial


label endtutorial:
    hide helena
    hide ariadne
    hide open
    with dissolve
    centered "{i}Theseus follows the wall of the great labyrinth until he finds an opening. And with that, his journey begins.{/i}"

label lab1:
    $currentstring-=1

    show sky1
    show leftright
    show stringback
    show athenians
    show screen stringbar
    with dissolve

    yc "Either Green’s a truth teller or I am. But not both of us."
    gc "A liar would tell you that Yellow is a liar."

    menu:
        "{color=#ffba08} (Yellow: Either Green’s a truth teller or I am. But not both of us.){/color}"
        "{color=#90be6d} (Green: A liar would tell you that Yellow is a liar.){/color}"
        "You can ask only one of them for directions. Who do you ask?"

        "Ask Yellow which way to go.":
            jump yellow1


        "Ask Green which way to go.":
            jump green1

label yellow1:

    yc "Go left"

    menu:
        "{color=#ffba08}(Yellow: Either Green’s a truth teller or I am. But not both of us).{/color}"
        "{color=#90be6d}(Green: A liar would tell you that Yellow is a liar).{/color}"
        "{color=#ffba08}Yellow: Go to the left.{/color}"

        "Go to the left":
            jump correct1

        "Go to the right":
            jump badroom1

label green1:

    gc "Go left"

    menu:
        "{color=#90be6d}Go to the left.{/color}"

        "Go to the left":
            jump correct1

        "Go to the right":
            jump badroom1





label correct1:
    $currentstring-=1
    centered "Correct."
    ##################fix jump when more puzzles added
#    hide leftright
#    hide athenians
#    with dissolve
    jump endinstructions


label badroom1:
    $currentstring-=1

    hide leftright
    hide athenians
    show deadend
    with dissolve
############ fix text about dead end
    thes "text about dead end"
    hide deadend with dissolve
    jump lab1




label endinstructions:


    hide sky1
    hide sky2
    hide stringbar
    hide leftright
    hide athenians
    with dissolve
    centered "{i}As you venture further into the labyrinth, the winding corridors and intersections give way to a straight path – a hallway at the end of which you can faintly see a series of doors. An Athenian clad in white approaches:{/i}"
    show sky3
    show straight
    with dissolve


    wc "Ah! The brave prince Theseus! You have no doubt come to save us from this torturous maze?"
    thes "I have. And from your words I know that you are among the truth-tellers of my kin. So tell me: where is the minotaur, that I may slay it?"
    wc "The minotaur is at the end of this hall; that much is known. But as noble as you are, you cannot defeat it in combat, for its strength far exceeds that of any man."
    thes "So what must I do?"
    wc "As night comes, the minotaur rests, laying behind a curtained door. One swift strike of your sword through the curtain may – if Tyche favours you, end its life."
    thes "Then that is what I shall do!"
    wc "But wait! For Daedalus created several other such rooms, each of which holds a great treasure of the land: the Golden Fleece, Heracles’s Bow, the Shield of Achilles, and the Sword of Peleus."
    wc "I fear that if you strike into one of these rooms of treasure you’ll succeed only in awakening the beast, and shall soon thereafter be devoured."
    thes "Do you know which room is which?"
    wc "Alas, I do not. But our fellow Athenians, who rest in this hallway, surely do. Choose among them they will surely off the knowledge you need. But choose these advisors carefully, for among them are deceiver who will just as surely lead you astray."
    thes "Many thanks for this wisdom, dear friend!"
    wc "Godspeed, Theseus!"


label advisor1:
    show athenians
    with dissolve

    "{i}As you depart from the honest man, you see a pair of Athenians down the hall and stop to hear their words.{/i}"
    yc "Either I’m a truth-teller or Green is."
    gc "Yellow is a liar."
    "{i}You can ask only one of these Athenians to join you as an advisor. Who do you choose?{/i}"

    menu:
        "{color=#ffba08}(Yellow: Either I’m a truth-teller or Green is){/color}"
        "{color=#90be6d}(Green: Yellow is a liar){/color}"
        "{color=#FFFFFF}{i} You can ask only one of these Athenians to join you as an advisor. Who do you choose?{/i}{/color}"


        "Ask Yellow to join you.":
            $ comp1 = "Correct"
            "{i}The Athenian joins you.{/i}"

        "Ask Green to join you.":
            $ comp1 = "Incorrect"
            "{i}The Athenian joins you.{/i}"

label advisor2:

    "{i}You venture further along the path, seeing another pair of captives. Neither speaks as you approach. However, upon the stone floor of the path you notice an unusual pattern.{/i}"
    show upside
    with dissolve
    "{i}You can ask only one of these Athenians to join you as an advisor. Who do you choose?{/i}"

    menu:
        "{i}You can ask only one of these Athenians to join you as an advisor. Who do you choose?{/i}"

        "Ask Red to join you.":
            $ comp2 = "Correct"


        "Ask Blue to join you.":
            $ comp2 = "Incorrect"



label advisor3:
    hide upside
    with dissolve

    "{i}You proceed down the passage, now with two of your people following. Again you encounter a pair of Athenians.{/i}"

    oc "Either we’re both truth-tellers or we’re both liars."
    pc "One of us is a truth-teller and the other is a liar."
    "{i}You can ask only one of these Athenians to join you as an advisor. Who do you choose?{/i}"

    menu:
        "{color=ff9e00}(Orange: Either we’re both truth-tellers or we’re both liars){/color}"
        "{color=#deaaff}(Purple: One of us is a truth-teller and the other is a liar){/color}"
        "{i}You can ask only one of these Athenians to join you as an advisor. Who do you choose?{/i}"

        "Ask Orange to join you.":
            $ comp3 = "Incorrect"

        "Ask Purple to join you.":
            $ comp3 = "Correct"


label advisor4:
    "{i}The third Athenian joins your growing band.Though you are nearing the end of the passageway, two more people stand between you and the sleeping minotaur. Neither speaks, but again you see a set of mysterious markings on the ground.{/i}"
    show maze
    with dissolve

    "{i}You can ask only one of these Athenians to join you as an advisor. Who do you choose?{/i}"

    menu:
        "{i}You can ask only one of these Athenians to join you as an advisor. Who do you choose?{/i}"

        "Ask Brown to join you":
            $ comp4 = "Correct"

        "Ask Grey to join you.":
            $ comp4 = "Incorrect"


label curtains:
    hide maze
    hide straight
    hide sky3
    with dissolve
    play music "audio/sb_pathfinder.mp3" fadein 2
    centered "{i}With four fellow Athenians at your side, you tread cautiously to the end of the hall.{/i}"

    show doors
    with dissolve

    centered "{i}The passage widens, and a wall stands before you, with five doorways and five curtains. Behind one of those curtains lies the minotaur. Behind the others are the lost treasures of the gods.{/i}"
    centered "{i}You turn to the other Athenians, tempted by the treasures but knowing that {u}you must correctly identify the minotaur’s room{/u} or all will be lost. {/i}"

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


    menu:
        "Stab your sword through the 1st door.":
            jump wrongstab

        "Stab your sword through the 2nd door.":
            jump foundminotaur

        "Stab your sword through the 3rd door.":
            jump wrongstab

        "Stab your sword through the 3rd door.":
            jump wrongstab

        "Stab your sword through the 5th door.":
            jump wrongstab


label wrongstab:
    hide doors
    hide athenians
    centered "{i}You step toward the door and slowly unsheathe Ariadne’s sword. Saying a silent prayer to Athena, you draw the sword back and plunge it through the curtain…{/i}"
    show empty
    with dissolve
    centered "{i}…only to strike the empty air! Below, you see a glorious treasure of the gods, and reach to take it.{/i}"
    play sound "audio/minotaur.mp3"
    show minotaur
    with dissolve

    "{w}{i}Theseus, the brave would-be hero of Athens, has fallen.{/i}"
    jump badend

label foundminotaur:
    hide doors
    hide athenians
    play sound "audio/minotaur.mp3"
    show deadminotaur
    with dissolve

    centered "{i}…and the minotaur falls in a grotesque heap of man and beast!{/i}"
    centered "{i}A gasp arises from the surrounding Athenians.{/i}"
    ########################line from green here?

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

    jump attribution

label goodend:
    hide deadminotaur
    with dissolve
    play music "audio/sb_reverie.mp3"
    show sea
    show whiteship
    with dissolve
    "{i}You, Theseus, have rescued the prisoners of Daedalus’s labyrinth. You return to Athens as the future kind, bringing with you the surviving Athenians as well as the treasure of the labyrinth:{/i}"
    "{i}The Golden Fleece{/i}"
    "{i}Heracles’s Bow{/i}"
    "{i}The Shield of Achilles{/i}"
    "{i}The Sword of Peleus{/i}"

label goose:
    hide sea
    hide whiteship
    with dissolve

    "{i}and the greatest treasure of all,{/i}"
    show goose
    with dissolve
    play sound "audio/goose.mp3"
    "{i}one gorgeous goose!{/i}"
    jump attribution





label attribution:
    hide goose with dissolve

    centered "Music by Scott Buckley:\n
    Chasing Daylight - https://www.scottbuckley.com.au/library/chasing-daylight/\n
    Pathfinder - https://www.scottbuckley.com.au/library/pathfinder/\n
    Reverie - https://www.scottbuckley.com.au/library/reverie/"






    # This ends the game.

    return
