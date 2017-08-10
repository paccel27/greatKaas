# print ("Caeser Cipher")
# plaintext = input ("Enter your message: ")
key = int(input ("What key value?"))
if key > 26:
	key,x = divmod(key,26)
if key <-26:
	key,x = divmod(key,26)
ciphertext = ''

def caesarcipher(plaintext):
	ciphertext = ''
	for letter in plaintext:
		cletter = ord(letter) + key
		if ord(letter) in range	(65,92):
			if cletter in range(65,92):
				ciphertext += chr(cletter)
			elif cletter > 92:
				ciphertext += chr(cletter-26)
			elif cletter < 65:
				ciphertext += chr(cletter+26)
		# elif ord(letter) in range	(97,121):
		# 	if cletter in range(97,121):
		# 		ciphertext += chr(cletter)
		# 	elif cletter > 121:
		# 		ciphertext += chr(cletter-26)
		# 	elif cletter < 97:
		# 		ciphertext += chr(cletter+26)
		
	print (ciphertext)
	return ciphertext

caesarcipher('zzzzzzabcdefghijklmnopqrstuvwxyz')
print (ciphertext)
# caesarcipher('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
# print (ciphertext)
# caesarcipher('.?!')
# print (ciphertext)



# for letter in plaintext:
# 	if ord(plaintext) in range 