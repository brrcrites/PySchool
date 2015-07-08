skin = raw_input("What type of skin does the animal have? ")

if skin == "fur":
    print "mammal"
elif skin == "feathers":
    print "feathers"
elif skin == "scales":
    print "fish"
elif skin == "skin":
    wetness = raw_input("Is the skin moist or dry? ")
    if wetness == "dry":
        print "reptile"
    elif wetness == "moist":
        print "amphibian"
    else:
        print "skin must be either dry or moist"
else:
    print "not a proper skin type"