#this is an rock pape siccors game developed by me 
import random

def get_choices():
    player_choice = input("enter a choice ""rock , paper, siccors:")
    comp_choice = ["rock", "paper", "siccors"]
    computer_choice = random.choice(comp_choice)
    
    return computer_choice
    
choices = get_choices()
print(choices)
