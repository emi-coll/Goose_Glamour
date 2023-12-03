# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define t = Character("Tutorial", color = "#0d2a0f", what_color = "#37a33e")
define n = Character("Narrator", color = "#d24dff")
define d = Character("Game Creators", color= "#5500ff")

# these variables are needed to display an outfit outside of the dress up minigame, also helps with point system - E.C.
#Variable for level 0
default accessory_0 = "a000"
default headwear_0 = "a000"
default topDress_0 = "a000"
default socksTights_0 = "a000"
default shoes_0 = "a000"
default coat_0 = "a000"

#Variables for level 1
default accessory_1 = "a000"
default headwear_1 = "a000"
default topDress_1 = "a000"
default socksTights_1 = "a000"
default shoes_1 = "a000"
default coat_1 = "a000"

#Variables for level 2
default accessory_2 = "a000"
default headwear_2 = "a000"
default topDress_2 = "a000"
default socksTights_2 = "a000"
default shoes_2 = "a000"
default coat_2 = "a000"

#Variables for level 3
default accessory_3 = "a000"
default headwear_3 = "a000"
default topDress_3 = "a000"
default socksTights_3 = "a000"
default shoes_3 = "a000"
default coat_3 = "a000"

# The game starts here.

label start:
   
    scene temp backgroundd 

    t "Welcome to Glamour Goose! You are a student at the University of Watergoose\
    and every day is another chance to show off your fashion skills."
    
    t "By choosing an outfit that fits each scenario’s theme, you can win special items and move\
    onto the next level! Maybe you’ll even unlock a hidden level ;)"
    
    t "Click on the clothing item to put it on. If you want to take it off, click on\
    the empty box."

    t "Each clothing item has different tags that correspond to the different\
    categories of clothes: {i}Cute, Elegant, Goth, Formal, Casual, and Active{/i}." 
    
    t "For each level, pay attention to keywords in the dialogue that hint towards which\
    categories you should wear."

    scene wloo outside

    n "It’s your first day at Watergoose! The first thing on your schedule is a CHE\
    120 lecture with Professor Pendar. Why don’t you put something {b}casual{/b} on?"
    
    call screen startdress0
    
    label doneLVL0:

        hide screen startdress0
        hide screen dress_ui0

        hide screen goosebase

        hide screen headwearNull
        hide screen headwear1
        hide screen headwear2
        hide screen headwear3

        hide screen coatNull
        hide screen coat1
        hide screen coat2
        hide screen coat3

        hide screen topDressNull
        hide screen topDress1
        hide screen topDress2
        hide screen topDress3

        hide screen socksTightsNull
        hide screen socksTights1
        hide screen socksTights2
        hide screen socksTights3

        hide screen shoesNull
        hide screen shoes1
        hide screen shoes2
        hide screen shoes3

        hide screen accessoryNull
        hide screen accessory1
        hide screen accessory2
        hide screen accessory3

        scene wloo outside

        show goose_0 at center

        $ statement0 = calculate_points(accessory_0, headwear_0, coat_0, topDress_0, socksTights_0, shoes_0)

        n "Casual Rank: [statement0[2]]"

        if statement0[2] == "B" or statement0[2]== "A" or statement0[2]=="S":
            
            n "Congrats! Pendar loved your outfit :) You’ve won a green dot accessory."

            jump startlvl1

        else:

            n "Oh no! Your outfit isn’t suitable for a lecture. Hint: Try something more casual."

            $ accessory_0 = "a000"
            $ headwear_0 = "a000"
            $ topDress_0 = "a000"
            $ socksTights_0 = "a000"
            $ shoes_0 = "a000"
            $ coat_0 = "a000"

            hide goose_0

            call screen startdress0

    label startlvl1:

        hide goose_0

        n "It’s almost the end of O Week at Watergoose. The last Frosh event is to earn \
        your hard hat by working with your friends to complete a series of challenges. \
        Let’s put something on that’s {b}cute{/b} and {b}active{/b}!"

        call screen startdress1

    label doneLVL1:

        hide screen startdress1
        hide screen dress_ui1

        hide screen goosebase

        hide screen headwearNull
        hide screen headwear1
        hide screen headwear2
        hide screen headwear3

        hide screen coatNull
        hide screen coat1
        hide screen coat2
        hide screen coat3

        hide screen topDressNull
        hide screen topDress1
        hide screen topDress2
        hide screen topDress3

        hide screen socksTightsNull
        hide screen socksTights1
        hide screen socksTights2
        hide screen socksTights3

        hide screen shoesNull
        hide screen shoes1
        hide screen shoes2
        hide screen shoes3

        hide screen accessoryNull
        hide screen accessory1
        hide screen accessory2
        hide screen accessory3
        hide screen accessorys1

        scene wloo outside

        show goose_1 at center

        $ statement1 = calculate_points(accessory_1, headwear_1, coat_1, topDress_1, socksTights_1, shoes_1)

        n "Cute Rank: [statement1[0]], Active Rank: [statement1[5]]"

        if (statement1[0] == "B" or statement0[0]== "A" or statement0[0]=="S") and (statement1[5]== "A" or statement1[5]== "S"):
            
            n "You’ve completed all the challenges and been awarded a hard hat! Good \
            luck on your journey to becoming an engigoose!"
            
            jump startlvl2

        else:

            n "Unfortunately, you weren’t able to complete all the challenges because \
            you were hindered by your outfit. Hint: Try something more active and/or cute."

            $ accessory_1 = "a000"
            $ headwear_1 = "a000"
            $ topDress_1 = "a000"
            $ socksTights_1 = "a000"
            $ shoes_1 = "a000"
            $ coat_1 = "a000"

            hide goose_1

            call screen startdress1

    label startlvl2:    
        return

    # This ends the game.

