weight = int(input('Enter your weight :'))
input = input('Enter (K)k or (L)bs :')

if input == 'k' or input == 'K':
    result = 2.20462 * weight
elif input == 'l' or input == 'L':
    result = 0.453592 * weight

print(f"Your weight is : {result}")

#using upper care mathod of string
if input.upper() == 'K':
    result = 2.20462 * weight
elif input.upper() == 'L':
    result = 0.453592 * weight

print(f"Your convert weight is : {result} ")