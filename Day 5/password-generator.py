import random

letters = ['a','b','c','d','e','f','g','h','i','j','k',
'l','m','n','o','p','q','r','s','t','u','v','w','x',
'y','z','A','B','C','D','E','F','G','H','I','J','K',
'L','M','N','O','P','Q','R','S','T','U','V','W','X',
'Y','Z']
numbers = ['0','1','2','3','4','5','6','7','8','9']

symbols = ['!','#','$','%','&','(',')','*','+']

print("Password generator")
nletters = int(input("How many letters would you like in your password ? \n"))
nsymbol = int(input("How many symbols would you like in your password ? \n"))
nnumber = int(input("How many numbers would you like in your password ? \n"))
total = nletters+nsymbol+nnumber
passwordl = []
for x in range(1,nletters+1):
    passwordl.append(random.choice(letters))
for x in range(1,nnumber+1):
    passwordl.append(random.choice(numbers))
for x in range(1,nsymbol+1):
    passwordl.append(random.choice(symbols))

random.shuffle(passwordl)
password = ''
for x in passwordl:
    password+=x

print(f"Your new password is: {password}")

