#This allows the software to change the size of the buttons without changing the image files themselves -E.C.
init:
    transform startbuttonzoom:
        zoom 3.0
    transform donebuttonzoom:
        zoom 1.2
    transform headwearzoom1:
        zoom 0.2
    transform headwearzoom2:
        zoom 0.2
    transform coatzoom1:
        zoom 0.1
    transform accessoryzoom1:
        zoom 0.125

#This screen displays a button that when clicked initializes the dress up UI - E.C.
screen startdress3:
    image "temp backgroundd.PNG"
    imagebutton auto "TestStart_%s.PNG" align(0.5, 0.40) action [Show("dress_ui3"), Show("goosebase")] at startbuttonzoom

#This is the dressup UI for level 1 - E.C.
screen dress_ui3:
    image "temp backgroundd.PNG"
    image "TestGUI.png" 
    
#This button takes the user out of the dressup UI when they are done creating their outfit - E.C.
    imagebutton auto "TestDone_%s.PNG" align(0.09, 1.0) action [Jump("doneLVL3")] at donebuttonzoom

#Every wearable item does 2 actions, the first is to show the screen associated with that particular wearable - EC
#And the second is to set the clothing variable to the string asccoitated with this item in the points code - EC
#For example, headwear1, which is a plush goose, shows a plush goose on the main body and sets the variable headwear_3 to "a112" - EC
#and "a112" is the string accosiated with the variable of the same name, and that variable is assigned to a list with the point value of that item - EC

#notice the file name used for the buttons, they all end in _%s.PNG - EC
#this nameing coupled with the declaration of "auto" allows the image to exist in two states - EC
#idle state, when it is not being interacted with, and hover, when the cursor is over the button - EC
#If you look into the image files, you'll notice that every button has two images, an _hover and _idle - EC
#using this naming convention, renpy automatically assigns those images to their corressponding state - EC

#Headwear buttons  - EC
    #X button
    imagebutton auto "nullGUI_%s.PNG" align (0.95, 0.05) action [Show("headwearNull"), SetVariable("headwear_3", "a000")] at nullzoom
    
    #goose plush - EC
    imagebutton auto "headwear1GUI_%s.PNG" align(0.325, 4) action [Show("headwear1"), SetVariable("headwear_3", "a112")] at headwearzoom1
    #buisness glasses - EC
    imagebutton auto "headwear2GUI_%s.PNG" align(0.4, 0) action [Show("headwear2"), SetVariable("headwear_3", "a114")] at headwearzoom2
    #batwing headband - EC
    imagebutton auto "headwear3GUI_%s.PNG" align(0.475, 0) action [Show("headwear3"), SetVariable("headwear_3", "a113")] at headwearzoom1
    #earrings - EC
    imagebutton auto "headwear4GUI_%s.PNG" align(0.550, 0) action [Show("headwear4"), SetVariable("headwear_3", "a116")] at accessoryzoom1
    
    #hardhat - EC
    imagebutton auto "headwears1GUI_%s.PNG" align (0.88, 0.05) action [Show("headwears1"), SetVariable("headwear_3", "a")] at coatzoom1
    #opera monocle - EC
    imagebutton auto "headwears2GUI_%s.PNG" align (0.825, 0) action [Show("headwears2"), SetVariable("headwear_3", "a1")] at coatzoom1

#Coat buttons - EC  
    #X button - EC
    imagebutton auto "nullGUI_%s.PNG" align (0.95, 0.25) action [Show("coatNull"), SetVariable("coat_3", "a000")] at nullzoom

    #varsity jacket - EC
    imagebutton auto "coat1GUI_%s.PNG" align(0.35, 0.25) action [Show("coat1"), SetVariable("coat_3", "a221")] at coatzoom1
    #blazer - EC
    imagebutton auto "coat2GUI_%s.PNG" align(0.42, 0.25) action [Show("coat2"), SetVariable("coat_3", "a223")] at coatzoom1
    #bolero - EC
    imagebutton auto "coat3GUI_%s.PNG" align(0.49, 0.25) action [Show("coat3"), SetVariable("coat_3", "a222")] at coatzoom1
    #boa - EC
    imagebutton auto "coat4GUI_%s.PNG" align(0.56, 0.25) action [Show("coat4"), SetVariable("coat_3", "a224")] at coatzoom1

#Top/Dress buttons - EC
    #X button - EC
    imagebutton auto "nullGUI_%s.PNG" align (0.95, 0.425) action [Show("topDressNull"), SetVariable("topDress_3", "a000")] at nullzoom

    #yellow wloo shirt - EC
    imagebutton auto "top1GUI_%s.PNG" align(0.34, 0.45) action [Show("topDress1"), SetVariable("topDress_3", "a331")] at coatzoom1
    #buisness shirt - EC
    imagebutton auto "top2GUI_%s.PNG" align(0.41, 0.45) action [Show("topDress2"), SetVariable("topDress_3", "a333")] at coatzoom1
    #goth corset - EC
    imagebutton auto "top3GUI_%s.PNG" align(0.48, 0.45) action [Show("topDress3"), SetVariable("topDress_3", "a332")] at coatzoom1
    #elegant dress - EC
    imagebutton auto "top4GUI_%s.PNG" align(0.55, 0.425) action [Show("topDress4"), SetVariable("topDress_3", "a334")] at coatzoom1

#Socks/Tights buttons - EC
    #X button - EC
    imagebutton auto "nullGUI_%s.PNG" align (0.95, 0.6) action [Show("socksTightsNull"), SetVariable("socksTights_3", "a000")] at nullzoom
    #yellow/black striped socks - EC
    imagebutton auto "socks1GUI_%s.PNG" align(0.325, 0.6) action [Show ("socksTights1"), SetVariable("socksTights_3", "a442")] at coatzoom1
    #buisness socks - EC
    imagebutton auto "socks2GUI_%s.PNG" align(0.4, 0.6) action [Show ("socksTights2"), SetVariable("socksTights_3", "a444")] at coatzoom1
    #fishnets - EC
    imagebutton auto "socks3GUI_%s.PNG" align(0.475, 0.6) action [Show ("socksTights3"), SetVariable("socksTights_3", "a443")] at coatzoom1
    #elegant socks - EC
    imagebutton auto "socks4GUI_%s.PNG" align(0.550, 0.6) action [Show ("socksTights4"), SetVariable("socksTights_3", "a445")] at coatzoom1

#Shoes buttons - EC
    #X button - EC
    imagebutton auto "nullGUI_%s.PNG" align (0.95, 0.8) action [Show("shoesNull"), SetVariable("shoes_3", "a000")] at nullzoom

    #slides - EC
    imagebutton auto "shoes1GUI_%s.PNG" align(0.325, 0.8) action [Show("shoes1"), SetVariable("shoes_3", "a549")] at coatzoom1
    #buisness shoes - EC
    imagebutton auto "shoes2GUI_%s.PNG" align(0.4, 0.8) action [Show("shoes2"), SetVariable("shoes_3", "a551")] at coatzoom1
    #platform boots - EC
    imagebutton auto "shoes3GUI_%s.PNG" align(0.475, 0.8) action [Show("shoes3"), SetVariable("shoes_3", "a550")] at coatzoom1
    #elegant shoes - EC
    imagebutton auto "shoes4GUI_%s.PNG" align(0.550, 0.8) action [Show("shoes4"), SetVariable("shoes_3", "a552")] at coatzoom1

#Accessory buttons - EC
    #X button - EC
    imagebutton auto "nullGUI_%s.PNG" align (0.95, 0.96) action [Show("accessoryNull"), SetVariable("accessory_3", "a000")] at nullzoom

    #lanyard - EC
    imagebutton auto "accessory1GUI_%s.PNG" align (0.325, 0.96) action [Show("accessory1"), SetVariable("accessory_3", "a902")] at accessoryzoom1
    #buisness watch - EC
    imagebutton auto "accessory2GUI_%s.PNG" align (0.4, 0.96) action [Show("accessory2"), SetVariable("accessory_3", "a904")] at accessoryzoom1
    #choker - EC
    imagebutton auto "accessory3GUI_%s.PNG" align (0.475, 0.96) action [Show("accessory3"), SetVariable("accessory_3", "a903")] at accessoryzoom1
    #elegant purse - EC
    imagebutton auto "accessory4GUI_%s.PNG" align (0.550, 1.0) action [Show("accessory4"), SetVariable("accessory_3", "a905")] at accessoryzoom1

    #green dot - EC
    imagebutton auto "accessorys1GUI_%s.PNG" align(0.85, 0.96) action [Show("accessorys1"), SetVariable("accessory_3", "a910")] at accessoryzoom1