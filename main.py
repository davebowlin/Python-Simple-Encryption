def encrypt(message, key):
    # Encrypt the message using the key.
    ciphertext = ""
    for char in message:
        encrypted_char = chr(ord(char) + key)
        ciphertext += encrypted_char
    return ciphertext


def decrypt(ciphertext, key):
    # Decrypt the ciphertext using the key.
    plaintext = ""
    for char in ciphertext:
        decrypted_char = chr(ord(char) - key)
        plaintext += decrypted_char
    return plaintext


# Key cannot be larger than 1,114,111 for unicode characters (0x10FFFF in base 16) or it will produce a ValueError error.
encryption_key = 293 # Just a random prime number, change if desired.
again = True

# Perform encryption and decryption.
while again:
  message = input("Enter text message (blank to end):\n")
  if message == "":
    again = False
    
  encrypted_message = encrypt(message, encryption_key)
  decrypted_message = decrypt(encrypted_message, encryption_key)
  
  print("Encrypted message:", encrypted_message)
  print("Decrypted message:", decrypted_message)
  print("\n")
