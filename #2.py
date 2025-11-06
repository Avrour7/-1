#2.1
import math

#a
x = float(input("Введите x для y = 17x^2 - 6x + 13: "))
y1 = 17*x**2 - 6*x + 13
print("y =", y1)

#b
a = float(input("Введите a для y = 3a^2 + 5a - 21: "))
y2 = 3*a**2 + 5*a - 21
print("y =", y2)

#2.2
import math

a = float(input("Введите a: "))
y = (a**2 + 10) / math.sqrt(a**2 + 1)
print("y =", y)

#2.3
import math

#a
a = float(input("Введите a для (a): "))
val_a = (2*a + math.sin(abs(3*a))) / 3.56
if val_a < 0:
    print("Подкоренное выражение отрицательно, результат комплексный")
else:
    res_a = math.sqrt(val_a)
    print("a) =", res_a)
    
#b
x = float(input("Введите x для (b): "))
den = abs(5*x)
if den == 0:
    print("b) делене на ноль (|5x|=0)")
else:
    res_b = math.sin((3.2 + math.sqrt(1 + x)) / den)
    print("b) =", res_b)
    
#2.4
a = float(input("Длина стороны квадрата a: "))
P = 4 * a
print("Периметр квадрата =", P)

#2.5
R = float(input("Введите радиус окружности R: "))
D = 2 * R
print("Диаметр =", D)
