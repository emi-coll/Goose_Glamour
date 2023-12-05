#This file contains all the screens for the different wearables - E.C.
#the following screens are for wearables appearing on the character in the dressup minigame - EC

#they all have the same position and size so they stack on top of eachother - EC
#and the zorder value is their layer number (bigger the number the more at the front) - E.C.
#x and y pos are where the character is in the dressupUI - EC

#the tag on each corresponds to what type of wearable they display. Only one screen with a specific tag can be displayed at a time - E.C
#the tag system removes the need for multiple lines of code hiding each screen when another screen needs to be displayed - EC
#tags are: head, access, cooats, topdresses, socktight, and shoe - EC

#screen for the goose - EC
screen goosebase:
    image "defaultgoose.PNG":
        xpos 75
        ypos -5
        zoom 0.27

#screens for blank items, used to deselect clothing - EC
screen headwearNull zorder 1:
    image "null.PNG":
        xpos 75
        ypos -5
        zoom 0.27
    tag head

screen accessoryNull zorder 6:
    image "null.PNG":
        xpos 75
        ypos -5
        zoom 0.27
    tag access

screen coatNull zorder 5:
    image "null.PNG":
        xpos 75
        ypos -5
        zoom 0.27
    tag cooats

screen topDressNull zorder 4:
    image "null.PNG":
        xpos 75
        ypos -5
        zoom 0.27
    tag topdresses

screen socksTightsNull zorder 1:
    image "null.PNG":
        xpos 75
        ypos -5
        zoom 0.27
    tag socktight

screen shoesNull zorder 2:
    image "null.PNG":
        xpos 75
        ypos -5
        zoom 0.27
    tag shoe

#screens for the basic wloo set - EC

#goose plush
screen headwear1 zorder 1:
    image "headwear1.PNG":
        xpos 75
        ypos -5
        zoom 0.27
    tag head

#laynard - EC
screen accessory1 zorder 6:
    image "accessory1.PNG":
        xpos 75
        ypos -5
        zoom 0.27
    tag access
    
#varsity jacket - EC
screen coat1 zorder 5:
    image "coat1.PNG":
        xpos 75
        ypos -5
        zoom 0.27
    tag cooats

#yellow wloo shirt
screen topDress1 zorder 4:
    image "top1.PNG":
        xpos 75
        ypos -5
        zoom 0.27
    tag topdresses

#yellow/black striped socks - EC
screen socksTights1 zorder 1:
    image "socks1.PNG":
        xpos 75
        ypos -5
        zoom 0.27
    tag socktight

#slides - EC
screen shoes1 zorder 2:
    image "shoes1.PNG":
        xpos 75
        ypos -5
        zoom 0.27
    tag shoe

#screens for the buisness goose set - EC

#buisness glasses - EC
screen headwear2 zorder 1:
    image "headwear2.PNG":
        xpos 75
        ypos -5
        zoom 0.27
    tag head

#buisness watch - EC
screen accessory2 zorder 6:
    image "accessory2.PNG":
        xpos 75
        ypos -5
        zoom 0.27
    tag access

#blazer - EC
screen coat2 zorder 5:
    image "coat2.PNG":
        xpos 75
        ypos -5
        zoom 0.27
    tag cooats

#buisness shirt - EC
screen topDress2 zorder 4:
    image "top2.PNG":
        xpos 75
        ypos -5
        zoom 0.27
    tag topdresses

#buisness socks - EC
screen socksTights2 zorder 1:
    image "socks2.PNG":
        xpos 75
        ypos -5
        zoom 0.27
    tag socktight

#buisness shoes - EC
screen shoes2 zorder 2:
    image "shoes2.PNG":
        xpos 75
        ypos -5
        zoom 0.27
    tag shoe

#screens for the goth goose set - EC

#batwing headband - EC
screen headwear3 zorder 1:
    image "headwear3.PNG":
        xpos 75
        ypos -5
        zoom 0.27
    tag head

#choker - EC
screen accessory3 zorder 6:
    image "accessory3.PNG":
        xpos 75
        ypos -5
        zoom 0.27
    tag access

#bolero - EC
screen coat3 zorder 5:
    image "coat3.PNG":
        xpos 75
        ypos -5
        zoom 0.27
    tag cooats

#goth corset - EC
screen topDress3 zorder 4:
    image "top3.PNG":
        xpos 75
        ypos -5
        zoom 0.27
    tag topdresses

#fish nets - EC
screen socksTights3 zorder 1:
    image "socks3.PNG":
        xpos 75
        ypos -5
        zoom 0.27
    tag socktight

#platform boots - EC
screen shoes3 zorder 2:
    image "shoes3.PNG":
        xpos 75
        ypos -5
        zoom 0.27
    tag shoe

#screens for elegant goose set - EC

#earrings - EC
screen headwear4 zorder 1:
    image "headwear4.PNG":
        xpos 75
        ypos -5
        zoom 0.27
    tag head

#elegant purse - EC
screen accessory4 zorder 6:
    image "accessory4.PNG":
        xpos 75
        ypos -5
        zoom 0.27
    tag access

#boa - EC
screen coat4 zorder 5:
    image "coat4.PNG":
        xpos 75
        ypos -5
        zoom 0.27
    tag cooats

#elegant dress - EC
screen topDress4 zorder 4:
    image "top4.PNG":
        xpos 75
        ypos -5
        zoom 0.27
    tag topdresses

#elegant socks - EC
screen socksTights4 zorder 1:
    image "socks4.PNG":
        xpos 75
        ypos -5
        zoom 0.27
    tag socktight

#elegant shoes - EC
screen shoes4 zorder 2:
    image "shoes4.PNG":
        xpos 75
        ypos -5
        zoom 0.27
    tag shoe

#screens for unlockable items - EC

#hardhat - EC
screen headwears1 zorder 1:
    image "headwears1.PNG":
        xpos 75
        ypos -5
        zoom 0.27
    tag head

#opera monocle - EC
screen headwears2 zorder 1:
    image "headwears2.PNG":
        xpos 75
        ypos -5
        zoom 0.27
    tag head

#rubber duck - EC
screen headwears3 zorder 1:
    image "headwears3.PNG":
        xpos 75
        ypos -5
        zoom 0.27
    tag head

#sanrio hat - EC
screen headwears4 zorder 1:
    image "headwears4.PNG":
        xpos 75
        ypos -5
        zoom 0.27
    tag head

#green dot - EC 
screen accessorys1 zorder 6:
    image "accessorys1.PNG":
        xpos 75
        ypos -5
        zoom 0.27
    tag access



