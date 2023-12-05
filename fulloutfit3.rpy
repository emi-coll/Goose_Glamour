
#this code is responsible for displaying an outfit outside of the dressup minigame -E.C.
layeredimage goose_3:
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
    #blank image - EC
    if socksTights_5 == "a000" :
        "null.PNG"
    #yellow/black striped socks - EC    
    elif socksTights_5 == "a442":
        "socks1.PNG"
    #buisness socks - EC
    elif socksTights_5 == "a444":
        "socks2.PNG"
    #fishnets - EC
    elif socksTights_5 == "a443":
        "socks3.PNG"
    #elegant socks - EC
    elif socksTights_5 == "a445":
        "socks4.PNG"
        
    group topDress:
        attribute 0 default:
            "null.PNG"
    #blank item - EC
    if topDress_5 == "a000":
        "null.PNG" 
    #yellow wloo shirt - EC
    elif topDress_5 == "a331":
        "top1.PNG"
    #buisness shirt - EC
    elif topDress_5 == "a333":
        "top2.PNG"
    #goth corset - EC
    elif topDress_5 == "a332":
        "top3.PNG" 
    #elegant dress - EC
    elif topDress_5 == "a334":
        "top4.PNG"

    group coat:
        attribute 0 default:
            "null.PNG"
    #blank item - EC
    if coat_5 == "a000":
        "null.PNG"
    #varsity jacket - EC
    elif coat_5 == "a221":
        "coat1.PNG"
    #blazer - EC
    elif coat_5 == "a223":
        "coat2.PNG"
    #bolero - EC
    elif coat_5 == "a222":
        "coat3.PNG"
    #boa - EC
    elif coat_5 == "a224":
        "coat4.PNG"

    group headwear:
        attribute 0 default:
            "null.PNG"
    #blank item - EC
    if headwear_5 == "a000":
        "null.PNG"
    #goose plush - EC
    elif headwear_5 == "a112":
        "headwear1.PNG"
    #buisness glasses - EC
    elif headwear_5 == "a114":
        "headwear2.PNG"
    #batwing headband - EC
    elif headwear_5 == "a113":
        "headwear3.PNG"
    #earrings - EC
    elif headwear_5 == "a116":
        "headwear4.PNG"
    #hardhat - EC
    elif headwear_5 == "a":
        "headwears1.PNG"
    #opera monocole - EC
    elif headwear_5 == "a1":
        "headwears2.PNG"

    group accessory:
        attribute 0 default:
            "null.PNG"
    #blank item - EC
    if accessory_5 == "a000":
        "null.PNG"
    #lanyard - EC
    elif accessory_5 == "a902":
        "accessory1.PNG"
    #buisness watch - EC
    elif accessory_5 == "a904":
        "accessory2.PNG"
    #choker - EC
    elif accessory_5 == "a903":
        "accessory3.PNG"
    #elegant purse - EC
    elif accessory_5 == "a905":
        "accessory4.PNG"
    #green dot - EC
    elif accessory_5 == "a910":
        "accessorys1.PNG"
    
    group shoes:
        attribute 0 default:
            "null.PNG"
    #blank item - EC
    if shoes_5 == "a000":
        "null.PNG"
    #slides - EC
    elif shoes_5 == "a549":
        "shoes1.PNG"
    #buisness shoes - EC
    elif shoes_5 == "a551":
        "shoes2.PNG"
    #platform boots - EC
    elif shoes_5 == "a550":
        "shoes3.PNG"
    #elegant shoes - EC
    elif shoes_5 == "a552":
        "shoes4.PNG" 
        