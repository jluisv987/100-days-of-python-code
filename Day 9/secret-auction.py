
auction = {}

def max_offer(auction):
    max = -1
    winner = ''
    for bidder in auction:
        if auction[bidder]>max:
            max = auction[bidder]
            winner=bidder
    return winner

print("Welcome to the secret auction")
while True:
    name = input("Input your name: \n")
    offer = float(input("Your offer: \n"))
    auction[name] = offer
    exit = input("Are there any more offers? type 'yes' or 'no'")
    if exit == 'no':
        break

win = max_offer(auction)
print(f"The winner of the auction is {win} with ${auction[win]}")