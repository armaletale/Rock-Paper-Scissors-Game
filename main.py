import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

choice = input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors. ")

computer_choice = [rock, paper, scissors]

random_integer = random.randint(0, 2)

comp_ans = computer_choice[random_integer]


ans =int(choice)

if ans == 0:
  print(f"{rock}\ncomputer chose:\n{comp_ans}")
  if rock == computer_choice[0] and comp_ans == computer_choice[0] :
    print("Draw!")
  elif rock == computer_choice[0] and comp_ans == computer_choice[1]:
    print("You Lose!")
  elif rock == computer_choice[0] and comp_ans == computer_choice[2]:
    print("You Win!")
    
elif ans == 1:
  print(f"{paper}\ncomputer chose:\n{comp_ans}")
  if paper == computer_choice[1] and comp_ans == computer_choice[0] :
    print("You Win!")
  elif paper == computer_choice[1] and comp_ans == computer_choice[1]:
    print("Draw!")
  elif paper == computer_choice[1] and comp_ans == computer_choice[2]:
    print("You Lose!")

elif ans == 2:
  print(f"{scissors}\ncomputer chose:\n{comp_ans}")
  if scissors == computer_choice[2] and comp_ans == computer_choice[0] :
    print("You Lose!")
  elif scissors == computer_choice[2] and comp_ans == computer_choice[1]:
    print("You Win!")
  elif scissors == computer_choice[2] and comp_ans == computer_choice[2]:
    print("Draw!")
else:
  print("Bad Loser")


