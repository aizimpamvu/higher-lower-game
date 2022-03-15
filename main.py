import random
from art import logo
from game_data import data

#displaying the logo
#randomly choose two super stars from the list
#ask the user to guess
#Write a function to compare
#loop until you get it wrong
#count the score
#give the feedback
print(logo)
right_answer=True
first_selected_star=[]
while right_answer:
  first_star=random.choice(data)
  for first in first_star:
    
  print(first_star)
  right_answer=False
  