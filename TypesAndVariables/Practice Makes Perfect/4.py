###
# A program that prints your height both in cm and in feet and inches.
#

cm = int(input('Enter your height in cm: '));
feet = cm * 0.032808;
inches = cm * 0.3937;


print(f'I am {cm}cm tall, i.e. {feet} feet and {inches} inches tall.');