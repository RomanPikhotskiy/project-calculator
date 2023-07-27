def summa(number1, number2):
    return number1 + number2

def main ():
    print('Приветствуем в нашем калькуляторе')
    print('Выберите действие которое хотите совершить')
    print('Сложить два числа: +')
    print('Найти разность чисел: -')
    choice = input()
    if choice == '+':
        summa()
    elif choice == '-':
        minus()
    else :
        error()

main()