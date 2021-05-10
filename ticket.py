import random
import PySimpleGUI as Sg


if __name__ := "__main__":
    main_num = []
    bonus_num = []

    def main():
        # Ask user if they would like a quick pick. If not they then self pick their numbers.
        # If user doesn't enter y/n then loop is restarted.
        while True:
            try:
                print('Would you like a quick pick?')
                types = input('Y/N: ').lower()
                if types == 'y':
                    quick_pick()
                    quick_bonus()
                    return main_num
                if types == 'n':
                    self_pick()
                    self_bonus()
                    return main_num
                else:
                    print('Invalid Selection')
            except ValueError:
                continue

    def quick_pick():
        # Function for generating quick pick selection.
        main_count = 0
        while main_count < 6:
            numbers = random.randint(1, 70)
            if numbers not in main_num:
                main_num.append(numbers)
                main_count += 1
                main_num.sort()


    def self_pick():
        # Self pick function. Ask users to select 6 numbers 1-70.
        # Loop will restart if user selects number out of range or duplicate.
        range_check = 0
        print('Please pick 6 numbers, 1-70, no duplicates.')
        while len(main_num) < 6:
            number = int(input('please enter a number: '))
            if number not in main_num:
                main_num.append(number)
            else:
                main_num.clear()
                print('No Duplicates, please re-enter your numbers.')
            for x in main_num:
                if x > 70:
                    range_check += 1
                    if range_check > 0:
                        main_num.clear()
                        print('Invalid Entry, please re-enter your numbers.')
                else:
                    main_num.sort()

    def quick_bonus():
        # Quick pick bonus number.
        number = random.randint(1, 26)
        bonus_num.append(number)

    def self_bonus():
        # User selection for bonus number.
        # Loop will restart if user enters number out of range.
        range_check = 0
        while len(bonus_num) < 1:
            number = int(input("please enter a bonus number from 1-26: "))
            bonus_num.append(number)
            for x in bonus_num:
                if x > 26:
                    range_check += 1
                    if range_check > 0:
                        bonus_num.clear()
                        print('Invalid Entry, re-enter bonus number')


class Ticket:
    # Class that generates ticket ID and calls numbers from functions for output.
    def __init__(self):
        self.num = main()
        self.bonus = bonus_num
        self.id = str(random.getrandbits(64))

    def __str__(self):

        return 'Ticket ID #: ' + self.id + '\nNumbers: ' + str(self.num) + '\nBonus: ' + str(self.bonus)


tkt = Ticket()
print(tkt)


def view():
    layout = [[Sg.Text('Numbers:')],
              [Sg.Text(tkt.num)],
              [Sg.Text('Bonus:')],
              [Sg.Text(tkt.bonus)],
              [Sg.Button("OK")]]

    window = Sg.Window('Ticket ID:'+tkt.id, layout, margins=(120, 1))

    while True:
        event, values = window.read()
        if event == "OK" or event == Sg.WIN_CLOSED:
            break
        window.close()


view()
