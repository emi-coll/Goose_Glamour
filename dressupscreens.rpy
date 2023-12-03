#This file contains all the screens for the different wearables - E.C.
#the following screens are for wearables appearing on the character in the dress
#up minigame, they all have the same position so they stack on top of eachother
#and the zorder value is their layer number (bigger the number the more at the front) - E.C.
#the tag on each corresponds to what type of wearable they display. Only one screen with a specific tag can be displayed at a time - E.C

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
screen headwear1 zorder 1:
    image "headwear1.PNG":
        xpos 75
        ypos -5
        zoom 0.27
    tag head

screen accessory1 zorder 6:
    image "accessory1.PNG":
        xpos 75
        ypos -5
        zoom 0.27
    tag access
    
screen coat1 zorder 5:
    image "coat1.PNG":
        xpos 75
        ypos -5
        zoom 0.27
    tag cooats

screen topDress1 zorder 4:
    image "top1.PNG":
        xpos 75
        ypos -5
        zoom 0.27
    tag topdresses

screen socksTights1 zorder 1:
    image "socks1.PNG":
        xpos 75
        ypos -5
        zoom 0.27
    tag socktight

screen shoes1 zorder 2:
    image "shoes1.PNG":
        xpos 75
        ypos -5
        zoom 0.27
    tag shoe

#screens for the buisness goose set - EC
screen headwear2 zorder 1:
    image "headwear2.PNG":
        xpos 75
        ypos -5
        zoom 0.27
    tag head

screen accessory2 zorder 6:
    image "accessory2.PNG":
        xpos 75
        ypos -5
        zoom 0.27
    tag access

screen coat2 zorder 5:
    image "coat2.PNG":
        xpos 75
        ypos -5
        zoom 0.27
    tag cooats

screen topDress2 zorder 4:
    image "top2.PNG":
        xpos 75
        ypos -5
        zoom 0.27
    tag topdresses

screen socksTights2 zorder 1:
    image "socks2.PNG":
        xpos 75
        ypos -5
        zoom 0.27
    tag socktight

screen shoes2 zorder 2:
    image "shoes2.PNG":
        xpos 75
        ypos -5
        zoom 0.27
    tag shoe

#screens for the goth goose set - EC
screen headwear3 zorder 1:
    image "headwear3.PNG":
        xpos 75
        ypos -5
        zoom 0.27
    tag head

screen accessory3 zorder 6:
    image "accessory3.PNG":
        xpos 75
        ypos -5
        zoom 0.27
    tag access

screen coat3 zorder 5:
    image "coat3.PNG":
        xpos 75
        ypos -5
        zoom 0.27
    tag cooats

screen topDress3 zorder 4:
    image "top3.PNG":
        xpos 75
        ypos -5
        zoom 0.27
    tag topdresses

screen socksTights3 zorder 1:
    image "socks3.PNG":
        xpos 75
        ypos -5
        zoom 0.27
    tag socktight

screen shoes3 zorder 2:
    image "shoes3.PNG":
        xpos 75
        ypos -5
        zoom 0.27
    tag shoe

#screens for unlockable items - EC
screen headwears1 zorder 1:
    image "headwears1.PNG":
        xpos 75
        ypos -5
        zoom 0.27
    tag head

screen headwears2 zorder 1:
    image "headwears2.PNG":
        xpos 75
        ypos -5
        zoom 0.27
    tag head

screen headwears3 zorder 1:
    image "headwears3.PNG":
        xpos 75
        ypos -5
        zoom 0.27
    tag head

screen headwears4 zorder 1:
    image "headwears4.PNG":
        xpos 75
        ypos -5
        zoom 0.27
    tag head

screen accessorys1 zorder 6:
    image "accessorys1.PNG":
        xpos 75
        ypos -5
        zoom 0.27
    tag access



