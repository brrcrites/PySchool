t = 0       #Set time to 0
e = 2.72    #Eulers constant

decay_constant = float(raw_input("decay constant: "))
amount = float(raw_input("amount of radioactive material: "))
time = int(raw_input("amount of time to decay: "))

while t < time:
    amount = amount * (e ** (-1 * decay_constant * t))
    print amount
    t = t + 1