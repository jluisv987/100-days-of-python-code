letters = ['a','b','c','d','e','f','g','h','i','j','k',
'l','m','n','o','p','q','r','s','t','u','v','w','x',
'y','z']
def encode(text,shift):
    enc_text=''
    for c in text:
        if letters.count(c)>0:
            position = letters.index(c)
            new_position = (position+shift)%26
            enc_text += letters[new_position]
        else:
            enc_text += c
    return enc_text

def decode(text,shift):
    dec_text =''
    for c in text:
        if letters.count(c)>0:
            position = letters.index(c)
            new_position = position-shift
            dec_text+=letters[new_position]
        else:
            dec_text+=c
    return dec_text

print("Caesar Cipher")

while True:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: \n")
    text = input("Type your message: \n").lower()
    shift = int(input("Type the shift number: \n"))
    if direction=='encode':
        print("Encrypted message is: ")
        print(encode(text,shift))
    
    elif direction=='decode':
        print("Decoded message is: ")
        print(decode(text,shift))
    
    exit = input("Do you want to encode/decode another message? Type 'yes' or 'no'")
    if exit == 'no':
        break