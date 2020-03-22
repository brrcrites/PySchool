#Choose one of the 8 planets
planet_input = input("Which planet do you want to calculate for? ")

#Choose either "Close" or "Far"
distance_input = input("Do you want to calculate the Close or Far disntace? ")

if distance_input != "Close":
    if distance_input != "Far":
        print("You must enter either Close or Far for your distance")
        exit()

#Check if the planet is Jupiter and set the necessary values
if planet_input == "Jupiter":
    mass2 = 1.8986*(10**27)
    if distance_input == "Close":
        distance = 741*(10**9)
    else:
        distance = 817*(10**9)
        
#Check if the planet is Saturn and set the necessary values
elif planet_input == "Saturn":
    mass2 = 5.6846*(10**26)
    if distance_input == "Close":
        distance = 1.35*(10**12)
    else:
        distance = 1.51*(10**12)
        
#Check if the planet is Neptune and set the necessary values
elif planet_input == "Neptune":
    mass2 = 10.243*(10**25)
    if distance_input == "Close":
        distance = 4.45*(10**12)
    else:
        distance = 4.55*(10**12)

#Check if the planet is Uranus and set the necessary values
elif planet_input == "Uranus":
    mass2 = 8.68*(10**25)
    if distance_input == "Close":
        distance = 2.75*(10**12)
    else:
        distance = 3*(10**12)
        
#Check if the planet is Earth and set the necessary values
elif planet_input == "Earth":
    mass2 = 5.9736*(10**24)
    if distance_input == "Close":
        distance = 147*(10**9)
    else:
        distance = 152*(10**9)
        
#Check if the planet is Venus and set the necessary values
elif planet_input == "Venus":
    mass2 = 4.8685*(10**24)
    if distance_input == "Close":
        distance = 107*(10**9)
    else:
        distance = 109*(10**9)
        
#Check if the planet is Mars and set the necessary values
elif planet_input == "Mars":
    mass2 = 6.4185*(10**23)
    if distance_input == "Close":
        distance = 205*(10**9)
    else:
        distance = 249*(10**9)
        
#Check if the planet is Mercury and set the necessary values
elif planet_input == "Mercury":
    mass2 = 3.3022*(10**23)
    if distance == "Close":
        distance = 46*(10**9)
    else:
        distance = 70*(10**9)

#If the planet is anything else, we should tell the user and end the program
else:
    print("You have not entered a valid planet")
    exit()


mass1 = 1.9891*(10**30)                         #The mass of the Sun       
gravity = 6.673*(10**(-11))                     #The gravitational constant
force = (gravity*mass1*mass2)/(distance**2)     #Calculate the force
print(force)                                    #Print the value found
