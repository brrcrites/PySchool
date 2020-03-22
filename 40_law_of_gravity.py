#We need to set initial values to our flags otherwise the while loop won't know
#what to do (and we'll get a runtime error)
planet_incorrect = True
distance_incorrect = True

#We want this condition to be or, because we want it to restart if either the
#planet or the distance is incorrect
while planet_incorrect or distance_incorrect:

    #Choose one of the 8 planets
    planet = input("Which planet do you want to calculate for? ")

    #Choose either "Close" or "Far"
    distance = input("Do you want to calculate the Close or Far disntace? ")

    #It is still easier to check if the distance is correct at the beginning
    #since it will mean less lines of code than doing it in the if/else statements
    if distance == "Close" or distance == "Far":
        distance_incorrect = False
    else:
        #We should print(an error message letting the user know what they did wrong
        print("You have entered an invalid distance, please try again")
        distance_incorrect = True

    #Check if the planet is Jupiter and set the necessary values
    if planet == "Jupiter":
        planet_incorrect = False
        m_2 = 1.8986*(10**27)
        if distance == "Close" :
            d = 741*(10**9)
        elif distance == "Far":
            d = 817*(10**9)
            
    #Check if the planet is Saturn and set the necessary values
    elif planet == "Saturn":
        planet_incorrect = False
        m_2 = 5.6846*(10**26)
        if distance == "Close" :
            d = 1.35*(10**12)
        elif distance == "Far":
            d = 1.51*(10**12)
            
    #Check if the planet is Neptune and set the necessary values
    elif planet == "Neptune":
        planet_incorrect = False
        m_2 = 10.243*(10**25)
        if distance == "Close" :
            d = 4.45*(10**12)
        elif distance == "Far":
            d = 4.55*(10**12)

    #Check if the planet is Uranus and set the necessary values
    elif planet == "Uranus":
        planet_incorrect = False
        m_2 = 8.68*(10**25)
        if distance == "Close" :
            d = 2.75*(10**12)
        elif distance == "Far":
            d = 3*(10**12)
            
    #Check if the planet is Earth and set the necessary values
    elif planet == "Earth":
        planet_incorrect = False
        m_2 = 5.9736*(10**24)
        if distance == "Close" :
            d = 147*(10**9)
        elif distance == "Far":
            d = 152*(10**9)
            
    #Check if the planet is Venus and set the necessary values
    elif planet == "Venus":
        planet_incorrect = False
        m_2 = 4.8685*(10**24)
        if distance == "Close" :
            d = 107*(10**9)
        elif distance == "Far":
            d = 109*(10**9)
            
    #Check if the planet is Mars and set the necessary values
    elif planet == "Mars" :
        planet_incorrect = False
        m_2 = 6.4185*(10**23)
        if distance == "Close" :
            d = 205*(10**9)
        elif distance == "Far":
            d = 249*(10**9)
            
    #Check if the planet is Mercury and set the necessary values
    elif planet == "Mercury":
        planet_incorrect = False
        m_2 = 3.3022*(10**23)
        if distance == "Close" :
            d = 46*(10**9)
        elif distance == "Far":
            d = 70*(10**9)

    #If none of the others were correct, then we have an incorrect input, so we should
    #update planet_incorrect to reflect that
    else:
        print("You have entered an invalid planet, please try again")
        planet_incorrect = True


m_1 = 1.9891*(10**30)   #The mass of the Sun       
G = 6.673*(10**(-11))   #The gravitational constant
F = (G*m_1*m_2)/(d**2)  #Calculate the force
print(F)                #Print the value found
