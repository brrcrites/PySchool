#Our three new dictionaries for the mass of planets and their distances
mass = {"Jupiter": 1.8986*(10**27), "Saturn": 5.6846*(10**26), "Neptune": 10.243*(10**25), "Uranus": 8.68*(10**25), "Earth": 5.9736*(10**24), "Venus": 4.8685*(10**24), "Mars": 6.4185*(10**23), "Mercury": 3.3022*(10**23)}
close_distance = {"Jupiter": 741*(10**9), "Saturn": 1.35*(10**12), "Neptune": 4.45*(10**12), "Uranus": 2.75*(10**12), "Earth": 147*(10**9), "Venus": 107*(10**9), "Mars": 205*(10**9), "Mercury": 46*(10**9)}
far_distance = {"Jupiter": 817*(10**9), "Saturn": 1.51*(10**12), "Neptune": 4.55*(10**12), "Uranus": 3*(10**12), "Earth": 152*(10**9), "Venus": 109*(10**9), "Mars": 249*(10**9), "Mercury": 70*(10**9)}

planet_incorrect = True
distance_incorrect = True

while planet_incorrect or distance_incorrect:
    
    planet = raw_input("Which planet do you want to calculate for? ")
    
    distance = raw_input("Do you want to calculate the Close or Far disntace? ")
    
    if distance == "Close" or distance == "Far":
        distance_incorrect = False
    else:
        print "You have entered an invalid distance, please try again"
        distance_incorrect = True
    
    #Check if the planet is Jupiter and set the necessary values
    if(planet == "Jupiter"):
        planet_incorrect = False
        m_2 = mass[planet]
        if(distance == "Close"):
            d = close_distance[planet]
        else:
            d = far_distance[planet]
            
    #Check if the planet is Saturn and set the necessary values
    elif(planet == "Saturn"):
        planet_incorrect = False 
        m_2 = mass[planet]
        if(distance == "Close"):
            d = close_distance[planet]
        else:
            d = far_distance[planet]
            
    #Check if the planet is Neptune and set the necessary values
    elif(planet == "Neptune"):
        planet_incorrect = False 
        m_2 = mass[planet]
        if(distance == "Close"):
            d = close_distance[planet]
        else:
            d = far_distance[planet]
    
    #Check if the planet is Uranus and set the necessary values
    elif(planet == "Uranus"):
        planet_incorrect = False
        m_2 = mass[planet]
        if(distance == "Close"):
            d = close_distance[planet]
        else:
            d = far_distance[planet]
            
    #Check if the planet is Earth and set the necessary values
    elif(planet == "Earth"):
        planet_incorrect = False 
        m_2 = mass[planet]
        if(distance == "Close"):
            d = close_distance[planet]
        else:
            d = far_distance[planet]
            
    #Check if the planet is Venus and set the necessary values
    elif(planet == "Venus"):
        planet_incorrect = False 
        m_2 = mass[planet]
        if(distance == "Close"):
            d = close_distance[planet]
        else:
            d = far_distance[planet]
            
    #Check if the planet is Mars and set the necessary values
    elif(planet == "Mars"):
        planet_incorrect = False 
        m_2 = mass[planet]
        if(distance == "Close"):
            d = close_distance[planet]
        else:
            d = far_distance[planet]
            
    #Check if the planet is Mercury and set the necessary values
    elif planet == "Mercury":
        planet_incorrect = False 
        m_2 = mass[planet]
        if(distance == "Close"):
            d = close_distance[planet]
        else:
            d = far_distance[planet]
    
    #If the planet is anything else, we should tell the user and end the program
    else:
        print "You have not entered a valid planet"
        planet_incorrect = True

m_1 = 1.9891*(10**30)   #The mass of the Sun       
G = 6.673*(10**(-11))   #The gravitational constant
F = (G*m_1*m_2)/(d**2)  #Calculate the force
print F                 #Print the value found
