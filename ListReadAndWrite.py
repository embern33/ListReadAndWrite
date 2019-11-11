from random import randint
import random

print("Hello, this program currently adds to a list and prints a random item from that list.")

samples = []
placeholder = "Y"
print("What would you like to add (If you want to get a random number, input RN)")

while placeholder.upper() == "RN":
    add_name = str(input("> "))

    if add_name.upper() == "N":
        break

    else:
        samples.append(add_name)
        print(samples)

ran_num = int(input(f"How many random items do you want? there are currently {len(samples)} things in the list > "))

loop_counter = 0

while loop_counter < ran_num:
    print(random.choice(samples))
    loop_counter += 1

