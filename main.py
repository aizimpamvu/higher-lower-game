import random
from art import logo,vs
from game_data import data

#displaying the logo
#randomly choose two super stars from the list
#ask the user to guess
#Write a function to compare
def check_answer(guess,a_followers):
  
#loop until you get it wrong
#count the score
#give the feedback
#making account at position B
def format_data(account):
  #get the format of the star name into printable format
  account_name=account["name"]
  account_description=account["description"]
  account_country=account["country"]
  return f"{account_name} a {account_description}, from {account_country}"
#clear the creen between rounds
print(logo)
right_answer=True
first_selected_star=[]
while right_answer:
  first_star_account=random.choice(data)
  second_star_account=random.choice(data)
  if first_star_account==second_star_account:
    second_star_account=random.choice(data)

  
  # Display both side of super start
  print(f" Compare A: {format_data(first_star_account)}")
  print(vs)
  print(f" Compare B: {format_data(second_star_account)}")
  guess=input("Who has more followers? Type 'A' or 'B': ").lower()
  account_follower=account["follower_count"]
  right_answer=False
  