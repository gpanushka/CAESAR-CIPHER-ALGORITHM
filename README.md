# Caesar Cipher Algorithm

I created a python program that can encrypt and decrypt text using the Caesar Cipher Algorithm.

I have used resources like Visual Studio Code as the text editor and used internet resources for debugging.
The code for this task was carried out in four steps as below : 

**1. Variable Initialization:**

The program begins by establishing two crucial elements:

letters: This variable stores the entire lowercase alphabet as a string. It serves as a reference point for finding the positions of characters and performing the encryption/decryption shift.
num_letters: This variable holds the length of the alphabet, which is typically 26 for the lowercase alphabet. It's used for calculations involving the modulo operation to ensure the encrypted characters stay within the alphabet's boundaries.

![image](https://github.com/gpanushka/PRODIGY_CS_01/assets/167328539/88a0bf10-89a9-4f55-82b1-23db85311e10)

**2. encrypt Function:**
   
The encrypt function takes the message and key to scramble it. It starts with an empty string to hold the encrypted message. It then checks each character in the original message. Spaces and symbols are usually left unchanged.

For letters, it finds their position in the alphabet (a = 0, b = 1, etc.). The key value is added to this position, but it might wrap around the alphabet. To keep it within the letters (A-Z), a special calculation (modulo operation) is used. Finally, the new encrypted letter (shifted by the key) is added to the growing encrypted message. Once done with all characters, the encrypted message is returned.

![image](https://github.com/gpanushka/PRODIGY_CS_01/assets/167328539/abfc06ea-d57f-4f80-91c9-e608beb3d3de)

**3. decrypt Function:**

Unlike encryption, decryption works backwards to reveal the original message. It starts with an empty string for the decrypted message. Similar to encryption, it processes each character in the ciphertext, skipping symbols and spaces.

For letters, it finds their position in the alphabet. This time, the key is subtracted, but the result might be negative. To keep it within the alphabet's range, the modulo operation is used again. Finally, the decrypted letter (shifted back by the key) is added to the growing decrypted message. After processing all characters, the original message is retrieved. 

![image](https://github.com/gpanushka/PRODIGY_CS_01/assets/167328539/410a7d2c-0084-4c20-bfe6-d5c7e58c40bc)

**4. User Input and Program Flow:**

The program starts by welcoming the user and offering a choice: encrypt or decrypt. Based on the user's selection (e for encrypt or d for decrypt), it prompts for the key value and the text to be processed. The appropriate function (encrypt or decrypt) is then called with the provided input. Finally, the resulting ciphertext (for encryption) or plaintext (for decryption) is displayed for the user.

![image](https://github.com/gpanushka/PRODIGY_CS_01/assets/167328539/6f941cb5-803a-4d0d-83da-b3bac322e0b4)


**OUTPUT:**

![image](https://github.com/gpanushka/PRODIGY_CS_01/assets/167328539/b5e76cb4-fdbb-4a79-81e6-33667c1170c9)

![image](https://github.com/gpanushka/PRODIGY_CS_01/assets/167328539/9f448634-9241-4f25-9e8c-a9abf6aaecbb)

