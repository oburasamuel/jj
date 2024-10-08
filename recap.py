# prompt user for input
# check for the input
# computer's input
# print the choices
# print the winner
# DO YOU WANT TO CONTINUE
# quit

import random


# emoji = {
#   'r': 'D',
#   'p': 'P',
#   's': 'X'
# }

# choices = ('r', 'p', 's')

# while True:
#     user_choice = input("rock, paper, scissors? (r/p/s): ")

#     if user_choice not in choices:
#         print("invalid choice try again!")
#         continue
    
#     computer_choice = random.choice(choices)

#     print(f'You chose{emoji[user_choice]}')
#     print(f'Computer chose{emoji[computer_choice]}')

#     if user_choice == computer_choice:
#         print('Tie!')

#     elif ((user_choice == 's' and computer_choice == 'r') or 
#           (user_choice == 'p' and computer_choice == 's') or
#           (user_choice == 'r' and computer_choice == 'p')):
#         print("You won")

#     else:
#         print("You lose")
    
#         should_continue = input("Do you want to continue? (y/n): ").lower()

#         if should_continue == 'n':
#             break
            

# //Dice game

# prompt the user to play
# how many times you want to roll the dice
# check if the user has rolled the right number
# if not continue or exit
# print if he/she won


while True:
  roll_dice = input("Do you want to roll a dice? (y/n): ").lower
  roll_times = input("How many times do you want to roll: ")
  count = 0

  if roll_dice == 'y':
      number = random.randint(1, 25)
      num = random.randint(50, 100)
      count += 1

      if count > int(roll_times):
        break
      print(f'you rolled a {number} and {num}')

  elif roll_dice == 'n':
      print("Okay see you later")

  else:
      print("Invalid choice! Try again")
      break