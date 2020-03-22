ask_for_distance = True
while ask_for_distance:
    distance_input = input("What distance? ")
    if distance_input == "Close" or distance_input == "Far":
        ask_for_distance = False
    else:
        ask_for_distance = True
