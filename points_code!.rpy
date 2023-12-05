init python:
#this allows python to work in renpy - JA
   
    """
    Jason Anandappa
    21070211

    """


    # JA: PV = Point Value
    # JA: This is how each of the item's point values are assigned
    # JA: "Category Names" = [Cute PV, Goth PV, Casual PV, Formal PV, Elegant PV, Active PV]

    #EC: NULL

    a000 = [0,0,0,0,0,0]

    #EC: level specific items

    #greendot - JA
    a910 = [3,3,3,3,3,3]
    #hardhat - JA
    a = [1,-1,2,0,0,7]
    #opera monocole - JA
    a1 = [1,2,0,5,5,0]
    #rubberduck - JA
    a2 = [6,0,3,-1,0,1]
    #sanrio hat - JA
    a3 = [5,10,0,0,0,0]

    # JA: Choice of Accessories

    #waterloo lanyard - JA
    a902 = [1,-2,2,1,0,2]
    #choker - JA
    a903 = [2,3,0,-2,-1,-2]
    #business watch - JA
    a904 = [0,0,1,3,1,0]
    #purse - JA
    a905 = [1,2,0,0,4,-2]

    # JA: Choice of Headwear

    #goose plush - JA
    a112 = [3,0,3,-1,-1,0]
    #batwing headband - JA
    a113 = [2,3,0,-2,-2,-2]
    #business glasses - JA
    a114 = [1,0,2,3,1,0]
    #cute glasses - JA
    a115 = [3,1,2,0,0,0]
    #earrings - JA
    a116 = [1,2,0,1,2,-1]

    # JA: Choice of Coats

    #waterloo varsity jacket - JA
    a221 = [3,-3,5,0,-2,5]
    #bolera - JA
    a222 = [3,5,0,-2,2,-1]
    #blazer - JA
    a223 = [1,0,-1,5,2,-1]
    #boa - JA
    a224 = [1,0,-2,2,5,-3]

    # JA: Choice of TopsDresses

    #spirit shirt - JA
    a331 = [3,-5,5,1,-1,5]
    #corset/harness - JA
    a332 = [2,5,-2,-2,2,-5]
    #dress shirt - JA
    a333 = [1,0,1,5,3,0]
    #ball gown - JA
    a334 = [1,-1,-3,0,5,-4]

    # JA: Choice of Socks/Tights

    #long yellow/black socks - JA
    a442 = [2,1,3,0,-1,4]
    #fishnets - JA
    a443 = [2,8,1,-2,0,-2]
    #professional socks - JA
    a444 = [1,0,2,3,1,0]
    #elegant socks - JA
    a445 = [1,1,-1,1,3,-1]

    # JA: Choice of Shoes

    #waterloo slides - JA
    a549 = [3,-2,4,0,-1,2]
    #platform boots - JA
    a550 = [3,4,-1,1,2,0]
    #business shoes - JA
    a551 = [1,2,2,4,3,-1]
    #elegant shoes - JA
    a552 = [1,2,-2,1,3,-2]

    # JA: The following itemlist includes all of the items in the game with their 
    # JA: point values for each category

    itemlist1 = [a000, a902, a903, a904, a905, a910, a112, a113, a114, a115, a116, a221, 
                a222, a223, a224, a331, a332, a333, a334, a442, a443, a444, a445, 
                a549, a550, a551, a552, a, a1, a2, a3]

    # JA: The following itemlist includes all of the names for each item in the game

    itemlist2 = ["a000","a902", "a903", "a904", "a905", "a910", "a112", "a113", "a114", "a115", "a116", "a221",
                "a222", "a223", "a224", "a331","a332", "a333", "a334", "a442", "a443",
                "a444", "a445", "a549", "a550", "a551", "a552", "a", "a1", "a2", "a3"]

    def points(Accessories, Headwear, Coats, TopsDresses, SocksTights, Shoes):
        
        """
        JA: 
        This function calculates the total point value for each category 
        (Cute, Goth, Casual, Formal, Elegant, Active)
        Using the specific point values of each item for each category.
        It returns a list with the total point values of each category
        [Cute, Goth, Casual, Formal, Elegant, Active]
        """
    
        # JA: These "if" statements uses the user's item name input, and assigns
        # JA: the point values of the item chosen to a new variable using itemlist1
    
        if Accessories in itemlist2:
            item1 = itemlist1[itemlist2.index(Accessories)]
        if Headwear in itemlist2:
            item2 = itemlist1[itemlist2.index(Headwear)]
        if Coats in itemlist2:
            item3 = itemlist1[itemlist2.index(Coats)]
        if TopsDresses in itemlist2:
            item4 = itemlist1[itemlist2.index(TopsDresses)]
        if SocksTights in itemlist2:
            item5 = itemlist1[itemlist2.index(SocksTights)]
        if Shoes in itemlist2:
            item6 = itemlist1[itemlist2.index(Shoes)]
    
        # JA: The following variables calculate the total point value for each 
        # JA: category, respectively. It uses each item's given point values from the
        # JA: code above and indexes them and adds all the respective values together
    
    
        Cute = (item1[0] + item2[0] + item3[0] + item4[0] + 
        item5[0] + item6[0])
    
        Goth = (item1[1] + item2[1] + item3[1] + item4[1] + 
        item5[1] + item6[1])
    
        Casual = (item1[2] + item2[2] + item3[2] + item4[2] + 
        item5[2] + item6[2])
    
        Formal = (item1[3] + item2[3] + item3[3] + item4[3] + 
        item5[3] + item6[3])
    
        Elegant = (item1[4] + item2[4] + item3[4] + item4[4] + 
        item5[4] + item6[4])
    
        Active = (item1[5] + item2[5] + item3[5] + item4[5] + 
        item5[5] + item6[5])
    
        # JA: This function returns a list with the total point values of each category
    
        return [Cute, Goth, Casual, Formal, Elegant, Active]

    def rank(FinalPoints):
    
        """
        JA: 
        This function calculates the final rank of each category using the
        total point values of each category from the list resulting from the
        "points" function.
        This function returns a letter score in a new list for each category.
        The letter options are: S, A, B, C, D, F
        """
    
        # JA: A while loop which checks every categories total point value and assigns
        # JA: a letter score to a new list based on how high the point value is 
    
        FinalRank = []
        i = 0
        while (i < len(FinalPoints)):
            if FinalPoints[i] > 19:
                FinalRank.append("S")
            elif FinalPoints[i] > 14:
                FinalRank.append("A")
            elif FinalPoints[i] > 9:
                FinalRank.append("B")
            elif FinalPoints[i] > 4:
                FinalRank.append("C")
            elif FinalPoints[i] > -1:
                FinalRank.append("D")
            elif FinalPoints[i] < 0:
                FinalRank.append("F")
            i += 1
    
        # JA: This function returns a new list with a letter score for each category
        # JA: respectively
    
        return FinalRank

    def calculate_points(accessory, headwear, coat, topDress, socksTights, shoes):
    
        """
        JA: 
        This function asks the user for which wearable item they are using.
        Using these items it calculates the final letter score using the "points"
        function and the "rank" function.
        The function then prints out the letter score for each category.
        Then the function closes.
        """
    
        # JA: Asking the user for the item name for each wearable
    
        Q1 = accessory
        Q2 = headwear
        Q3 = coat
        Q4 = topDress
        Q5 = socksTights
        Q6 = shoes
    
        # JA: Uses "points" function and "rank" function to create a new list
        # JA: which has the letter score for each category.
    
        FinalPoints = points(Q1, Q2, Q3, Q4, Q5, Q6)
        FinalRank = rank(FinalPoints)
    
    
        # JA: Closes the function
    
        return FinalRank

    # JA: Runs the calculation for the score of each category