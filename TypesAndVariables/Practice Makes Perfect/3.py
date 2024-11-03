###
# A program that reads temperature in degrees Celsius from the keyboard.
# Use comments to briefly describe the program's algorithm.
#

temperature = float(input('Enter temperature in degrees Celsius: '));
farenheit = temperature * 9 / 5 + 32;
kelvin = temperature + 273.15;
print(f'Temperature in degrees Celsius: {temperature} \n Farenheit: {farenheit} \n Kelvin: {kelvin}');