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

#Variables for level 4
default accessory_4 = "a000"
default headwear_4 = "a000"
default topDress_4 = "a000"
default socksTights_4 = "a000"
default shoes_4 = "a000"
default coat_4 = "a000"

#these are images that will be displayed later in the game
image happy goose = im.Scale("goose_happy.PNG", 431, 1000)
# The game starts here.

label start:
   
    scene temp backgroundd 
     
    #this dialogue is for the tutorial level/level 0 and sets up the context of the game for the player - E.L
    t "Welcome to Glamour Goose! You are a student at the University of Watergoose\
    and every day is another chance to show off your fashion skills."
    
    t "By choosing an outfit that fits each scenario’s theme, you can win special items and move\
    onto the next level! Maybe you’ll even unlock a hidden level ;)"
    #this dialgoue is instructions on how to actually select clothing items to create their outfits - E.L
    t "Click on the clothing item to put it on. If you want to take it off, click on\
    the empty box."
    #this dialogue informs the player about the category system and reminds them to keep each level's theme in mind for their outfit - E.L
    t "Each clothing item has different tags that correspond to the different\
    categories of clothes: {i}Cute, Elegant, Goth, Formal, Casual, and Active{/i}." 
    
    t "For each level, pay attention to keywords in the dialogue that hint towards which\
    categories you should wear."

    scene wloo outside

    #this is the dialogue for the first level of the game dictated by the narrator instead of the tutorial - E.L
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
            #these dialgoue statements tell the player if they've passed or failed the level - E.L
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
        #this is the dialogue for the second level of the game - E.L
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
            #these dialgoue statements tell the player if they've passed or failed the level and what item they've won by passing - E.L
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
        
        scene wloo outside

        hide goose_1
        #this is the dialogue for the third level of the game - E.L
        n "It’s time to relax after your midterms. Isn’t there a Noon Hour concert that\
        features different musical theatre songs later today? Call your friends to join you and get\
        dressed up in something {b}elegant{/b}!"

        call screen startdress2

    label doneLVL2:

        hide screen startdress2
        hide screen dress_ui2

        hide screen goosebase

        hide screen headwearNull
        hide screen headwear1
        hide screen headwear2
        hide screen headwear3
        hide screen headwears1

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

        scene opera
        show goose_2 at center

        $ statement2 = calculate_points(accessory_2, headwear_2, coat_2, topDress_2, socksTights_2, shoes_2)

        n "Elegant Rank: [statement2[4]]"

        if statement2[4]=="B" or statement2[4]=="A" or statement2[4]=="S":
            #these dialgoue statements tell the player if they've passed or failed the level and what item they've won by passing- E.L
            n "You’re looking very classy for the concert! You’ve won an opera monocole."

            jump startlvl3

        else:

            n "Oh no, your outfit doesn’t fit the concert dress code :( Hint: Try something more elegant."

            $ accessory_2 = "a000"
            $ headwear_2 = "a000"
            $ topDress_2 = "a000"
            $ socksTights_2 = "a000"
            $ shoes_2 = "a000"
            $ coat_2 = "a000"

            hide goose_2

            call screen startdress2

    label startlvl3:

        scene wloo outside
        hide goose_2
        #this is the dialogue for the fourth level of the game - E.L
        n "It’s co-op application season… But the good thing is, you’ve secured an interview \
        with Professor Pendar to discuss the possibilities of being one of her research assistants. \
        To make a good impression, wear something {b}formal{/b} to the interview."

        call screen startdress3

    label doneLVL3:
        
        hide screen startdress3
        hide screen dress_ui3

        hide screen goosebase

        hide screen headwearNull
        hide screen headwear1
        hide screen headwear2
        hide screen headwear3
        hide screen headwears1
        hide screen headwears2

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
        show goose_3 at center

        $ statement3 = calculate_points(accessory_3, headwear_3, coat_3, topDress_3, socksTights_3, shoes_3)

        n "Formal Rank: [statement3[3]]"

        if statement3[3]=="A" or statement3[3]=="S":
            #these dialgoue statements tell the player if they've passed or failed the level and the item they've won by passing - E.L
            n "Good work! Professor Pendar seemed impressed with your appearance and interview skills.\
            Hopefully you get the job! You’ve won a rubber duck to help you with coding."

            if statement0[1] == "B" and statement1[1] == "B" and statement2[1] == "B" and statement3[1] == "B":
                
                hide goose_3
                show happy goose at center
                #this dialogue tells the player they've unlocked the secret goth date level and have an additional level to complete - E.L
                n "Yippee! You’ve unlocked the secret goth level :) You’re going on a goth date with \
                your goose crush in an hour. Quick, put on your best {b}goth{/b} outfit to leave a mysterious \
                and lingering impression!"

                call screen startdress4

            else: 
                jump donegame

        else:
            n "Professor Pendar didn’t seem too impressed with what you wore… Hint: Try something more formal."

            $ accessory_3 = "a000"
            $ headwear_3 = "a000"
            $ topDress_3 = "a000"
            $ socksTights_3 = "a000"
            $ shoes_3 = "a000"
            $ coat_3 = "a000"

            hide goose_3

            call screen startdress3
    
    label doneLVL4:

        hide screen startdress4
        hide screen dress_ui4

        hide screen goosebase

        hide screen headwearNull
        hide screen headwear1
        hide screen headwear2
        hide screen headwear3
        hide screen headwears1
        hide screen headwears2
        hide screen headwears3

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
        show goose_4 at center

        $ statement4 = calculate_points(accessory_4, headwear_4, coat_4, topDress_4, socksTights_4, shoes_4)

        n "Goth Rank: [statement4[1]]"

        if statement4[1] == "A" or statement4[1] == "S":
            #these dialgoue statements tell the player if they've passed or failed the secret final level - E.L
            n "You had such a great time you’re going out on another date again next week! What a \
            happy goose couple!"

            jump donegame

        else: 

            n "Because you didn’t fit the dress code of the date venue, you and your goose crush \
            had to awkwardly leave and go somewhere else :( Hint: Try something more goth."

            call screen startdress4

    label donegame:
        
        hide goose_3
        hide goose_4

        scene wloo outside

        show happy goose at center
        #this dialogue tells the player the game is over - E.L
        n "What an eventful week it’s been! So much to do and learn now that you’re at the University \
        of Watergoose. I wonder what outfit you’ll wear tomorrow?"
        #this dialogue is just a thank you to the player from us for playing the game :) - E.L
        d "Thank you so much for playing Goose Glamour! We hope you had lots of fun dressing up your \
        goose persona :)"
        
        return
    # This ends the game.

