#Our three new dictionaries for the mass of planets and their distances
mass = {0: 1.8986*(10**27), 1: 5.6846*(10**26), 2: 10.243*(10**25), 3: 8.68*(10**25), 4: 5.9736*(10**24), 5: 4.8685*(10**24), 6: 6.4185*(10**23), 7: 3.3022*(10**23)}
close_distance = {0: 741*(10**9), 1: 1.35*(10**12), 2: 4.45*(10**12), 3: 2.75*(10**12), 4: 147*(10**9), 5: 107*(10**9), 6: 205*(10**9), 7: 46*(10**9)}
far_distance = {0: 817*(10**9), 1: 1.51*(10**12), 2: 4.55*(10**12), 3: 3*(10**12), 4: 152*(10**9), 5: 109*(10**9), 6: 249*(10**9), 7: 70*(10**9)}
planets = {0: "Jupiter", 1: "Saturn", 2: "Neptune", 3: "Uranus", 4: "Earth", 5: "Venus", 6: "Mars", 7: "Mercury"}

m_1 = 1.9891*(10**30)           #The mass of the Sun  

index = 0
while index < 8:

    m_2 = mass[index]           #The mass of the current plan

    print("Force when " + planets[index] + " is close to the Sun")

    d = close_distance[index]   #The distance when the planet is close
    G = 6.673*(10**(-11))       #The gravitational constant
    F = (G*m_1*m_2)/(d**2)      #Calculate the force
    print(F)                    #Print the value found

    print("Force when " + planets[index] + " is far from the Sun")

    d = far_distance[index]     #The distance when the planet is far
    G = 6.673*(10**(-11))       #The gravitational constant
    F = (G*m_1*m_2)/(d**2)      #Calculate the force
    print(F)                    #Print the value found

    index = index + 1           #Increment the index
