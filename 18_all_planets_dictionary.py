#Our three new dictionaries for the mass of planets and their distances
mass = {"Jupiter": 1.8986*(10**27), "Saturn": 5.6846*(10**26), "Neptune": 10.243*(10**25), "Uranus": 8.68*(10**25), "Earth": 5.9736*(10**24), "Venus": 4.8685*(10**24), "Mars": 6.4185*(10**23), "Mercury": 3.3022*(10**23)}
close_distance = {"Jupiter": 741*(10**9), "Saturn": 1.35*(10**12), "Neptune": 4.45*(10**12), "Uranus": 2.75*(10**12), "Earth": 147*(10**9), "Venus": 107*(10**9), "Mars": 205*(10**9), "Mercury": 46*(10**9)}
far_distance = {"Jupiter": 817*(10**9), "Saturn": 1.51*(10**12), "Neptune": 4.55*(10**12), "Uranus": 3*(10**12), "Earth": 152*(10**9), "Venus": 109*(10**9), "Mars": 249*(10**9), "Mercury": 70*(10**9)}

#Check if the planet is a key in the mass dictionary
for planet in mass:

    m_2 = mass[planet]

    d = close_distance[planet]
    print "The force between " + planet + " and the Sun at it's closest distance is..."
    m_1 = 1.9891*(10**30)   #The mass of the Sun       
    G = 6.673*(10**(-11))   #The gravitational constant
    F = (G*m_1*m_2)/(d**2)  #Calculate the force
    print F                 #Print the value found
    
    d = far_distance[planet]
    print "The force between " + planet + " and the Sun at it's furthest distances is..."
    m_1 = 1.9891*(10**30)   #The mass of the Sun       
    G = 6.673*(10**(-11))   #The gravitational constant
    F = (G*m_1*m_2)/(d**2)  #Calculate the force
    print F                 #Print the value found