classification = {"fur": "mammal", "feathers": "bird", "scales": "fish", "dry skin": "reptile", "moist skin": "amphibian"}

skin = ""

while skin not in classification:
    skin = raw_input("What type of skin does the animal have? ")
    
print classification[skin]