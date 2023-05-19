# Break Statement
"""
for i in "DevOps":
    print(i)
    if i == "O":
        print("I Found My Data!")
        break
print("Out of loop")


# Continue Statement

for i in "DevOps":
    if i == "O":
        print("I Found My Data!")
        continue
    print(f"Value of i is {i}")
print("Out of loop")
"""

# Using function

import random

VACCINES = ["Moderna", "Pfizer", "Sputnik V", "Covaxin", "AstraZeneca", "CoronaVac"]

random.shuffle(VACCINES)
print("\n",VACCINES)

# LUCKY = random.choice(VACCINES)
# # print("\n",LUCKY)

# for vac in VACCINES:
#     print(f"TESTING VACCINE: {vac}")
#     if vac == LUCKY:
#         print("###############################################")
#         print(f"{LUCKY} Vaccine, Test Successful")
#         print("###############################################")
#         print()
#         break # continue user for other test
#     print('xxxxxxxxxxxxxxxxxx')
#     print("Test Failed")
#     print('xxxxxxxxxxxxxxxxxx')
#     print()

