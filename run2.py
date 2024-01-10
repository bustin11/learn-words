import random
import sys


catalogue = {}
with open("dominic_system.txt", "r") as f:
    for line in f:
        x = line.strip().split(",")
        if len(x) == 2 and x[1] != '':
            catalogue[int(x[0])] = x[1]

while True:
    heads = (random.randint(0,2) == 1)
    num, name = random.choice(list(catalogue.items()))
    if heads:
        response = input(f"{num} ").lower().strip()
        if response == name.strip().lower():
            print("Correct!")
        else:
            print(f"Wrong! It's {name}")
    else:
        response = int(input(f"{name} "))
        if response == num:
            print("Correct!")
        else:
            print(f"Wrong! It's {num}")
