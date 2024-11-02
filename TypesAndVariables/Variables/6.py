###
#Write a program that calculates the distance to the horizon from a height given in meters from the keyboard. Then, using the program, calculate the distance to the horizon in km when:
# i  You are standing on a beach, by the sea, on the water line (calculate the distance for your height in m). You have probably been to the seaside many times. Can you believe that the horizon is only a few kilometers away?
# ii You are looking out of a hotel window located by the sea, the window is at a height of 20 meters.

# 😎
import math;
print('Distance to the horizon in meters');

h = float(input('Height in meters: '));

d = 3.57 * math.sqrt(h);
print('Distance to the horizon:', round(d, 2),' kilometers');
