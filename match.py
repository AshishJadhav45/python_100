x = 4

match x :
    case 0:
        print("x is zero")
# case with if - condition 

    case 4 if x % 2 == 0:
        print("x % 2==0 and case is 4")

        # empty case with if - conditon

    case _ if x < 10:
        print("x is < 10")
    
    case _ :
        print(x)
    