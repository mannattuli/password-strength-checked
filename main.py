score = 0 
password = input('Enter your password: ')
length = len(password)

for i in range (length):
	#Special characters
	if password[i] == '@' or password[i] == '$' or password[i] == '%' or password[i] == '&':
		score += 1
		break

for i in range (length):
	#Capital letters
	if password[i].isupper():
		score += 1
		break

for i in range (length):
	#Lowercase letters
	if password[i].islower():
		score += 1
		break

for i in range (length):
	#Numbers
	if password[i].isdigit():
		score += 1
		break

if length > 8:
	score += 1

print(str(score) + '/5')