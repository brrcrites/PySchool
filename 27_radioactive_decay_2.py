current_time = 0        #Set the current time to 0 (because we're just starting)
e = 2.72                #Eulers constant

decay_constant = float(raw_input("decay constant: "))
start_amount = float(raw_input("amount of radioactive material: "))
stop_time = int(raw_input("amount of time to decay: "))

while current_time < stop_time:
    amount = start_amount * (e ** (-1 * decay_constant * current_time))
    print amount
    current_time = current_time + 1