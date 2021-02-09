import random
rock ='''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper ='''
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
'''

scissors='''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

images = [rock,paper,scissors]
print("Game of Rock Paper Scissors")
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper and 2 for Scissors \n"))
if user_choice <=2 and user_choice >=0:
    print(images[user_choice])
    cp_choice = random.randint(0,2)
    print("Computer choice")
    print(images[cp_choice])

    if user_choice == cp_choice:
        print("It is a draw")
    elif user_choice == 0 and cp_choice==2:
        print("You win!!!!")
    elif user_choice == 1 and cp_choice==0:
        print("You win!!!!")
    elif user_choice==2 and cp_choice==1:
        print("You win!!!!")
    else:
        print("You lose")
else:
    print("Invalid number, try again")