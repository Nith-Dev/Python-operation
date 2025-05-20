# IF Statement
age = int(input("Input your age:"))
if(age >= 18):{
    print('You are eligible')
}

# If and Else Statement
grade = int(input("Check your score"))
if grade >= 50:
    print('You Pass the exam')
else:
    print("Study more harder") 

# if-elif-else Statement
gradeCheck = int(input("Enter your score to check your grade:"))
if gradeCheck < 50:
    print("You fail the class")
elif gradeCheck < 70:
    print("You get the medimum score")
elif gradeCheck < 85 :
    print("You pass the exam with excellent score")
else:
    print("Study harder")

# Nested if Statement
Citizen = True
age = 26

if age >= 20:
    if Citizen == True:
        print("You are eligible to vote")
    else:
        print|('You must be citizen first')
else:
        print('You are too young to vote')