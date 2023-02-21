name = "What is your name? "
askName = input(name)

age = "What is your age? "
askAge = input(age)
old = int(askAge)  # Convert askAge to an integer

hi = "Hi, " + str(askName) + "!"

currentYear = 2023
year = currentYear - old  # Use askA instead of age
yearBorn = " You were born in either " + str(year) + " or " + str(year-1) + "!"

print(hi + yearBorn)
