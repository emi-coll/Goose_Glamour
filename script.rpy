# The script of the game goes in this file - EC

#Initializing music - IC
define audio.wario = "garlic jam (an album made in warioware d.i.y).mp3"

# Declare characters used by this game. The color argument colorizes the
# name of the character and the text they "say" - EC
define t = Character("Tutorial", color = "#0d2a0f", what_color = "#37a33e")
define n = Character("Narrator", color = "#d24dff")
define d = Character("Game Creators", color = "#5500ff")
define p = Character("Professor Pendar", colour = "#811313")

# these variables are needed to display an outfit outside of the dress up minigame, also helps with point system - E.C.
# they are set to "a000" at the start of the game since this string in the point code has values of 0 for every category - EC

#Variables for level 0 - EC
default accessory_0 = "a000"
default headwear_0 = "a000"
default topDress_0 = "a000"
default socksTights_0 = "a000"
default shoes_0 = "a000"
default coat_0 = "a000"

#Variables for level 1 - EC
default accessory_1 = "a000"
default headwear_1 = "a000"
default topDress_1 = "a000"
default socksTights_1 = "a000"
default shoes_1 = "a000"
default coat_1 = "a000"

#Variables for level 2 - EC
default accessory_2 = "a000"
default headwear_2 = "a000"
default topDress_2 = "a000"
default socksTights_2 = "a000"
default shoes_2 = "a000"
default coat_2 = "a000"

#Variables for level 3 - EC
default accessory_3 = "a000"
default headwear_3 = "a000"
default topDress_3 = "a000"
default socksTights_3 = "a000"
default shoes_3 = "a000"
default coat_3 = "a000"

#Variables for level 4 - EC
default accessory_4 = "a000"
default headwear_4 = "a000"
default topDress_4 = "a000"
default socksTights_4 = "a000"
default shoes_4 = "a000"
default coat_4 = "a000"

#variables for level 5 - EC
default accessory_5 = "a000"
default headwear_5 = "a000"
default topDress_5 = "a000"
default socksTights_5 = "a000"
default shoes_5 = "a000"
default coat_5 = "a000"

#these are images that will be displayed later in the game - EC
image happy goose = im.Scale("goose_happy.PNG", 431, 1000)
image normal goose = im.Scale("defaultgoose.PNG", 432, 1000)
image pendarsee = im.Scale("pendarsee.PNG", 500, 1000)
image pendarblink = im.Scale("pendarblink.PNG", 500, 1000)

#the following code runs the actual game - EC
label start:
#each label is a different scene in the progress of the game - EC
#this label is shown after start is clicked from the start menu - EC 
    
    play music audio.wario
    #PLAY MUSIC LETS GOOOOOO - IC

    scene temp backgroundd
    #calling "scene" sets the background to the image that follows after - EC

    #this dialogue is for the tutorial level/level 0 and sets up the context of the game for the player - E.L
    t "Welcome to Glamour Goose! You are a student at the University of Watergoose\
    and every day is another chance to show off your fashion skills."
    
    t "By choosing an outfit that fits each scenario’s theme, you can win special items and move\
    onto the next level! Maybe you’ll even unlock a hidden level ;)"

    #this dialgoue is instructions on how to actually select clothing items to create their outfits - E.L
    t "Click on the clothing item to put it on. If you want to take it off, click on\
    the red X."

    #this dialogue informs the player about the category system and reminds them to keep each level's theme in mind for their outfit - E.L
    t "Each clothing item has different tags that correspond to the different\
    categories of clothes: {i}Cute, Elegant, Goth, Formal, Casual, and Active{/i}." 
    
    t "For each level, pay attention to keywords in the dialogue that hint towards which\
    categories you should wear."

    scene rch hall with Dissolve(1)
    #takes 1 second to display new background - EC
    
    #this is the dialogue for the first level of the game dictated by the narrator instead of the tutorial - E.L
    n "It’s your first day at Watergoose! The first thing on your schedule is a CHE\
    120 lecture with Professor Pendar. Why don’t you put something {b}casual{/b} on?"
    
    call screen startdress0
    #calling this screen starts the dress up client

    label doneLVL0:

        hide screen startdress0
        hide screen dress_ui0

        hide screen goosebase

        hide screen headwearNull
        hide screen headwear1
        hide screen headwear2
        hide screen headwear3
        hide screen headwear4

        hide screen coatNull
        hide screen coat1
        hide screen coat2
        hide screen coat3
        hide screen coat4

        hide screen topDressNull
        hide screen topDress1
        hide screen topDress2
        hide screen topDress3
        hide screen topDress4

        hide screen socksTightsNull
        hide screen socksTights1
        hide screen socksTights2
        hide screen socksTights3
        hide screen socksTights4

        hide screen shoesNull
        hide screen shoes1
        hide screen shoes2
        hide screen shoes3
        hide screen shoes4

        hide screen accessoryNull
        hide screen accessory1
        hide screen accessory2
        hide screen accessory3
        hide screen accessory4
        #all dressup screens are hidden - EC

        scene rch hall with Dissolve(0.5)
        #takes 0.5 seconds to show new background - EC
        show goose_0 at center
        #shows the outfit created in lvl0, code for this is in the file fulloutfit0 - EC

        $ statement0 = calculate_points(accessory_0, headwear_0, coat_0, topDress_0, socksTights_0, shoes_0)
        #the dollar sign initilaizes python for this one line of code, it calls the function from the points code file - EC
        #it takes in the variables whose values were determined by the imagebuttons in the dressup_client_lvl0 file - EC
        #this calculates the rank of the outfit - EC
        n "Casual Rank: [statement0[2]]"
        #Prints the 3rd entry of statement0, which corresponds to Casual Rank as stated in the points_code file - EC

        if statement0[2] == "B" or statement0[2]== "A" or statement0[2]=="S":
            #The casual rank needs to be a B or higher to pass this level - EC

            #these dialgoue statements tell the player if they've passed or failed the level - E.L
            n "Congrats! Pendar loved your outfit :) You’ve won a green dot accessory."

            jump startlvl1
            #the jump command takes the player to another label, in this case startlvl1 - EC

        else:

            n "Oh no! Your outfit isn’t suitable for a lecture. Hint: Try something more casual."

            $ accessory_0 = "a000"
            $ headwear_0 = "a000"
            $ topDress_0 = "a000"
            $ socksTights_0 = "a000"
            $ shoes_0 = "a000"
            $ coat_0 = "a000"
            #initilizes python to reset the variable values to the string that coressponds to 0 points in all categories - EC
            hide goose_0
            #hides the layered image - EC

            call screen startdress0
            #restarts the level - EC

    label startlvl1:

        scene wloo outsiderch with Dissolve(2)
        #shows background in 2 seconds - EC
        hide goose_0
        #hides image from previous label - EC

        #this is the dialogue for the second level of the game - E.L
        n "It’s almost the end of O Week at Watergoose. The last Frosh event is to earn \
        your hard hat by working with your friends to complete a series of challenges. \
        Let’s put something on that’s {b}cute{/b} and {b}active{/b}!"

        call screen startdress1
        #starts level 1 - EC

    label doneLVL1:

        hide screen startdress1
        hide screen dress_ui1

        hide screen goosebase

        hide screen headwearNull
        hide screen headwear1
        hide screen headwear2
        hide screen headwear3
        hide screen headwear4

        hide screen coatNull
        hide screen coat1
        hide screen coat2
        hide screen coat3
        hide screen coat4

        hide screen topDressNull
        hide screen topDress1
        hide screen topDress2
        hide screen topDress3
        hide screen topDress4

        hide screen socksTightsNull
        hide screen socksTights1
        hide screen socksTights2
        hide screen socksTights3
        hide screen socksTights4

        hide screen shoesNull
        hide screen shoes1
        hide screen shoes2
        hide screen shoes3
        hide screen shoes4

        hide screen accessoryNull
        hide screen accessory1
        hide screen accessory2
        hide screen accessory3
        hide screen accessory4
        hide screen accessorys1

        #all dressup screens are hidden - EC

        scene wloo outsiderch with Dissolve(0.5)
        #show new background in 0.5 sec
        show goose_1 at center
        #shows layered image for lvl 1

        $ statement1 = calculate_points(accessory_1, headwear_1, coat_1, topDress_1, socksTights_1, shoes_1)
        #the dollar sign initilaizes python for this one line of code, it calls the function from the points code file - EC
        #it takes in the variables whose values were determined by the imagebuttons in the dressup_client_lvl1 file - EC
        #this calculates the rank of the outfit - EC
        n "Cute Rank: [statement1[0]], Active Rank: [statement1[5]]"
        #Prints the 1st and last entry of statement1, which corresponds to Cute and Active Rank as stated in the points_code file - EC
        if statement1[0]=="C" or statement1[0]=="D" or statement1[0]=="F":
            jump faillvl1
            #goes to fail lvl1 - EC

        elif statement1[5]=="C" or statement1[5]=="D" or statement1[5]=="F":
            jump faillvl1
            #goes to fail lvl1 - EC
       
        else:
            #at least a B in both Cute and Active is needed to pass this level - EC
            
            #these dialgoue statements tell the player if they've passed or failed the level and what item they've won by passing - E.L
            n "You’ve completed all the challenges and been awarded a hard hat! Good \
            luck on your journey to becoming an engigoose!"
            
            jump startlvl2
            #goes to the next level - EC

    label faillvl1:
            n "Unfortunately, you weren’t able to complete all the challenges because \
            you were hindered by your outfit. Hint: Try something more active and/or cute."

            $ accessory_1 = "a000"
            $ headwear_1 = "a000"
            $ topDress_1 = "a000"
            $ socksTights_1 = "a000"
            $ shoes_1 = "a000"
            $ coat_1 = "a000"
            #resets item variables - EC
            hide goose_1
            #hides image so it doesn't overlap in the gameUI - EC

            call screen startdress1
            #restarts lvl1 - EC

    label startlvl2:    
        
        scene wloo outside with Dissolve(2)
        #2 secs to show new background - EC

        hide goose_1
        #hides layered image from previous level - EC

        #this is the dialogue for the third level of the game - E.L
        n "It’s time to relax after your midterms. Isn’t there a Noon Hour concert that\
        features different musical theatre songs later today? Call your friends to join you and get\
        dressed up in something {b}elegant{/b}!"
        #the {b}...{/b} format bolds the words inbetween the b's - EC

        call screen startdress2
        #starts level 2 dress up client - EC

    label doneLVL2:

        hide screen startdress2
        hide screen dress_ui2

        hide screen goosebase

        hide screen headwearNull
        hide screen headwear1
        hide screen headwear2
        hide screen headwear3
        hide screen headwear4
        hide screen headwears1

        hide screen coatNull
        hide screen coat1
        hide screen coat2
        hide screen coat3
        hide screen coat4

        hide screen topDressNull
        hide screen topDress1
        hide screen topDress2
        hide screen topDress3
        hide screen topDress4

        hide screen socksTightsNull
        hide screen socksTights1
        hide screen socksTights2
        hide screen socksTights3
        hide screen socksTights4

        hide screen shoesNull
        hide screen shoes1
        hide screen shoes2
        hide screen shoes3
        hide screen shoes4

        hide screen accessoryNull
        hide screen accessory1
        hide screen accessory2
        hide screen accessory3
        hide screen accessory4
        hide screen accessorys1

        #all dressup screens are hidden - EC

        scene opera with Dissolve(0.5)
        #shows background after 0.5 seconds - EC
        show goose_2 at center
        #shows layered image created by the _2 item variables - EC

        $ statement2 = calculate_points(accessory_2, headwear_2, coat_2, topDress_2, socksTights_2, shoes_2)
        #the dollar sign initilaizes python for this one line of code, it calls the function from the points code file - EC
        #it takes in the variables whose values were determined by the imagebuttons in the dressup_client_lvl2 file - EC
        #this calculates the rank of the outfit - EC
        n "Elegant Rank: [statement2[4]]"
        #Prints the 5th entry of statement2, which corresponds to Elegant Rank as stated in the points_code file - EC
        if statement2[4]=="B" or statement2[4]=="A" or statement2[4]=="S":
            #needs at least a B in Elegant to pass - EC
            
            #these dialgoue statements tell the player if they've passed or failed the level and what item they've won by passing- E.L
            n "You’re looking very classy for the concert! You’ve won an opera monocole."

            jump startlvl3
            #goes to next level - EC

        else:

            n "Oh no, your outfit doesn’t fit the concert dress code :( Hint: Try something more elegant."

            $ accessory_2 = "a000"
            $ headwear_2 = "a000"
            $ topDress_2 = "a000"
            $ socksTights_2 = "a000"
            $ shoes_2 = "a000"
            $ coat_2 = "a000"
            #resets variables corresponding to this level - EC
            hide goose_2
            #hides layered image so it doesn't appear in dressupUI - EC

            call screen startdress2
            #restarts level 2 - EC

    label startlvl3:

        scene wloo e6 with Dissolve(2)
        #2 secs to show background - EC
        hide goose_2
        #hides layered image from previous level - EC

        #this is the dialogue for the fourth level of the game - E.L
        n "It’s co-op application season… But the good thing is, you’ve secured an interview \
        with Professor Pendar to discuss the possibilities of being one of her research assistants. \
        To make a good impression, wear something {b}formal{/b} to the interview."

        call screen startdress3
        #starts level3 - EC

    label doneLVL3:
        
        hide screen startdress3
        hide screen dress_ui3

        hide screen goosebase

        hide screen headwearNull
        hide screen headwear1
        hide screen headwear2
        hide screen headwear3
        hide screen headwear4
        hide screen headwears1
        hide screen headwears2

        hide screen coatNull
        hide screen coat1
        hide screen coat2
        hide screen coat3
        hide screen coat4

        hide screen topDressNull
        hide screen topDress1
        hide screen topDress2
        hide screen topDress3
        hide screen topDress4

        hide screen socksTightsNull
        hide screen socksTights1
        hide screen socksTights2
        hide screen socksTights3
        hide screen socksTights4

        hide screen shoesNull
        hide screen shoes1
        hide screen shoes2
        hide screen shoes3
        hide screen shoes4

        hide screen accessoryNull
        hide screen accessory1
        hide screen accessory2
        hide screen accessory3
        hide screen accessory4
        hide screen accessorys1

        #all dressup screens are hidden - EC

        scene wloo e6 with Dissolve(0.5)
        #shows background after 0.5 secs - EC
        show goose_3 at center
        #layered image created in dressupUI3 - EC

        $ statement3 = calculate_points(accessory_3, headwear_3, coat_3, topDress_3, socksTights_3, shoes_3)
        #the dollar sign initilaizes python for this one line of code, it calls the function from the points code file - EC
        #it takes in the variables whose values were determined by the imagebuttons in the dressup_client_lvl3 file - EC
        #this calculates the rank of the outfit - EC
        n "Formal Rank: [statement3[3]]"
        #Prints the 4th entry of statement3, which corresponds to Formal Rank as stated in the points_code file - EC
        if statement3[3]=="A" or statement3[3]=="S":
            #needs at least an A in Formal to pass - EC

            #these dialgoue statements tell the player if they've passed or failed the level and the item they've won by passing - E.L
            n "Good work! Professor Pendar seemed impressed with your appearance and interview skills.\
            Hopefully you get the job! You’ve won a rubber duck to help you with coding."

            #recalculates points to check if goth level is unlocked - EC
            $ statement0 = calculate_points(accessory_0, headwear_0, coat_0, topDress_0, socksTights_0, shoes_0)
            $ statement1 = calculate_points(accessory_1, headwear_1, coat_1, topDress_1, socksTights_1, shoes_1)
            $ statement2 = calculate_points(accessory_2, headwear_2, coat_2, topDress_2, socksTights_2, shoes_2)
            $ statement3 = calculate_points(accessory_3, headwear_3, coat_3, topDress_3, socksTights_3, shoes_3)

            if statement0[1] == "D" or statement0[1] == "F":
                jump freedress
                #if the player did not unlock the secret level, the move on to the final level - EC
            elif statement1[1] == "D" or statement1[1] == "F":
                jump freedress 
                #if the player did not unlock the secret level, the move on to the final level - EC
            elif statement2[1] == "D" or statement2[1] == "F":
                jump freedress
                #if the player did not unlock the secret level, the move on to the final level - EC
            elif statement3[1] == "D" or statement3[1] == "F":
                jump freedress
                #if the player did not unlock the secret level, the move on to the final level - EC
            else:
                #if the player has acheived at least a C rank in Goth for all previous levels they unlock a secret level - EC
                scene wloo outside with Dissolve(2)
                #shows background in 2 secs - EC
                hide goose_3
                #hides layered image from previous level - EC
                show happy goose at center
                #shows new image - EC

                #this dialogue tells the player they've unlocked the secret goth date level and have an additional level to complete - E.L
                n "Yippee! You’ve unlocked the secret goth level :) You’re going on a goth date with \
                your goose crush in an hour. Quick, put on your best {b}goth{/b} outfit to leave a mysterious \
                and lingering impression!"

                call screen startdress4
                #starts secret 4th level - EC

        else:
            n "Professor Pendar didn’t seem too impressed with what you wore… Hint: Try something more formal."

            $ accessory_3 = "a000"
            $ headwear_3 = "a000"
            $ topDress_3 = "a000"
            $ socksTights_3 = "a000"
            $ shoes_3 = "a000"
            $ coat_3 = "a000"
            #resets the variables that determine the rank of the level3 outfit - EC
            hide goose_3
            #hides layered image - EC

            call screen startdress3
            #restarts level3 - EC
    
    label doneLVL4:

        hide screen startdress4
        hide screen dress_ui4

        hide screen goosebase

        hide screen headwearNull
        hide screen headwear1
        hide screen headwear2
        hide screen headwear3
        hide screen headwear4
        hide screen headwears1
        hide screen headwears2
        hide screen headwears3

        hide screen coatNull
        hide screen coat1
        hide screen coat2
        hide screen coat3
        hide screen coat4

        hide screen topDressNull
        hide screen topDress1
        hide screen topDress2
        hide screen topDress3
        hide screen topDress4

        hide screen socksTightsNull
        hide screen socksTights1
        hide screen socksTights2
        hide screen socksTights3
        hide screen socksTights4

        hide screen shoesNull
        hide screen shoes1
        hide screen shoes2
        hide screen shoes3
        hide screen shoes4

        hide screen accessoryNull
        hide screen accessory1
        hide screen accessory2
        hide screen accessory3
        hide screen accessory4
        hide screen accessorys1

        #all dressup screens are hidden - EC

        scene goth cafe with Dissolve(0.5)
        #shows background in 0.5 seconds - EC
        show goose_4 at center
        #shows layered image created in level4 -EC

        $ statement4 = calculate_points(accessory_4, headwear_4, coat_4, topDress_4, socksTights_4, shoes_4)
        #the dollar sign initilaizes python for this one line of code, it calls the function from the points code file - EC
        #it takes in the variables whose values were determined by the imagebuttons in the dressup_client_lvl4 file - EC
        #this calculates the rank of the outfit - EC
        n "Goth Rank: [statement4[1]]"
        #Prints the 2nd entry of statement4, which corresponds to Goth Rank as stated in the points_code file - EC
        if statement4[1] == "A" or statement4[1] == "S":
            #needs at least an A in goth to pass - EC

            #these dialgoue statements tell the player if they've passed or failed the secret final level - E.L
            n "You had such a great time you’re going out on another date again next week! What a \
            happy goose couple!"

            jump freedress
            #goes to final level - EC

        else: 

            n "Because you didn’t fit the dress code of the date venue, you and your goose crush \
            had to awkwardly leave and go somewhere else :( Hint: Try something more goth."

            call screen startdress4
            #restarts level 4 - EC

    label freedress:

        hide goose_3
        hide goose_4
        #hides layered images from level 3 and 4 to account for the fact some players may not unlock level 4 - EC
        scene wloo outsiderch with Dissolve(2)
        #shows background in 2 secs - EC

        show normal goose at center
        #displays image - EC

        n "Ah after all that outfit changing you must want to take a break...."
        n "Wait a second,,,, who's that in the distance?"

        show normal goose at left
        #moves image position - EC
        show pendarsee at center
        #shows new image at the same time - EC

        n "OMG it's Professor Pendar!"

        hide normal goose
        show happy goose at left
        #replaces normal goose image - EC

        p "I've been very impressed with your outfits this week, especially during your interview."

        hide pendarsee
        show pendarblink at center
        #replaces pendarsee with pendarblink - EC

        p "Before I take you on as my co-op student, I need to see your personal style! \
        Please dress however {b}you{/b} want to."

        hide happy goose
        hide pendarblink
        #hides images before dressup_client is run - EC

        call screen startdress5
        #starts lvl5

    label donefree:

        hide screen startdress5
        hide screen dress_ui5

        hide screen goosebase

        hide screen headwearNull
        hide screen headwear1
        hide screen headwear2
        hide screen headwear3
        hide screen headwear4
        hide screen headwears1
        hide screen headwears2
        hide screen headwears3
        hide screen headwears4

        hide screen coatNull
        hide screen coat1
        hide screen coat2
        hide screen coat3
        hide screen coat4

        hide screen topDressNull
        hide screen topDress1
        hide screen topDress2
        hide screen topDress3
        hide screen topDress4

        hide screen socksTightsNull
        hide screen socksTights1
        hide screen socksTights2
        hide screen socksTights3
        hide screen socksTights4

        hide screen shoesNull
        hide screen shoes1
        hide screen shoes2
        hide screen shoes3
        hide screen shoes4

        hide screen accessoryNull
        hide screen accessory1
        hide screen accessory2
        hide screen accessory3
        hide screen accessory4
        hide screen accessorys1

        #hides all item screens - EC

        scene wloo outsiderch with Dissolve(0.5)
        #shows background in 0.5 seconds - EC

        show goose_5 at center
        #shows outfit created as a layered image - EC

        $ statement5 = calculate_points(accessory_5, headwear_5, coat_5, topDress_5, socksTights_5, shoes_5)
        #the dollar sign initilaizes python for this one line of code, it calls the function from the points code file - EC
        #it takes in the variables whose values were determined by the imagebuttons in the dressup_client_lvl5 file - EC
        #this calculates the rank of the outfit - EC
        n "Cute Rank: [statement5[0]], Goth Rank: [statement5[1]], Casual Rank: [statement5[2]], \
        Formal Rank: [statement5[3]], Elegant Rank: [statement5[4]], Active Rank: [statement5[5]]"
        #Prints all entries of statement 5 to let the player know what their outfit could've scored - EC
        #no pass condition, it's free dressup - EC
        show goose_5 at left
        #moves layered image - EC
        show pendarsee at center
        #shows other image at the same time - EC

        p "Wow! You are a very stylish goose! I can really see your personality through this outfit."

        hide pendarsee
        show pendarblink at center
        #replaces pendarsee with pendarblink -EC

        p "You have definitly earned a co-op position with me. I'm excited to see what you bring to \
        this university!"

        hide pendarblink
        #gets rid of pendar blink - EC
        show goose_5 at center
        #moves layered image - EC

        n "You did it! And it was all thanks to your super styling :)"

        jump donegame
        #goes to ending label - EC

    label donegame:

        scene wloo outside with Dissolve(2)
        #shows background in 2 secs - EC

        hide goose_5
        #hides image from previous level - EC

        show happy goose at center
        #shows image - EC

        #this dialogue tells the player the game is over - E.L
        n "What an eventful week it’s been! So much to do and learn now that you’re at the University \
        of Watergoose. I wonder what outfit you’ll wear tomorrow?"
    
        #this dialogue is just a thank you to the player from us for playing the game :) - E.L
        d "Thank you so much for playing Goose Glamour! We hope you had lots of fun dressing up your \
        goose persona :)"

        hide happy goose
        #gets rid of happy goose - EC

        scene end
        #replaces background
        show goose_0 at Position(xpos=0.1)
        show goose_1 at Position(xpos=0.2)
        show goose_2 at Position(xpos=0.4)
        show goose_3 at Position(xpos=0.6)
        show goose_4 at Position(xpos=0.8)
        show goose_5 at Position(xpos=0.9)
        #shows all created images on one screen, since more than 3 images are to be displayed, center, right, and left are not sufficient - EC
        #Position argument is used to specify location on the horizontal axis - EC
        #it goes in terms of percentage of the screen, so 0.5 is in the middle, 0.0 is all the way on the left, 1.0 is all the way on the right - EC

        d "Stay glam!"

        #Stops the music - IC
        stop music fadeout 1.0

        return

    # This ends the game.

