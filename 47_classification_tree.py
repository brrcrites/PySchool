choices = ["fur", "feathers", "scales", "skin"]

print("Please choose from the following list:")
i = 0
while i < len(choices):
    print(choices[i])
    i = i + 1

ask_for_skin = True

while ask_for_skin:
    skin = input("What type of skin does the animal have? ")
    
    ask_for_skin = False
    
    if skin == "fur":
        print("mammal")
    elif skin == "feathers":
        print("bird")
    elif skin == "scales":
        print("fish")
    elif skin == "skin":
        dry_or_moist = input("Is the skin moist or dry? ")
        if dry_or_moist == "dry":
            print("reptile")
        elif dry_or_moist == "moist":
            print("amphibian")
        else:
            print("skin must be either dry or moist")
    
    else:
        print("not a proper skin type, please try again")
        ask_for_skin = True
