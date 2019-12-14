name = input('What is your name ? ')
your_weight_in_pound = input(' Enter '+name+' weight in pound : ')
print(type(your_weight_in_pound))

your_weight_in_kg = int(your_weight_in_pound) / 0.453592

print(name,'weight in kg :',your_weight_in_kg,'Kg')
