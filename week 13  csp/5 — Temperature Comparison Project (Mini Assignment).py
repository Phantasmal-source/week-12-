# Objective:
# Apply comparison and logical operators to a real-world problem.

# Scenario:
# Write a program that:

# Asks the user for today’s temperature.
temperature = int(input("What's the fahrenheit temperature bro?: "))
# Prints whether it’s cold, warm, or hot using comparison operators.
if temperature < 75 and temperature > -10:
    print("its cool!")
else:
    if temperature >= 75 and temperature <= 90:
        print("it's warm")
    else:
        if temperature > 90 and temperature < 110:
            print("Too hot!")
        else:
            print("Extreme temperature warning!")
# If the temperature is out of range (below -10 or above 110), display “Extreme temperature warning!”

# Starter Code:

