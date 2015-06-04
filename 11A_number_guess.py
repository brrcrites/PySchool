secret_number = 5
user_input = 0
while user_input != secret_number:
	user_input = int(raw_input("Pick a number between 1 and 10: "))
	if user_input == secret_number:
		print "Correct!"
	else:
		print "WRONG! Guess again"