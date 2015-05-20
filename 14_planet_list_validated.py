#Our three new dictionaries for the mass of planets and their distances
mass = {"Jupiter": 1.8986*(10**27), "Saturn": 5.6846*(10**26), "Neptune": 10.243*(10**25), "Uranus": 8.68*(10**25), "Earth": 5.9736*(10**24), "Venus": 4.8685*(10**24), "Mars": 6.4185*(10**23), "Mercury": 3.3022*(10**23)}
close_distance = {"Jupiter": 741*(10**9), "Saturn": 1.35*(10**12), "Neptune": 4.45*(10**12), "Uranus": 2.75*(10**12), "Earth": 147*(10**9), "Venus": 107*(10**9), "Mars": 205*(10**9), "Mercury": 46*(10**9)}
far_distance = {"Jupiter": 817*(10**9), "Saturn": 1.51*(10**12), "Neptune": 4.55*(10**12), "Uranus": 3*(10**12), "Earth": 152*(10**9), "Venus": 109*(10**9), "Mars": 249*(10**9), "Mercury": 70*(10**9)}

#Our new list with all the planets that our program has values for
planet_list = ["Jupiter", "Saturn", "Neptune", "Uranus", "Earth", "Venus", "Mars", "Mercury"]

#Choose one of the 8 planets
planet = raw_input("Which planet do you want to calculate for? ")

#Choose either "Close" or "Far"
distance = raw_input("Do you want to calculate the Close or Far disntace? ")

#Check if the planet is a key in the mass dictionary
if planet in planet_list:
    #Notice that since we've already validated the name of the planet
    #we can use the varible as the key for the dictionary instead of
    #hand typing in the string
    m_2 = mass[planet]
    if distance == "Close":
        d = close_distance[planet]
    elif distance == "Far":
        d = far_distance[planet]
    #Note that we have moved the check for "Close" and "Far" into this
    #block, since we now only have one if/else block we can check here
    #without having to re-write the check for each planet
    else:
        print "Please choose either \"Close\" or \"Far\" for your distance"
        exit()

#If the planet is anything else, we should tell the user and end the program
else:
    print "You have not entered a valid planet"
    exit()


m_1 = 1.9891*(10**30)   #The mass of the Sun       
G = 6.673*(10**(-11))   #The gravitational constant
F = (G*m_1*m_2)/(d**2)  #Calculate the force
print F                 #Print the value found
