current_time = 0        #Set the current time to 0 (because we're just starting)
e = 2.72                #Eulers constant

decay_constant = float(input("decay constant: "))
start_amount = float(input("amount of radioactive material: "))

while current_time < 10:
    amount = start_amount * (e ** (-1 * decay_constant * current_time))
    print(amount)
    current_time = current_time + 1
