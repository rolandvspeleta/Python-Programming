import random
import string

chars = " " + string.punctuation + string.digits + string.ascii_letters
chars = list(chars)
key = chars.copy()

random.shuffle(key)

running = True
while running:
  
  plain_text = input("Enter a message to encrypt: ")
  cipher_text = ""

  for letter in plain_text:
      index = chars.index(letter)
      cipher_text += key[index]
  print(f"Original Message: {plain_text}")
  print(f"Encrypted Message: {cipher_text}")
  new_action = input("Encrypt another word or Decrypt word (e/d): ")
  if new_action == "e":
      running = False
  else:
      plain_text = ""
      print(f"Decrypting {cipher_text}")
      for letter in cipher_text:
        index = key.index(letter)
        plain_text += chars[index]
      print(f"Decrypted Message: {plain_text}")


