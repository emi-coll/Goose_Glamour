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
    transform nullzoom:
        zoom 0.05

#This screen displays a button that when clicked initializes the dress up UI - E.C.
screen startdress0:
    image "temp backgroundd.PNG"
    imagebutton auto "TestStart_%s.PNG" align(0.5, 0.40) action [Show("dress_ui0"), Show("goosebase")] at startbuttonzoom

#This is the dressup UI for level 1 - E.C.
screen dress_ui0:
    image "temp backgroundd.PNG"
    image "TestGUI.png" 
    
#This button takes the user out of the dressup UI when they are done creating their outfit - E.C.
    imagebutton auto "TestDone_%s.PNG" align(0.09, 1.0) action [Jump("doneLVL0")] at donebuttonzoom

#Headwear buttons
    imagebutton auto "nullGUI_%s.PNG" align (0.95, 0.05) action [Show("headwearNull"), SetVariable("headwear_0", "a000")] at nullzoom
    
    imagebutton auto "headwear1GUI_%s.PNG" align(0.325, 4) action [Show("headwear1"), SetVariable("headwear_0", "a112")] at headwearzoom1
    imagebutton auto "headwear2GUI_%s.PNG" align(0.4, 0) action [Show("headwear2"), SetVariable("headwear_0", "a114")] at headwearzoom2
    imagebutton auto "headwear3GUI_%s.PNG" align(0.475, 0) action [Show("headwear3"), SetVariable("headwear_0", "a113")] at headwearzoom1

#Coat buttons
    imagebutton auto "nullGUI_%s.PNG" align (0.95, 0.25) action [Show("coatNull"), SetVariable("coat_0", "a000")] at nullzoom

    imagebutton auto "coat1GUI_%s.PNG" align(0.35, 0.25) action [Show("coat1"), SetVariable("coat_0", "a221")] at coatzoom1
    imagebutton auto "coat2GUI_%s.PNG" align(0.42, 0.25) action [Show("coat2"), SetVariable("coat_0", "a223")] at coatzoom1
    imagebutton auto "coat3GUI_%s.PNG" align(0.49, 0.25) action [Show("coat3"), SetVariable("coat_0", "a222")] at coatzoom1

#Top/Dress buttons
    imagebutton auto "nullGUI_%s.PNG" align (0.95, 0.45) action [Show("topDressNull"), SetVariable("topDress_0", "a000")] at nullzoom

    imagebutton auto "top1GUI_%s.PNG" align(0.34, 0.45) action [Show("topDress1"), SetVariable("topDress_0", "a331")] at coatzoom1
    imagebutton auto "top2GUI_%s.PNG" align(0.41, 0.45) action [Show("topDress2"), SetVariable("topDress_0", "a333")] at coatzoom1
    imagebutton auto "top3GUI_%s.PNG" align(0.48, 0.45) action [Show("topDress3"), SetVariable("topDress_0", "a332")] at coatzoom1

#Socks/Tights buttons
    imagebutton auto "nullGUI_%s.PNG" align (0.95, 0.6) action [Show("socksTightsNull"), SetVariable("socksTights_0", "a000")] at nullzoom

    imagebutton auto "socks1GUI_%s.PNG" align(0.325, 0.6) action [Show ("socksTights1"), SetVariable("socksTights_0", "a442")] at coatzoom1
    imagebutton auto "socks2GUI_%s.PNG" align(0.4, 0.6) action [Show ("socksTights2"), SetVariable("socksTights_0", "a444")] at coatzoom1
    imagebutton auto "socks3GUI_%s.PNG" align(0.475, 0.6) action [Show ("socksTights3"), SetVariable("socksTights_0", "a443")] at coatzoom1

#Shoes buttons
    imagebutton auto "nullGUI_%s.PNG" align (0.95, 0.8) action [Show("shoesNull"), SetVariable("shoes_0", "a000")] at nullzoom

    imagebutton auto "shoes1GUI_%s.PNG" align(0.325, 0.8) action [Show("shoes1"), SetVariable("shoes_0", "a549")] at coatzoom1
    imagebutton auto "shoes2GUI_%s.PNG" align(0.4, 0.8) action [Show("shoes2"), SetVariable("shoes_0", "a551")] at coatzoom1
    imagebutton auto "shoes3GUI_%s.PNG" align(0.475, 0.8) action [Show("shoes3"), SetVariable("shoes_0", "a550")] at coatzoom1

#Accessory buttons
    imagebutton auto "nullGUI_%s.PNG" align (0.95, 0.96) action [Show("accessoryNull"), SetVariable("accessory_0", "a000")] at nullzoom

    imagebutton auto "accessory1GUI_%s.PNG" align (0.325, 0.96) action [Show("accessory1"), SetVariable("accessory_0", "a902")] at accessoryzoom1
    imagebutton auto "accessory2GUI_%s.PNG" align (0.4, 0.96) action [Show("accessory2"), SetVariable("accessory_0", "a904")] at accessoryzoom1
    imagebutton auto "accessory3GUI_%s.PNG" align (0.475, 0.96) action [Show("accessory3"), SetVariable("accessory_0", "a903")] at accessoryzoom1

    