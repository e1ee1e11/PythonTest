from random import randint

print "Guess a number"
number = 0
correct_number = randint(1,100)

while number != correct_number:
	number = input()
	
	if number > correct_number:
		print "too big."
	elif number <correct_number:
		print "too small"
	else:
		print "BINGO! Congratulation!"
