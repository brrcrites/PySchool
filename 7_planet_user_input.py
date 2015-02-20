#Choose one of the 8 planets
planet = raw_input("Which planet do you want to calculate for? ")

#Choose either "Close" or "Far"
distance = raw_input("Do you want to calculate the Close or Far disntace? ")

#Check if the planet is Jupiter and set the necessary values
if(planet == "Jupiter"):
    m_2 = 1.8986*(10**27)
    if(distance == "Close"):
        d = 741*(10**9)
    else:
        d = 817*(10**9)
        
#Check if the planet is Saturn and set the necessary values
elif(planet == "Saturn"):
    m_2 = 5.6846*(10**26)
    if(distance == "Close"):
        d = 1.35*(10**12)
    else:
        d = 1.51*(10**12)
        
#Check if the planet is Neptune and set the necessary values
elif(planet == "Neptune"):
    m_2 = 10.243*(10**25)
    if(distance == "Close"):
        d = 4.45*(10**12)
    else:
        d = 4.55*(10**12)

#Check if the planet is Uranus and set the necessary values
elif(planet == "Uranus"):
    m_2 = 8.68*(10**25)
    if(distance == "Close"):
        d = 2.75*(10**12)
    else:
        d = 3*(10**12)
        
#Check if the planet is Earth and set the necessary values
elif(planet == "Earth"):
    m_2 = 5.9736*(10**24)
    if(distance == "Close"):
        d = 147*(10**9)
    else:
        d = 152*(10**9)
        
#Check if the planet is Venus and set the necessary values
elif(planet == "Venus"):
    m_2 = 4.8685*(10**24)
    if(distance == "Close"):
        d = 107*(10**9)
    else:
        d = 109*(10**9)
        
#Check if the planet is Mars and set the necessary values
elif(planet == "Mars"):
    m_2 = 6.4185*(10**23)
    if(distance == "Close"):
        d = 205*(10**9)
    else:
        d = 249*(10**9)
        
#Check if the planet is Mercury and set the necessary values
else:
    m_2 = 3.3022*(10**23)
    if(distance == "Close"):
        d = 46*(10**9)
    else:
        d = 70*(10**9)
        
#What would happen if there was a spelling mistake when we
#assigned planet, or if we chose Pluto (which is not a planet)?

m_1 = 1.9891*(10**30)   #The mass of the Sun       
G = 6.673*(10**(-11))   #The gravitational constant
F = (G*m_1*m_2)/(d**2)  #Calculate the force
print F                 #Print the value found
