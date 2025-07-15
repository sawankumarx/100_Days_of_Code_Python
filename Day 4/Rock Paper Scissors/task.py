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
user_input = int(input("What do you choose? Type 0 for Rock , 1 for Paper of 2 for Scissors.\n"))
computer_input = random.randint(0,2)

game_images = [rock, paper, scissors]

if 0<=user_input<=2:
    print(f"You choose\n{game_images[user_input]}")
    print(f"Computer choose\n{game_images[computer_input]}")

    if user_input == computer_input:
        print("It's tie!")
    else:
        if user_input == 0 and computer_input == 1:
            print("You lose!")
        elif user_input == 0 and computer_input == 2:
            print("You win!")
        elif user_input == 1 and computer_input == 0:
            print("You win!")
        elif user_input == 1 and computer_input == 2:
            print("You lose!")
        elif user_input == 2 and computer_input == 0:
            print("You lose!")
        elif user_input == 2 and computer_input == 1:
            print("You win!")


else:
    print("You typed wrong number. You lose!")



# if 0<=user_input<=2:
#     print(f"You choose\n{values[user_input]}")
#     print(f"Computer choose\n{values[computer_input]}")
#     if computer_input == user_input:
#         print("Its draw")
#     elif computer_input < user_input:
#         if user_input - computer_input == 1:
#             print("you lose!")
#         else:
#             print("you win!")
#     elif computer_input > user_input:
#         if computer_input - user_input == 1:
#             print("you win!")
#         else:
#             print("you lose!")
#
# else:
#     print("You typed invalid number. You lose!")


