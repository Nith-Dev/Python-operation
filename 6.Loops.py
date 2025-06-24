# For loop
Age = [1,5,6,7,8]
for count in Age:
 print(count)

# While Loop
count = 0
while count < 5:
    print(count)
    count += 1

# Break Loop
Age = [20,30,40,50]
for i in Age:
   if i == 40:
      break
   print(i)

# Continues
Age = [ 10,20,30,40,50,60]
for i in Age:
   if i == 20:
      continue
   print(i)


# else with loop with break
Score = [ 10,20,30,40,50,60]
for i in Score:
   if i in Score:
      if i == 40:
        break
      print(i)
else:
   print("Block")

# else with loop
for i in range(3):
    print(i)
else:
   print("Check")
