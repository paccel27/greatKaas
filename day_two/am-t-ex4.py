print ("Ceasar Cipher")

plaintext = input ("What is your message: ")

keyshift= int(input ("How many characters do you want to shift? "))

ciphertext = ""


print(ord('a'),'a')
print(ord('A'),'A')
print(ord('z'),'z')
print(ord('Z'),'Z')

for letter in plaintext:
	upperlower = ord(letter)
	if upperlower >= 65 and upperlower <= 90:
		if upperlower + keyshift > 90:
			ciphertext = ciphertext + chr(ord(letter)+keyshift-26)
		elif upperlower + keyshift < 65:
			ciphertext = ciphertext + chr(ord(letter)+keyshift+26)
		else: 
			ciphertext = ciphertext + chr(ord(letter)+keyshift)

	if upperlower >= 97 and upperlower <= 122:
		if upperlower + keyshift > 122:
			ciphertext = ciphertext + chr(ord(letter)+keyshift-26)
		elif upperlower + keyshift < 97:
			ciphertext = ciphertext + chr(ord(letter)+keyshift+26)
		else: 
			ciphertext = ciphertext + chr(ord(letter)+keyshift)

	if upperlower <65 or upperlower > 122:
		ciphertext += etter
	if upperlower > 90 and upperlower < 97:
		ciphertext += letter
	
print (plaintext)
print (ciphertext)


