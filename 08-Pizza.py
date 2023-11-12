#   ######################################
#			SK Technologies 
#	######################################
#Exercise : 08
#--------------

print("Welcome to SK-Technologies \n \
     Do you wanna to eat Pizza 🍕🍕🍕🍕🍕....Let's play this")
# small_pizza = 100
# medium_pizza = 200
# large_pizza = 300
bill = 0
size = input("Kindly enter the Pizza which one you want {S/M/L}: ")
if size == 'S' or size == 's':
    bill += 100
    print(f"Small size Pizza price is {bill} INR ")
elif size == 'M' or size =='m':
    bill += 200
    print(f"Medium size Pizza is {bill} INR ")
elif size == 'L' or size == 'l':
    bill += 300
    print(f"Large size Pizza is {bill} INR ")

else:
    print("Hello excuse me ........enter the valid option 😏😏😏")
#print("Extra Pepporani 🧀 small_pizza = 30 & medium/large_pizza = 50 INR")
add_pepperoni = input("Do you want to add Pepperoni {Y/N}: ")
if add_pepperoni == 'Y' or add_pepperoni == 'y':
    if size == 'S' or size == 's':
        bill += 30
        print("For Extra Pepporani 30 INR")
    else:
        bill +=50
        print("For Extra Pepporani 50 INR")

#print("Extra Cheese 🧀 small/medium/large = 20 INR ")
extra_cheese = input("Do you want Extra Cheese {Y/N}: ")
if extra_cheese == 'Y' or extra_cheese == 'y':
    bill += 20
    print("For Extra Cheese 20 INR")
print(f"Your Final bill is {bill} INR")

