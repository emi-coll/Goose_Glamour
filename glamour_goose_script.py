#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Glamour Goose Dialogue/Text

Emma Ka Wai Liu
ID: 21065138
"""
define t = Character("Tutorial")
define n = Character("Narrator")
define d = Character("Game Creators")

#for intro scene before level 0
    t "Welcome to Glamour Goose! You are a student at the University of Watergoose\
    and every day is another chance to show off your fashion skills. By choosing\
    an outfit that fits each scenario’s theme, you can win special items and move\
    onto the next level! Maybe you’ll even unlock a hidden level ;)"
    
#for dialogue before level 0    
    t "Click on the clothing item to put it on. If you want to take it off, click on\
    the empty box.”
    
    t "Each clothing item has different tags that correspond to the different\
    categories of clothes: {i}Cute, Elegant, Goth, Formal, Casual, and Active{/i}. For\
    each level, pay attention to keywords in the dialogue that hint towards which\
    categories you should wear."
    
    n "It’s your first day at Watergoose! The first thing on your schedule is a CHE\
    120 lecture with Professor Pendar. Why don’t you put something {b}casual{/b} on?"
    
    #if pass:
    n "Congrats! Pendar loved your outfit :) You’ve won a green dot accessory."
        
    #if fail:
    n "Oh no! Your outfit isn’t suitable for a lecture. Hint: Try something more casual."

#for dialogue before level 1
    n "It’s almost the end of O Week at Watergoose. The last Frosh event is to earn \
    your hard hat by working with your friends to complete a series of challenges. \
    Let’s put something on that’s {b}cute{/b} and {b}active{/b}!”
    
    #if pass
    n "You’ve completed all the challenges and been awarded a hard hat! Good \
    luck on your journey to becoming an engigoose!"

    #if fail
    n "Unfortunately, you weren’t able to complete all the challenges because \
    you were hindered by your outfit. Hint: Try something more active and/or cute."
    
#dialogue before level 2
    n "It’s time to relax after your midterms. Isn’t there a Noon Hour concert that\
    features different musical theatre songs later today? Call your friends to join you and get\
    dressed up in something {b}elegant{/b}!"
    
    #if pass
    n "You’re looking very classy for the concert! You’ve won a Phantom of the Opera mask."
    
    #if fail
    n "Oh no, your outfit doesn’t fit the concert dress code :( Hint: Try something more elegant."

#dialogue before level 3
    n "It’s co-op application season… But the good thing is, you’ve secured an interview \
    with Professor Pendar to discuss the possibilities of being one of her research assistants. \
    To make a good impression, wear something {b}formal{/b} to the interview."
    
    #if pass
    n "Good work! Professor Pendar seemed impressed with your appearance and interview skills.\
    Hopefully you get the job! You’ve won a rubber duck to help you with coding."

    #if fail
    n "Professor Pendar didn’t seem too impressed with what you wore… Hint: Try something more formal."

#dialogue before secret goth date level
    n "Yippee! You’ve unlocked the secret goth level :) You’re going on a goth date with \
    your goose crush in an hour. Quick, put on your best {b}goth{/b} outfit to leave a mysterious \
    and lingering impression!"
    
    #if pass
    n "You had such a great time you’re going out on another date again next week! What a \
    happy goose couple!"

    #if fail
    n "Because you didn’t fit the dress code of the date venue, you and your goose crush \
    had to awkwardly leave and go somewhere else :( Hint: Try something more goth."
    
#for outro scene
    n "What an eventful week it’s been! So much to do and learn now that you’re at the University \
    of Watergoose. I wonder what outfit you’ll wear tomorrow?"
    
    d "Thank you so much for playing Goose Glamour! We hope you had lots of fun dressing up your \
    goose persona :)"
    
