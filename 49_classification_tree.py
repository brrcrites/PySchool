classification_dictionary = {"fur": "mammal", "feathers": "bird", "scales": "fish", "dry skin": "reptile", "moist skin": "amphibian"}
ask_for_skin = True

while ask_for_skin:
    skin = input("What type of skin does the animal have? ")
    
    if skin in classification_dictionary:
        print(classification_dictionary[skin])
        ask_for_skin = False
    else:
        print("not a proper skin type, please try again")
        ask_for_skin = True
