# GUESSING GAME 

print(f'\n')
print(' >>> START <<< ')

# Importing required functions
from sys import argv
from random import randint

# Defining guessings
lower_number = int(argv[1])
upper_number = int(argv[2])

answer = randint(lower_number, upper_number)

# Generates a function that only accepts integers between the given answers
def guess_number():
	while True:
		try:
			print(f'>>> Please guess a number between {lower_number} and {upper_number}: ', end ='')
			guess = int(input())
		except ValueError:
			print('>>> That is not a number, ', end ='')
			continue
		if guess < lower_number or guess > upper_number:
			print(f'>>> That number is outside the range ', end ='')
		else:
			return guess
			break

# Initial guess
guess = guess_number()

# Are you correct? - verification part
count = 0 
while True:
	if guess != answer:
		print('>>> You are unlucky today... That is not the right answer, try again: ')
		print(f'\n')
		count = count + 1
		guess = guess_number()
	if count == 4:
			r = answer - int((upper_number - lower_number)/2)
			new_lower_number =  randint(r, answer)
			new_upper_number = new_lower_number + int((upper_number - lower_number)/2)
			print(f'>>> Clue: The answer is between {new_lower_number} and {new_upper_number}')
	    else:
		    print('>>> WELL DONE FRIEND! You got it!')
		break

print(' >>> THE END <<< ')
print(f'\n')
