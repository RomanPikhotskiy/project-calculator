def summa(number1, number2):
    return number1 + number2

def minus(number1, number2):
    return number1 - number2

def main ():
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

    print(number1 , choice, number2, '=', answer)
    print('Ответ:', answer)

main()

print('ads')