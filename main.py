import random
from art import logo,vs
from game_data import data

#displaying the logo
#randomly choose two super stars from the list
#ask the user to guess
#Write a function to compare

def check_answer(guess,a_followers,b_followers):
  if a_followers>b_followers:
    return guess=="a"
  else:
    return guess=="b"
      
#loop until you get it wrong
#count the score
#making account at position B
def format_data(account):
  #get the format of the star name into printable format
  account_name=account["name"]
  account_description=account["description"]
  account_country=account["country"]
  return f"{account_name} a {account_description}, from {account_country}"
#clear the creen between rounds
print(logo)
score=0
right_answer=True
first_selected_star=[]
second_star_account=random.choice(data)
while right_answer:
  first_star_account=second_star_account
  second_star_account=random.choice(data)
  if first_star_account==second_star_account:
    second_star_account=random.choice(data)

  
  # Display both side of super start
  print(f" Compare A: {format_data(first_star_account)}")
  print(vs)
  print(f" Compare B: {format_data(second_star_account)}")
  guess=input("Who has more followers? Type 'A' or 'B': ").lower()
  a_followers=first_star_account["follower_count"]
  b_followers=second_star_account["follower_count"]
  is_correct=check_answer(guess,a_followers,b_followers)
  #give the feedback
  if is_correct:
    print("You are right!, you got it!")
    score+=1
  else:
    print(f"Sorry that's wrong. Your final score is {score}")
    right_answer=False
  