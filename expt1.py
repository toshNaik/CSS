import random
import numpy as np

print('Select cryptography method:\n1. Substitution\n2. ROT13\n3. Transpose\n4. Double Transposition\n5. Vernam Cipher')
method = int(input())

print('Enter plain text: ')
text = str(input())


if method == 1:
	shift = int(input("Enter position shift: "))
	encrypted = ""
	decrypted = ""
	for i in text:
		if ord(i) >= 65 and ord(i) <= 90:
			encrypted += chr((ord(i) + shift - 65) % 26 + 65)
		elif ord(i) >= 97 and ord(i) <= 122:
			encrypted += chr((ord(i) + shift - 97) % 26 + 97)
	for i in encrypted:
		if ord(i) >= 65 and ord(i) <= 90:
			decrypted += chr((ord(i) - shift - 65) % 26 + 65)
		elif ord(i) >= 97 and ord(i) <= 122:
			decrypted += chr((ord(i) - shift - 97) % 26 + 97)
	
	print("Encrypted Message: " + encrypted)
	print("Decrypted Message: " + decrypted)

elif method == 2:
	shift = 13
	encrypted = ""
	decrypted = ""
	for i in text:
		if ord(i) >= 65 and ord(i) <= 90:
			encrypted += chr((ord(i) + shift - 65) % 26 + 65)
		elif ord(i) >= 97 and ord(i) <= 122:
			encrypted += chr((ord(i) + shift - 97) % 26 + 97)
	for i in encrypted:
		if ord(i) >= 65 and ord(i) <= 90:
			decrypted += chr((ord(i) - shift - 65) % 26 + 65)
		elif ord(i) >= 97 and ord(i) <= 122:
			decrypted += chr((ord(i) - shift - 97) % 26 + 97)
	
	print("Encrypted Message: " + encrypted)
	print("Decrypted Message: " + decrypted)

elif method == 3:
	encrypted = ""
	decrypted = ""
	key = input("Enter key: ")
	length_key = len(key)
	order = ""
	
	for i in range(1, length_key+1):
		order += str(i)
	str1 = key + order + text
	if len(text)%length_key != 0:
		for i in range(length_key - len(text)%length_key):
			str1 += chr(random.randint(97, 122))
	
	grid = np.array(list(str1)).reshape(len(str1)//length_key, length_key)
	# Encryption
	grid_sort = grid[:, grid[0].argsort()]
	for j in range(length_key):
		for i in range(2, len(grid_sort)):
			encrypted += grid_sort[i][j]
		encrypted += " "
	
	# Decryption
	gresort = grid_sort[:, grid_sort[1].argsort()]
	for i in range(2, len(gresort)):
		for j in range(length_key):
			decrypted+=gresort[i][j]
	
	print("Encrypted Message: " + encrypted)
	print("Decrypted Message: " + decrypted[:len(text)])


elif method == 4:
	encrypted = ""
	decrypted = ""
	key = input("Enter key: ")
	length_key = len(key)
	order = ""
	
	for i in range(1, length_key+1):
		order += str(i)
	
	str1 = key + order + text
	
	if len(text)%length_key != 0:
		for i in range(length_key - len(text)%length_key):
			str1 += chr(random.randint(97, 122))

	grid = np.array(list(str1)).reshape(len(str1)//length_key, length_key)

	
	# First Transpose
	grid = grid[:, grid[0].argsort()]
	for j in range(length_key):
		for i in range(2, len(grid)):
			encrypted += grid[i][j]
	
	str1 = key + order + encrypted
	grid2 = np.array(list(str1)).reshape(len(str1)//length_key, length_key)
	grid2 = grid2[:, grid2[0].argsort()]
	encrypted2 = ""
	
	# Second Transpose
	for j in range(length_key):
		for i in range(2, len(grid2)):
			encrypted2 += grid2[i][j]
		encrypted2 += " "
	
	
	# Decryption 1
	grid_reverse = grid2[:, grid2[1].argsort()]
	for i in range(2, len(grid_reverse)):
		for j in range(length_key):
			decrypted += grid_reverse[i][j]

	str1 = ""
	for i in range(2):
		for j in range(length_key):
			str1 += grid2[i][j]
			
	grid = np.array(list(decrypted)).reshape(length_key, len(decrypted)//length_key)
	grid = grid.T
	for i in range(len(grid)):
		for j in range(length_key):
			str1 += grid[i][j]
		
	grid = np.array(list(str1)).reshape(len(str1)//length_key, length_key)
	grid_reverse2 = grid[:, grid[1].argsort()]
	
	# Decryption 2
	final_decrypted = ""
	for i in range(2, len(grid_reverse2)):
		for j in range(length_key):
			final_decrypted+=grid_reverse2[i][j]
	
	print("Encrypted Message: " + encrypted2)
	print("Decrypted Message: " + final_decrypted[:len(text)])

elif method == 5:
	key = ""
	while len(key) != len(text):
		key = input("Enter key same length as text: ")

	encrypted = ""
	decrypted = ""

	for i in range(len(text)):
		encrypted += chr(ord(text[i]) ^ ord(key[i]))

	for i in range(len(text)):
		decrypted += chr(ord(encrypted[i]) ^ ord(key[i]))
		
	print("Encrypted Message: " + encrypted)
	print("Decrypted Message: " + decrypted)