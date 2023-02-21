
name = "What is your name? "
askName = input(name)

age = "What is your age? "
askAge = input(age)
a = int(askAge)

hi = "Hi, " + askName + "!"

currentYear = 2023
year = currentYear - a 
yearBorn = " You were born in either " + str(year) + " or " + str(year-1) + "!"

print(hi + yearBorn)

