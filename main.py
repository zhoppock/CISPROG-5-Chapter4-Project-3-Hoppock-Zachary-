def encryption(text, distanceValue):
  plainText = text
  distance = int(distanceValue)
  code = ""
  for ch in plainText:
    ordvalue = ord(ch)
    cipherValue = ordvalue + distance
    if cipherValue > ord('~'):
      cipherValue = ord('!') + distance - (ord('~') - ordvalue + 1)
    code += chr(cipherValue)
  print("\nThe encrypted text is:")
  print(code)
  return code

def decryption(code, distanceValue):
  encryptedText = code
  distance = int(distanceValue)
  text = ""
  for ch in encryptedText:
    ordvalue = ord(ch)
    cipherValue = ordvalue - distance
    if cipherValue < ord('!'):
      cipherValue = ord('~') - (distance - abs(ord('!') - ordvalue - 1))
    text += chr(cipherValue)
  print("\nThe decrypted text is:")
  print(text)
  return text


f = open("textfile.txt", 'w')
f.write("First line.\nSecond line.\n")
f.close()

f = open("textfile.txt", 'r')
text = f.read()
print("Text file to encrypt:")
print(text)
distanceValue = input("Please input a distance value: ")

e = open("encrypt_file.txt","w")
e.write(encryption(text, distanceValue))

f.close()
e.close()

e = open("encrypt_file.txt", 'r')
code = e.read()
print("\nText file to unencrypt:")
print(code)

u = open("unencrypt_file.txt","w")
u.write(decryption(code, distanceValue))

e.close()
u.close()