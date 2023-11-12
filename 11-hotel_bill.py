#   ######################################
#			SK Technologies 
#	######################################
#Exercise : 11
#--------------


import random

print("Welcome to SK Technologies \n"
      "Today we will have some fun on paying the Hotaal Bill")
names = input("Enter your friends names: ")

names_list = []
names_list = names.split()
print(names_list)
# bill_payer = random.choice(names_list)
# print(f" Today {bill_payer} is the lucky person so he will pay the bill")

length = len(names_list)
lucky_no = random.randint(0,length-1)

bill_payer = names_list[lucky_no]
print(bill_payer)