skin = input("What type of skin does the animal have? ")

if skin == "fur":
    print("mammal")
elif skin == "feathers":
    print("bird")
elif skin == "scales":
    print("fish")
elif skin == "skin":
    dry_or_moist = raw_input("Is the skin moist or dry? ")
    if dry_or_moist == "dry":
        print("reptile")
    elif dry_or_moist == "moist":
        print("amphibian")
    else:
        print("skin must be either dry or moist")
else:
    print("not a proper skin type")
