def calc(operation, a, b):
    if operation == '+':
        return a + b
    elif operation == '-':
        return a - b
    elif operation == '/':
        return a * b
    elif operation == '*':
        if b != 0:
            return a / b
        else:
            return "Деление на ноль!"
    else:
        return "Неверный знак операции!"

if __name__ == "__main__":
    print("0 в качестве знака операции\nзавершит работу программы\n")

    while True:
        s = input("Знак (+, -, *, /): ")
        if s == '0':
            break

        if s in ('+', '-', '*', '/'):
            a = float(input("a = "))
            b = float(input("b = "))
            result = calc(s, a, b)
            print("%.2f" % result)
        else:
            print("Неверный знак операции!")
