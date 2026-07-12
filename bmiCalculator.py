#23-06-26
#Given a weight in pounds and a height in inches, return the BMI (Body Mass Index) rounded to one decimal place.
#To get BMI: divide the weight by the height squared, then multiply the result by 703.
def calculate_bmi(weight, height):
    bmi=(weight/height**2)*703
    return round(bmi,1)

weight=float(input("Enter weight in pounds: "))
height=float(input("Enter height in inches: "))
bmi=calculate_bmi(weight, height)
print(bmi)