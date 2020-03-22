secret_number = 65
user_input = 0
while user_input != secret_number:
	user_input = int(input("Pick a number between 1 and 100: "))
	if user_input < 1 or user_input > 100:
		print("Your guess must be between 1 and 100")
	elif user_input == secret_number:
		print("Correct!")
	elif user_input < secret_number:
		print("Too low, guess again")
	#Should this be an else instead or an elif?
	elif user_input > secret_number:
		print("Too high, guess again")
