current_time = 0        #Set the current time to 0 (because we're just starting)
e = 2.72                #Eulers constant

decay_constant = float(input("decay constant: "))
start_amount = float(input("amount of radioactive material: "))
stop_time = int(input("amount of time to decay: "))

while stop_time < 0 or stop_time > 1000:
    stop_time = int(input("Please enter an amount of time to decay between 1 and 1000: "))

while current_time < stop_time:
    amount = start_amount * (e ** (-1 * decay_constant * current_time))
    print(amount)
    current_time = current_time + 1
