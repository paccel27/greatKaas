#
# Caesar Cipher
#  
# plaintext = (input("Enter your Caesar string: "))
# key = int(input("What is your Caesar key?"))
# if key > 25:
# 	key = key % 26
ciphertext =''

def ceasarcipher(plaintext,key):
	ciphertext = ""

	for letter in plaintext:
		if ord(letter) in range(65,91):
			cletter = ord(letter)+key
			if cletter in range (65,91):
				ciphertext += chr(cletter)
			elif cletter >= 91:
				ciphertext += chr(cletter-26)
			elif cletter < 65:
				ciphertext += chr(cletter+26)
		if ord(letter) in range(97,123):
			cletter = ord(letter)+key
			if cletter in range (97,123):
				ciphertext += chr(cletter)
			elif cletter >= 123:
				ciphertext += chr(cletter-26)
			elif cletter < 97:
				ciphertext += chr(cletter+26)
	return ciphertext

# ciphertext = ceasarcipher(plaintext,key)
# print ("Ciphertext is: ",ciphertext)

def vignerecipher(vplaintext,vkey):
	vciphertext = ""
	keylist = []
	for letter in vkey:
		if ord(letter) in range(65,91):
			keylist.append(ord(letter)-65)
		elif ord(letter) in range(97,123):
			keylist.append(ord(letter)-97)
	print (keylist)

	i=0
	for letter in vplaintext:
		i+=1
		if i == len(keylist):
			i=0
		vciphertext += ceasarcipher(letter,keylist[i-1])
		
	return vciphertext


vplaintext = (input("Enter your Vignere string: "))
vkey = input("What is your Vignere key?")


vciphertext = vignerecipher(vplaintext,vkey)
print ("Vignere Ciphertext is: ",vciphertext)

