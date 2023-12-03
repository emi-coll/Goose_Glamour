
#this code is responsible for displaying an outfit outside of the dressup minigame -E.C.
layeredimage goose_0:
#this layered image is for the outfit created in level 0
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
    if socksTights_0 == "a000" :
        "null.PNG"
    elif socksTights_0 == "a442":
        "socks1.PNG"
    elif socksTights_0 == "a444":
        "socks2.PNG"
    elif socksTights_0 == "a443":
        "socks3.PNG"
        
    group topDress:
        attribute 0 default:
            "null.PNG"
    if topDress_0 == "a000":
        "null.PNG"
    elif topDress_0 == "a331":
        "top1.PNG"
    elif topDress_0 == "a333":
        "top2.PNG"
    elif topDress_0 == "a332":
        "top3.PNG"

    group coat:
        attribute 0 default:
            "null.PNG"
    if coat_0 == "a000":
        "null.PNG"
    elif coat_0 == "a221":
        "coat1.PNG"
    elif coat_0 == "a223":
        "coat2.PNG"
    elif coat_0 == "a222":
        "coat3.PNG"

    group headwear:
        attribute 0 default:
            "null.PNG"
    if headwear_0 == "a000":
        "null.PNG"
    elif headwear_0 == "a112":
        "headwear1.PNG"
    elif headwear_0 == "a114":
        "headwear2.PNG"
    elif headwear_0 == "a113":
        "headwear3.PNG"
    
    group accessory:
        attribute 0 default:
            "null.PNG"
    if accessory_0 == "a000":
        "null.PNG"
    elif accessory_0 == "a902":
        "accessory1.PNG"
    elif accessory_0 == "a904":
        "accessory2.PNG"
    elif accessory_0 == "a903":
        "accessory3.PNG"
    
    group shoes:
        attribute 0 default:
            "null.PNG"
    if shoes_0 == "a000":
        "null.PNG"
    elif shoes_0 == "a549":
        "shoes1.PNG"
    elif shoes_0 == "a551":
        "shoes2.PNG"
    elif shoes_0 == "a550":
        "shoes3.PNG"
        
