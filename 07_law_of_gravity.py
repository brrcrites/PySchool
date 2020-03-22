#Get the mass of the two planets, and the distance between the planets
mass1_input = input("Enter first planet's mass: ")
mass2_input = input("Enter second planet's mass: ")
distance_input = input("Enter the distance between the planets: ")

#Convert the user input into integer numbers
mass1 = int(mass1_input)
mass2 = int(mass2_input)
distance = int(distance_input)

#Set the gravity constant, solve the equation, and print
gravity = 6.673*(10**(-11))
force = (gravity*mass1*mass2)/distance**2
print(force)
