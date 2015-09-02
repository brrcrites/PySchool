secret_number = 65
user_input = 0
minimum = 1
maximum = 100
while user_input != secret_number:
	user_input = int(raw_input("Pick a number between 1 and 100: "))
	if user_input < minimum or user_input > maximum:
		print "Your guess must be between ", minimum, " and ", maximum
	elif user_input == secret_number:
		print "Correct!"
	elif user_input < secret_number:
		print "Too low, guess again"
		minimum = user_input
	#Should this be an else instead or an elif?
	elif user_input > secret_number:
		print "Too high, guess again"
		maximum = user_input