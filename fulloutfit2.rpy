
#this code is responsible for displaying an outfit outside of the dressup minigame -E.C.
layeredimage goose_2:
#this layered image is for the outfit created in level 2
    zoom 0.25
#This image is always apart of the layered image - E.C.
    always:
        "defaultgoose.PNG"
#Grouping these images together prevents multiple of them being displayed at a time - E.C.
#the if statements are used in refrence to the wearable variables defined in the script file -E.C.
#Depending on what the value of the variable, the layered image displays a different item - E.C.
#These groups are in the order they are applied to the image instead of using a zorder statement - E.C.       
    group socksTights:
        attribute 0 default:
            "null.PNG"
    if socksTights_2 == "a000" :
        "null.PNG"
    elif socksTights_2 == "a442":
        "socks1.PNG"
    elif socksTights_2 == "a444":
        "socks2.PNG"
    elif socksTights_2 == "a443":
        "socks3.PNG"
        
    group topDress:
        attribute 0 default:
            "null.PNG"
    if topDress_2 == "a000":
        "null.PNG"
    elif topDress_2 == "a331":
        "top1.PNG"
    elif topDress_2 == "a333":
        "top2.PNG"
    elif topDress_2 == "a332":
        "top3.PNG"

    group coat:
        attribute 0 default:
            "null.PNG"
    if coat_2 == "a000":
        "null.PNG"
    elif coat_2 == "a221":
        "coat1.PNG"
    elif coat_2 == "a223":
        "coat2.PNG"
    elif coat_2 == "a222":
        "coat3.PNG"

    group headwear:
        attribute 0 default:
            "null.PNG"
    if headwear_2 == "a000":
        "null.PNG"
    elif headwear_2 == "a112":
        "headwear1.PNG"
    elif headwear_2 == "a114":
        "headwear2.PNG"
    elif headwear_2 == "a113":
        "headwear3.PNG"
    elif headwear_2 == "a":
        "headwears1.PNG"
    
    group accessory:
        attribute 0 default:
            "null.PNG"
    if accessory_2 == "a000":
        "null.PNG"
    elif accessory_2 == "a902":
        "accessory1.PNG"
    elif accessory_2 == "a904":
        "accessory2.PNG"
    elif accessory_2 == "a903":
        "accessory3.PNG"
    elif accessory_2 == "a":
        "accessorys1.PNG"
    
    group shoes:
        attribute 0 default:
            "null.PNG"
    if shoes_2 == "a000":
        "null.PNG"
    elif shoes_2 == "a549":
        "shoes1.PNG"
    elif shoes_2 == "a551":
        "shoes2.PNG"
    elif shoes_2 == "a550":
        "shoes3.PNG"
        