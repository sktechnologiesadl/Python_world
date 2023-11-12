#   ######################################
#			SK Technologies 
#	######################################
#Exercise : 03 Calculating of BMI 
#--------------

print("Welcome to SK-Technologies \n \
     Calculating of BMI value ")

height = float(input("Enter your height in meters: "))
weight = int(input("Enter your weight in kgs: "))

bmi = weight / height ** 2
print(round(bmi))
