#   ######################################
#			SK Technologies 
#	######################################
#Exercise : 07
#--------------

print("Welcome to SK-Technologies \n \
     Find out Leap year or not")
year = int(input("Can you enter the year: "))
if year % 4 == 0:
    #print("This is Leap Year")
    if year % 100 == 0:
        #print("This is not Leap Year")
        if year % 400 == 0:
            print(f"The entered year {year} is Leap Year")
        else:
            print(f"The entered year {year} is not Leap Year")
    else:
        print(f"The entered year {year} is Leap Year")
else:
    print(f"The entered year {year} is not Leap Year")