#this is an bmi caluclator 
weight = float(input("enter your weight :"))
height = float(input("enter your height :"))

bmi = weight / (height*height)
print("your bmi is:", round(bmi, 2))
#this is an rock pape siccors game developed by me 
import random

def get_choices():
    player_choice = input("enter a choice ""rock , paper, siccors:")
    comp_choice = ["rock", "paper", "siccors"]
    computer_choice = random.choice(comp_choice)
    
    return computer_choice
    
choices = get_choices()
print(choices)
