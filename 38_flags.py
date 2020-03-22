distance_correct = False
while not distance_correct:
    distance_input = input("What distance? ")
    if distance_input == "Close" or distance_input == "Far":
        distance_correct = True
    else:
        distance_correct = False
