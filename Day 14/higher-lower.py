import random
search={"Computer":3650,"Music":8280,"Water":5760,"Python":448,"Chocolate":1330,"Mexico":1590,"Google":10360,"C++":85,"US":6220}

def compare_two(na,nb):
    if na>nb:
        return 0
    else:
        return 1

score = 0
print("Higher and lower game\n")
while True:
    ka = random.choice(list(search.keys()))
    kb = random.choice(list(search.keys()))
    while kb == ka:
        kb = random.choice(list(search.keys()))
    print(f"Current score {score}\n")
    opt = input(f"Between a) {ka} and b) {kb} who has more results in Google?\n Type 'a' or 'b'\n")
    if opt == 'a' and compare_two(search[ka],search[kb])==0 :
        score+=1
        print("Correct")
    elif opt == 'b' and compare_two(search[ka],search[kb])==1 :
        score+=1   
        print("Correct")
    else:
        print(f"Game over!, your final score is {score}")
        break