# Question 1
# To prompt the user for the temperature in Celsius and convert the input value to Fahrenheit temperature.
# Asks the user for temperature in Celsius


def one():
    temperature = int(input("Enter the temperature in Celsius: "))

# Formula for converting the Celsius to Fahrenheit
    fahrenheit = int(round((temperature - 32) * 5 / 9))

# Prints out the converted value
    print("The temperature in Fahrenheit is: ", fahrenheit)
