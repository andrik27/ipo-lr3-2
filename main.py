x = float(input("Введите первое число: "))
y = float(input("Введите второе число: "))
if x == y:
    print("Чсисла равны.")
else:
    print("Первое число больше второго.") if x > y else print("Второе число больше первого.")