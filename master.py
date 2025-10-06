print("Hello, Boris Igorevich")
a = int(input())
b = int(input())
op = input()
res = ''
if op == '+':
    res = a + b
elif op == '-':
    res = a-b 
elif op == '*':
    res = a * b
elif op == '/':
    if b != 0:
        res = a / b
    else: 
        print("Деление на 0")
else:
    print("Ошибка ввода")
print("Answer:", res)