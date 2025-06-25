#Number Check
InputNumber = int(input("Number to guess:"))

if InputNumber > 0:
    print("It's Possitive Number")
elif InputNumber < 0:
    print("It's Negative Number")
else:
    print("The Number is Zero")       
