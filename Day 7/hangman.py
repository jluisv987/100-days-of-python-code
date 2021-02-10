import random
life =5
word_list = ["python","program","day","coding","green"]
word = random.choice(word_list)
print("Hangman game")
win =0
letter = input("Type a letter to play \n").lower()
correctw =[]
for c in word:
    correctw.append('_')
print(correctw)

while life>0:
    print(f"Current lifes {life}")
    letter = input("Guess the letter \n").lower()
    x=0
    correct = 0
    for c in word:
        if c == letter:
            correctw[x] = c
            correct=1
        x+=1
    if correct==0:
        print("You did not guess right, you lose a life")
        life-=1
    print(correctw)
    if correctw.count('_')==0:
        print("You win the game!!!!")
        break

if life ==0:
    print("You run out of lifes, game over")