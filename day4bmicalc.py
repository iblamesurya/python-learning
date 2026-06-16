#this is an bmi caluclator 
weight = float(input("enter your weight :"))
height = float(input("enter your height :"))

bmi = weight / (height*height)
print("your bmi is:", round(bmi, 2))
