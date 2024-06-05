#CAESAR CIPHER ALGORITHM

letters = 'abcdefghijklmnopqrstuvwxyz'
num_letters = len(letters)

#Encrypt function for encryption of input data
def encrypt(plaintext, key): 
    ciphertext = ''
    for letter in plaintext:
        letter = letter.lower()
        if not letter == ' ':
            index = letters.find(letter)
            if index == -1 :
                ciphertext += letter
            else:
                newindex = index + key
                if newindex >= num_letters:
                    newindex -= num_letters
                ciphertext += letters[newindex]
    return ciphertext

#Decrypt function for decryption of input data
def decrypt(ciphertext, key): 
    plaintext = ''
    for letter in ciphertext:
        letter = letter.lower()
        if not letter == ' ':
            index = letters.find(letter)
            if index == -1 :
                plaintext += letter
            else:
                newindex = index - key
                if newindex < 0 :
                    newindex += num_letters
                plaintext += letters[newindex]
    return plaintext

#Input for the process you want to do
print('Do you want to encrypt or decrypt?')
user_input=input("e: Encrypt or d: Decrypt : ").lower()
print()

if user_input == 'e':
    print('Encryption Mode Selected')
    print()
    key=int(input('Enter the key (1 through 26): '))
    text=input('Text to encrpyt:')
    ciphertext = encrypt(text, key)
    print(f'CIPHERTEXT: {ciphertext}')

elif user_input == 'd':
    print('Decryption Mode Selected')
    print()
    key=int(input('Enter the key (1 through 26): '))
    text=input('Text to decrpyt:')
    plaintext = decrypt(text, key)
    print(f'CIPHERTEXT: {plaintext}')
