car_star = 'START'
car_stop = 'STOP'
exit_game = 'EXIT'

started_car = False
stopped_car = False

while True:
    use_input = input('>').upper()
    if use_input == "HELP":
        print("""
           Start - Start The Car
           Stop - Stop The Car
           Exit - Exit The Game
           """)
    elif use_input == car_star:
        if started_car:
            print("Car is already started...")
        else:
            started_car = True
            print("Car Started...")
    elif use_input == car_stop:
        if stopped_car:
            print("Car is already stopped...")
        else:
            stopped_car: True
            print("Car is stopped...")
    elif use_input == exit_game:
        break
    else:
        print("Sorry, I don't understand that...")


print("Thant you.See you aging...")


