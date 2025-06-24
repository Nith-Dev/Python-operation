# If and else Statement
Age = 16
if Age > 16:
    print("You are  eligible")
else:
    print("You are not")

#If elif and else
Age = 20
Score = 60

if Age >= 20 and Score >= 60:
    print("You are passed the exam")
elif Age > 20 and Score < 60:
    print("You failed the exam ")
else:
    print("Check the result")


# Ternary Operator
Score = 60
Reuslt = "Pass" if Score >= 50 else "fail"
print(Reuslt)

# Switch Statement

day = "Monday"
match day: 
    case "Monday":
        print("Monday")
    case "Tuesday":
        print("Tuesday")
    case _:
        print("The rest of the week")