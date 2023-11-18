#This allows the software to change the size of the buttons without changing the image files themselves -E.C.
init:
    transform donebuttonzoom:
        zoom 1.4
    transform headwearzoom1:
        zoom 0.2
    transform headwearzoom2:
        zoom 0.2
    transform coatzoom1:
        zoom 0.1
    transform accessoryzoom1:
        zoom 0.125

#This screen displays a button that when clicked initializes the dress up UI - E.C.
screen startdress:
    image "tempBackground.PNG"
    imagebutton auto "TestStart_%s.PNG" align(0.5, 0.40) action [Show("dress_ui"), Show("goosebase")]
    

#This is the dressup UI - E.C.
screen dress_ui:
    image "tempBackground.PNG"
    image "TestGUI.png" 
#This button takes the user out of the dressup UI when they are done creating their outfit - E.C.
    
    imagebutton auto "TestDone_%s.PNG" align(0.09, 1.0) action Jump("done") at donebuttonzoom
#Headwear
    imagebutton auto "headwear1GUI_%s.PNG" align(0.325, 4) action [Show("headwear1"), SetVariable("headwear", 1)] at headwearzoom1
    imagebutton auto "headwear2GUI_%s.PNG" align(0.4, 0) action [Show("headwear2"), SetVariable("headwear", 2)] at headwearzoom2

#Coat
    imagebutton auto "coat1GUI_%s.PNG" align(0.35, 0.25) action [Show("coat1"), SetVariable("coat", 1)] at coatzoom1

#Top/Dress
    imagebutton auto "top1GUI_%s.PNG" align(0.34, 0.45) action [Show("topDress1"), SetVariable("topDress", 1)] at coatzoom1

#Socks/Tights
    imagebutton auto "socks1GUI_%s.PNG" align(0.325, 0.6) action [Show ("socksTights1"), SetVariable("socksTights", 1)] at coatzoom1

#Shoes
    imagebutton auto "shoes1GUI_%s.PNG" align(0.325, 0.8) action [Show("shoes1"), SetVariable("shoes", 1)] at coatzoom1

#Accessory
    imagebutton auto "accessory1GUI_%s.PNG" align (0.325, 0.96) action [Show("accessory1"), SetVariable("accessory", 1)] at accessoryzoom1