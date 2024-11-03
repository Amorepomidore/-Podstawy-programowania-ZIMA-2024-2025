speed = int(input('Enter speed vehicle in km/h: '));
speed_limit = speed >= 40 and speed <= 140;
print(f'Speed is valid: {speed_limit}');