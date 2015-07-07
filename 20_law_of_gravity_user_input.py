#Get the mass of the two planets, and the distance between the planets
mass1 = raw_input("Enter first planet's mass: ")
mass2 = raw_input("Enter second planet's mass: ")
distance = raw_input("Enter the distance between the planets: ")

#Convert the user input into integer numbers
m1 = int(mass1)
m2 = int(mass2)
d = int(distance)

#Set the gravity constant, solve the equation, and print
G = 6.673*(10**(-11))
F = (G*m1*m2)/d**2
print F