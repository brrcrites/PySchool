distance_correct = False
while not distance_correct:
    distance_input = raw_input("What distance? ")
    if distance_input == "Close" or distance_input == "Far":
        distance_correct = True
    else:
        distance_correct = False