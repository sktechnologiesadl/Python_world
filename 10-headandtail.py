#   ######################################
#			SK Technologies 
#	######################################
#Exercise : 10
#--------------


import random

print("Welcome to SKTechnologis \n "
      "today we are going to play dove aata")
head = 1
tails = 0

list_1 = [0,1]
#list_1 = ['tails','heads']
results = random.choice(list_1)
#print(results)
if results == 1:
    print("Heads")
else:
    print("Tails")