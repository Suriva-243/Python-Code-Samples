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


UR_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors: "))
if UR_choice == 0:
    print("Your choice is rock "+rock)
elif UR_choice == 1:
    print("Your Choice is Paper "+paper)
elif UR_choice == 2:
    print("Your Choice is scissors " + scissors)
print(UR_choice)

Computer_choice = random.randint(0,2)
if  UR_choice > 2:
        print(f"Invalid Entry")
        print("Restart game to play!")
if Computer_choice == 0 and UR_choice == 0:
        print(f"Computer Choice is Rock "+rock)
        print("It's a draw!")
if Computer_choice == 0 and UR_choice == 1:
        print(f"Computer Choice is Rock" + rock)
        print("You win!")
if Computer_choice == 0 and UR_choice == 2:
        print(f"Computer Choice is Rock" + rock)
        print("You Loose!")
if Computer_choice == 1 and UR_choice == 0:
        print(f"Computer Choice is Paper" + paper)
        print("You win!")
if Computer_choice == 1 and UR_choice == 1:
        print(f"Computer Choice is Paper" + paper)
        print("It's a draw!")
if Computer_choice == 1 and UR_choice == 2:
        print(f"Computer Choice is Paper" + paper)
        print("You win!")
if Computer_choice == 2 and UR_choice == 0:
        print(f"Computer Choice is scissors" + scissors)
        print("You win!")
if Computer_choice == 2 and UR_choice == 1:
        print(f"Computer Choice is scissors" + scissors)
        print("You Lose!")
if Computer_choice == 2 and UR_choice == 2:
        print(f"Computer Choice is scissors" + scissors)
        print("It's a draw!")



