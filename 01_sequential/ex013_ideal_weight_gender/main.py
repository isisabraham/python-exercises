height = float(input('Enter your height in meters: '))
sex = input('Enter your sex (M/F): ').strip().upper()
weight = float(input('Enter your current weight in kg: '))

if sex == 'M':
    ideal_weight = (72.7 * height) - 58
elif sex == 'F':
    ideal_weight = (62.1 * height) - 44.7
else:
    ideal_weight = None

if ideal_weight:
    print(f'Your ideal weight is {ideal_weight:.2f} kg')
    if weight == ideal_weight:
        print('You are at the ideal weight')
    elif weight > ideal_weight:
        print('You are above the ideal weight')
    else:
        print('You are below the ideal weight')
else:
    print('Invalid sex input')
