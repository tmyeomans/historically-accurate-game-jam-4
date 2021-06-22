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

screen stringbar:
    text "String left: [currentstring]/[maxstring]" xalign 0.0 yalign 0.05
    bar value currentstring range maxstring xalign 0.0 yalign 0.1 xmaximum 1280


# The game starts here.
label start:


    $currentstring = 10
    $maxstring = 10

    jump lab1

    scene black

    centered "On the island of Crete lives the fearsome minotaur, roaming the passages of Daedalus’s labyrinth."
    centered "As a condition of peace, the people of Athens send 14 youths through the labyrinth gates every seven years."
    centered "None have returned."
    centered "Brave Theseus, you must end this folly. Speak with the princess Ariadne, enter the labyrinth, and…"
    centered "SLAY THE MINOTAUR"

    play music "audio/sb_chasingdaylight.mp3"
    centered "{size=100}{color=#f00}The Minotaur{/size}{/color}"




label introduction:

    ari "Theseus, my love, you’ve arrived! Your father allowed this?"
    thes "I gave him no choice. When the Minotaur is dead and I return to Athens, we shall fly the white flag of victory and my father will see me for the King that I am."
    ari "And if you fail?"
    thes "Then the flag shall be black."
    ari "Ariadne: By Zeus! I can’t bear that, Theseus. Let me help!"
    thes "I must go alone, in the footsteps of my countrymen."
    ari "But you need not go unarmed! Take this {u}sword{/u}, that you may slay the beast."
    ari "Ariadne: And take this length of {u}thread{/u}. If you follow the wrong path through the labyrinth, you can retrace your steps."

    centered "{i}When you reach a dead end, use the thread to backtrack. With each step forward or back, your thread count will deplete (see the meter at top of screen).{/i}"

    thes "My thanks, good Ariadne! And now I am ready."
    ari "Wait! There’s something more you must know. Many of the Athenians who’ve entered the labyrinth are still alive, but… changed. A strange madness afflicts them, perhaps caused by the terror of the Minotaur, or perhaps it’s some trickery of Dolos."
    ari "The Athenians inside are demented in one of two ways: some {u}speak only the truth{/u}. Others {u}speak only falsehoods.{/u}"
    thes "How will I know which is which?"
    ari "You must listen to what they say. I’ve brought my handmaiden, Helena, to demonstrate. We will each say one thing. Listen carefully."


label tutorial:
    hel "Ariadne and I are both truth tellers."
    ari "Helena is a liar."
    ari "Now who is telling the truth? Who is lying? Both of us? Neither of us?"



    menu:
        "{color=#C7D3BF}(Ariadne and I are both truth tellers){/color}"
        "{color=#ac46a1}(Helena is a liar){/color}"
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
    centered "{i}Theseus follows the wall of the great labyrinth until he finds an opening. And with that, his journey begins.{/i}"



label lab1:

    show sky1
    show leftright
    with dissolve



    show screen stringbar

    show athenians with dissolve
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
            jump correct

        "Go to ther right":
            jump badroom

label green1:

    gc "Go left"

    menu:
        "{color=#90be6d}Go to the left.{/color}"

        "Go to the left":
            jump correct

        "Go to the right":
            jump badroom





label correct:
        show min with dissolve

label badroom:
    hide block with dissolve
    centered "You picked the first block so you enter the door on your left."

    show min with dissolve




label R2_c:
    hide block with dissolve
    centered "You picked the third block so you enter the door on your right."




#add attribution for Scott Buckley Chasing Daylight
#https://www.scottbuckley.com.au/library/chasing-daylight/


    # This ends the game.

    return
