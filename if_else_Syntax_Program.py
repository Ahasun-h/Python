is_hot = False
is_cool = True

if is_hot:
    print("Drink Water")

print("Enjoy The Day")

if is_hot:
    print("Drink Water")
elif is_cool:
    print("Drink Hot Tea")
else:
    print("It,s Lovely Day,Thank You")

print("Enjoy The Day")



Price = 100000
have_a_good_price = True

if have_a_good_price :
    down_payment = 0.1 * Price
else:
    down_payment = 0.2 * Price

print(f"Down Payment $:{down_payment}")

has_high_income = True
has_good_cradit = True

if has_high_income and has_good_cradit:  # AND:Both must Be True
    print("Eligible for loan")


get_loan_before = False
has_criminal_racode = True
if has_high_income or get_loan_before:    # OR: One must be True
    print("Eligible for loan")

if has_high_income and not has_criminal_racode:
    print("Eligible for loan")
else:
    print("Not eligible for loan")


name = input('Enter your name :')
name_langth = (len(name))
print(name_langth)

if name_langth <= 3:
    print("Name must be at least 3 character")
elif name_langth >= 50:
    print("Name must be maximum least 50 character")
else:
    print("Good Name")


if len(name)<= 3 or len(name) >= 50:
    print("Your name must be at least 3 character or maximum 50 character ")
else:
    print("good name")

