"""
Jason Anandappa
21070211

"""


# JA: PV = Point Value
# JA: This is how each of the item's point values are assigned
# JA: "Category Names" = [Cute PV, Goth PV, Casual PV, Formal PV, Elegant PV, Active PV]

# JA: Choice of Accessories

a902 = [1,	-2,	2,	1,	0,	2]
a903 = [2,	3,	0,	-2,	-1,	-2]
a904 = [0,	0,	1,	3,	1,	0]

# JA: Choice of Headwear

a112 = [3,	0,	3,	-1,	-1,	0]
a113 = [2,	3,	0,	-2,	-2,	-2]
a114 = [1,	0,	2,	3,	1,	0]
a115 = [3,	1,	2,	0,	0,	0]

# JA: Choice of Coats

a221 = [3,	-3,	5,	0,	-2,	4]
a222 = [3,	5,	0,	-2,	2,	-1]
a223 = [1,	0,	-1,	5,	2,	-1]

# JA: Choice of TopsDresses

a331 = [3,	-5,	5,	1,	-1,	4]
a332 = [2,	5,	-2,	-2,	2,	-5]
a333 = [1,	0,	1,	5,	3,	0]

# JA: Choice of Socks/Tights

a442 = [2,	1,	3,	0,	-1,	2]
a443 = [2,	4,	1,	-2,	0,	-2]
a444 = [1,	0,	2,	3,	1,	0]

# JA: Choice of Shoes

a549 = [3,	-2,	4,	0,	-1,	2]
a550 = [3,	4,	-1,	1,	2,	-2]
a551 = [1,	2,	2,	4,	3,	-1]

# JA: The following itemlist includes all of the items in the game with their 
# JA: point values for each category

itemlist1 = [a902, a903, a904, a112, a113, a114, a115, a221, a222, a223, a331,
            a332, a333, a442, a443, a444, a549, a550, a551]

# JA: The following itemlist includes all of the names for each item in the game

itemlist2 = ["a902", "a903", "a904", "a112", "a113", "a114", "a115", "a221",
             "a222", "a223", "a331","a332", "a333", "a442", "a443",
             "a444", "a549", "a550", "a551"]

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

def calculate_points():
    
    """
    JA: 
    This function asks the user for which wearable item they are using.
    Using these items it calculates the final letter score using the "points"
    function and the "rank" function.
    The function then prints out the letter score for each category.
    Then the function closes.
    """
    
    # JA: Asking the user for the item name for each wearable
    
    Q1 = input("What is your Accessory? (a902,a903,a904): ")
    Q2 = input("What is your Headwear? (a112,a113,a114,a115): ")
    Q3 = input("What is your Coat? (a221, a222, a223): ")
    Q4 = input("What is your Top/Dress? (a331, a332, a333):")
    Q5 = input("What are your Socks/Tights? (a442, a443, a444): ")
    Q6 = input("What are your Shoes? (a549, a550, a551): ")
    
    # JA: Uses "points" function and "rank" function to create a new list
    # JA: which has the letter score for each category.
    
    FinalPoints = points(Q1, Q2, Q3, Q4, Q5, Q6)
    FinalRank = rank(FinalPoints)
    
    # JA: Prints out the letter score for its respective category
    
    print("\nCute Rank: ", FinalRank[0], "\nGoth Rank: ", FinalRank[1], 
          "\nCasual Rank: ", FinalRank[2], "\nFormal Rank: ", FinalRank[3],
          "\nElegant Rank: ", FinalRank[4], "\nActive Rank: ", FinalRank[5])
    
    # JA: Closes the function
    
    return

# JA: Runs the calculation for the score of each category

calculate_points()