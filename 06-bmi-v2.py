#   ######################################
#			SK Technologies 
#	######################################
#Exercise : 06
#--------------

print("Welcome to SK-Technologies \n \
     BMI Value advanced version ")

height = float(input("Enter your height in meters: "))
weight = int(input("Enter your weight in kgs: "))
bmi = round(weight / height ** 2)
print(bmi)
if bmi <= 15:
    print(f"The BMI value is {bmi} , You are too much under weight \n Take extra food Try to increase your weight")
elif bmi <= 20:
    print(f"The BMI value is {bmi} , You are under weight \n"
          f"Try to increase your weight")
elif bmi <= 25:
    print(f"The BMI value is {bmi} , You are in Normal range \n Keep it up ")
elif bmi <= 30:
    print(f"The BMI value is {bmi} , You are okay but slight Obese \n"
          f"Try to do Jagging/Walking daily basis Good Luck!")
elif bmi <=35:
    print(f"The BMI value is {bmi} , You are too much weight \n"
          f"Take immediate action --- Running/Jaggin/Walking/Yoga would be great if you follow")
else:
    print("God will help you ........Arey entra intha Lav unnav😱😱😱😱😱😱😱😱😱")