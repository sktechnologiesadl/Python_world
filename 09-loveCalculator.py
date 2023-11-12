#   ######################################
#			SK Technologies 
#	######################################
#Exercise : 09
#--------------

print("Welcome to SKTechnologies \n \
      We are creating an interesting Love Calculator")

first_name = input("Enter your name: ")
crush_name = input("Enter your crush name: ")
first_name = first_name.lower()
crush_name = crush_name.lower()
combined_name = first_name + crush_name
#print(combined_name)
print(f"My name is {first_name} and my crush name is {crush_name}")

t = combined_name.count('t')
r = combined_name.count('r')
u = combined_name.count('u')
e = combined_name.count('e')

l = combined_name.count('l')
o = combined_name.count('o')
v = combined_name.count('v')
e = combined_name.count('e')

result = t + r + u + e
result_2 = l + o + v + e
final = int(str(result) + str(result_2))
print(f"Your love score is {final}")
if final < 10 or final > 90:
    print('Your love is Extrem')
elif final < 30:
    print('Your love is average')
elif final > 30 and final < 50:
    print('You are okay not that much deep')
elif final > 50 and final <70:
    print('You are very good keep it up')
else:
    print('You are the best lovers made for each others')