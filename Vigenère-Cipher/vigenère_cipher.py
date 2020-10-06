# Python code to implement Vigenere Cipher 	
import string

ASCII = list(string.ascii_letters)

def generate_key(string, key):
	i = 0
	while len(key) < len(string):
		key = key + key[i]
		i = (i + 1)%len(key)
	return key 

def cipher_text(string, key): 
	key = generate_key(string, key)
	text = [] 
	for i in range(len(string)): 
		if string[i] in ASCII:	# rotate only the alphabets
			x = (ASCII.index(string[i]) + ASCII.index(key[i])) % len(ASCII) 
			text.append(ASCII[x])
		else:
			text.append(string[i])

	return("" . join(text))

def decipher_text(string, key):
	key = generate_key(string, key)
	text = [] 
	for i in range(len(string)): 
		if string[i] in ASCII:	# rotate only the alphabets
			x = (ASCII.index(string[i]) - ASCII.index(key[i])) % len(ASCII) 
			text.append(ASCII[x])
		else:
			text.append(string[i])

	return("" . join(text))

# Driver code 
if __name__ == "__main__": 
	text1 = "Encrypt Me"
	key = "test"

	cipherd_text = cipher_text(text1, key)

	text2 = cipherd_text

	deciphered_text = decipher_text(text2, key)

	print(cipherd_text)
	print(deciphered_text)
