import random
def difficulty(o):
    if o == 'easy':
        return 10
    elif o == 'hard':
        return 5

def guess(g,num):
    if g == num:
        print("You guess the number, you win!")
        return 1
    elif num-10>=g:
        print("Your number is too small")
    elif num>=g:
        print("Nice guess from the right")
    elif g-10>=num:
        print("Your number is too high")
    elif g>=num:
        print("Nice guess from the left")
    return 0

print("Guess the number game")
num = random.randint(1,100)
opt= input("Select the difficulty, type 'easy' or 'hard' \n").lower()
lifes = difficulty(opt)

g = 0
while(lifes>0):
    print(f"You have {lifes} lifes left")
    g = int(input("Guess the number? \n"))
    if not(guess(g,num)):
        lifes-=1
    else:
        break