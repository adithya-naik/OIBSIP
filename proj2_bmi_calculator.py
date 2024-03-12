#COMMAND LINE APPLICATION FOR CALCULATING BMI(BODY MASS INDEX)

#Author : Jatoth Adithya Naik
#for    : Intenship (PROJECT-2)

# Discription :
# this command appplication calculates BMI of the user
# user has to give weight in kilograms, height in meters

# category ranges :
# Underweight: BMI less than 18.5
# Normal weight: BMI of 18.5 to 24.9
# Overweight: BMI of 25 to 29.9
# Obesity: BMI of 30 or higher


print("\n\n\t\t\tby @JATOTH ADITHYA NAIK")
print("________________________________________")
print("\n\t\t\t***BMI CALCULATOR APP***\n")
weight = float(input("\tEnter your Weight (in Kilograms) : "))
print("\n")
height = float(input("\tEnter your Height (in meters) : "))

bmi = (weight)/(height*height)

print("\n\t\tBMI VALUE : ",bmi," kg/m*m")

if(bmi<18.5):
    print("\n\t\t  Category : Under Weight")
elif(bmi>=18.5 and bmi<=24.9):
    print("\n\t\t  Category : Normal Weight")
elif(bmi>=25 and bmi<=29.9):
    print("\n\t\t  Category : Over Weight")
elif(bmi>=30):
    print("\n\t\t  Category : Obesity")
print("\n")