#   ######################################
#			SK Technologies 
#	######################################
#Exercise : 11
#--------------


print("Welcome to SKTechnologies \n"
      "We are hiding our money in Cubic Box")
x1 = ["😍","😍","😍"]
x2 = ["😍","😍","😍"]
x3 = ["😍","😍","😍"]
#z1 = x1 + x2 + x3
#print(z1)
#z1 = print(f"{x1}\n{x2}\n{x3}")
z1 = [x1 , x2 , x3]
# z1[2][1] = 'S'
number = input("Enter the Row and Column number where you want to hide money: ")

row = int(number[0])
col = int(number[1])
print("Now see where you kept your money")
# print(row)
# print(col)
# y1 = z1[row-1]
# y1[col-1] = 'S'
z1[row-1][col-1] = 'S'
#print(y1)
z1 = print(f"{x1}\n{x2}\n{x3}")





