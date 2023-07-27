def summa(number1, number2):
    return number1 + number2

def minus(number1, number2):
    return number1 - number2

def error ():
    print('Ошибка. Введите правильное действие')
    main()

def main ():
    f = True
    print('Приветствуем в нашем калькуляторе')
    print('Выберите действие которое хотите совершить')
    print('Сложить два числа: +')
    print('Найти разность чисел: -')
    choice = input(':')
    number1 = float(input('Введите первое число: '))
    number2 = float(input('Введите второе число: '))
    if choice == '+':
        answer  = summa(number1, number2)
    elif choice == '-':
        answer = minus(number1, number2)
    else :
        error()
        f = False
    if f :
        print(number1 , choice, number2, '=', answer)
        print('Ответ:', answer)

main()