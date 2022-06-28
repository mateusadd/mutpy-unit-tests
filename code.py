def checkNumbersInputted(number1, number2):
    if(number1 > number2):
        return True
    else:
        return False

def getNumberInputted():
    number1 = input('Forneça um número: ')
    number2 = input('Forneça outro número: ')

    validation = checkNumbersInputted(number1, number2)

    print(validation)