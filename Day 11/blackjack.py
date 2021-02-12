import random
cards =[11,2,3,4,5,6,7,8,9,10,10,10,10]

def get_card():
    return random.choice(cards)

def get_score(hand):
    hand.sort()
    total = 0
    for x in hand:
        if total>21 and x ==11:
            total +=1
        else:
            total+=x
    return total

def results(player,pc):
    s_player = sum(player)
    s_pc = sum(pc)
    if s_player >21 or s_pc==21:
        return "You Lose"
    elif s_pc>21 and s_player<21:
        return "You win"
    elif s_player==s_pc:
        return "Draw"
    elif s_player<=21 and s_player>s_pc:
        return "You Win"
    elif s_pc>s_player:
        return "You Lose"

play = input("Black Jack game\nType 'yes' or 'no' to start playing\n")
while play == 'yes':
    player = []
    pc =[]
    player.append(get_card())
    player.append(get_card())
    print("Player current hand")
    print(player)
    print(f"Player Total score:{get_score(player)}")
    pc.append(get_card())
    print("PC current hand")
    print(pc)
    pc.append(get_card())
    choice = "hit"
    while get_score(player)<21 and choice == "hit":
        choice = input("Type 'hit' or 'stand'\n")
        if choice == "hit":
            player.append(get_card())
            print("Player current hand")
            print(player)
            print(f"Player Total score:{get_score(player)}")

    while get_score(pc)<17:
        pc.append(get_card())

    print("PC current hand")
    print(pc)   
    print(f"PC Total score:{get_score(pc)}") 
    print(results(player,pc))
    play = input("Type 'yes' or 'no' to restart playing\n")