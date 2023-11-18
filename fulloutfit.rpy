
#this code is responsible for displaying an outfit outside of the dressup minigame -E.C.
layeredimage goose:
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
    if socksTights == 0:
        "null.PNG"
    elif socksTights == 1:
        "socks1.PNG"
        
    group topDress:
        attribute 0 default:
            "null.PNG"
    if topDress == 0:
        "null.PNG"
    elif topDress == 1:
        "top1.PNG"

    group coat:
        attribute 0 default:
            "null.PNG"
    if coat == 0:
        "null.PNG"
    elif  coat == 1:
        "coat1.PNG"

    group headwear:
        attribute 0 default:
            "null.PNG"
    if headwear == 0:
        "null.PNG"
    elif headwear == 1:
        "headwear1.PNG"
    
    group accessory:
        attribute 0 default:
            "null.PNG"
    if accessory == 0:
        "null.PNG"
    elif accessory == 1:
        "accessory1.PNG"
    
    group shoes:
        attribute 0 default:
            "null.PNG"
    if shoes == 0:
        "null.PNG"
    elif shoes == 1:
        "shoes1.PNG"
        
