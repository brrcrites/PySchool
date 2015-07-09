#Start with a flag set to true, since we need to ask the user at
#least once for an input (otherwise the program wont run)
ask_for_skin = True

while ask_for_skin:
    skin = raw_input("What type of skin does the animal have? ")
    
    #We have a user input, but we haven't validated it yet. Since
    #we already have an if/elif/else block that catches invalid input
    #we can simply assume the input is correct here, and if we arrive
    #at the else statement (which we know means invalid input was
    #given) then we will change the flag to ask for input again (since
    #we now know that the input given was invalid
    
    ask_for_skin = False
    
    if skin == "fur":
        print "mammal"
    elif skin == "feathers":
        print "feathers"
    elif skin == "scales":
        print "fish"
    elif skin == "skin":
        dry_or_moist = raw_input("Is the skin moist or dry? ")
        if dry_or_moist == "dry":
            print "reptile"
        elif dry_or_moist == "moist":
            print "amphibian"
        else:
            print "skin must be either dry or moist"
            
    #Since this else catches all invalid input, if we get here then we
    #know the input was invalid and we need to ask for input again
    
    else:
        print "not a proper skin type, please try again"
        ask_for_skin = True