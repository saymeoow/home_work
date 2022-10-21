class PossitiveError(Exception):
    def __init__(self, text):
        self.text = text


while True:
    sign = input("Choose sign (+,-,*,/): ")
    if sign == 'stop':
        break
    try:
        if sign in ('+', '-', '*', '/'):
            first_number = float(input("first_number is "))
            second_number = float(input("second_number is "))
            if sign == '+':
                print(first_number + second_number)
            elif sign == '-':
                print(first_number - second_number)
            elif sign == '*':
                print(first_number * second_number)
            elif sign == '/':
                try:
                    if second_number != 0:
                        print(first_number / second_number)
                    else:
                        raise PossitiveError('Value must be possitive')
                except:
                    print(PossitiveError('Value must be possitive'))
        else:
            print(f'You put the wrong sign')
    except:
        print(f"You put the wrong value")
