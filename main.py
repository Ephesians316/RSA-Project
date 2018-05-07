def RSAprogram():
	print("What would you like to do?")
	print("1) Encrypt message")
	print("2) Decrypt message")
	print("3)Exit")
	choice = input("Enter an option: ")
	while input != choice:
		if choice == "1":
			e = int(input("Enter your 'e' variable: "))
			n = int(input("Enter your 'n' variable: "))
			encryption(e, n)
		if choice == "2":
			d = int(input("Enter your 'd' variable: "))
			n = int(input("Enter your 'n' variable: "))
			decryption(d, n)
		if choice == '3':
			break
		else:
			RSAprogram()
			break


def encryption(e, n):
	encrypted_message = ""
	message = input("Input Message: ")
	for x in message:
		numerize = ord(x)
		encrypt = pow(numerize, e, n)
		denumerize = chr(encrypt)
		encrypted_message += denumerize
	print(encrypted_message)
	print("")
	RSAprogram()


def decryption(d, n):
	decrypted_message = ""
	emessage = input("Input encrypted message: ")
	for t in emessage:
		numerize = ord(t)
		decrypt = pow(numerize, d, n)
		denumerize = chr(decrypt)
		decrypted_message += denumerize
	print(decrypted_message)
	print("")
	RSAprogram()
  

