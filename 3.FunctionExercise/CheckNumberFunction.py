def CheckNumber():
    userInut = float(input("Enter The Number"))
    if userInut % 2 == 0:
        print("The Number is even")
    else:
        print("The Number is odd")
    return CheckNumber()
CheckNumber()