import turtle as tr
import random

# Настройка окна
tr.setup(800, 800)
tr.title("Задание 2: Метод Монте-Карло")
tr.speed(0)
tr.tracer(0)  # Отключение анимации
tr.setworldcoordinates(-3, -3, 5, 11)  # Область для нашей фигуры

# Ось
tr.penup()
tr.goto(-3, 0);
tr.pendown();
tr.goto(5, 0)
tr.write(" X", font=("Arial", 12, "bold"))
tr.penup()
tr.goto(0, -2);
tr.pendown();
tr.goto(0, 10)
tr.write(" Y", font=("Arial", 12, "bold"))

# Рамка
tr.penup()
tr.goto(-2, -1);
tr.pendown()
tr.color("red")
for _ in range(2):
    tr.forward(6);
    tr.left(90);
    tr.forward(10);
    tr.left(90)
tr.penup()


def check(x, y):
    if -1 <= x < 1:
        return (y >= 2 * x + 2) and (y <= x ** 3 - 4 * x ** 2 + x + 6)
    elif 1 <= x <= 4:
        return (y >= x ** 3 - 4 * x ** 2 + x + 6) and (y <= 2 * x + 2)
    return False

# Тут создаем 1000 точек
hits = 0
N = 10000
for _ in range(N):
    x = random.uniform(-2, 4)
    y = random.uniform(-1, 9)

    if check(x, y):
        tr.goto(x, y)
        tr.dot(3, "violet")
        hits += 1

tr.update()

# Площадь прямоугольника: ширина 6, высота 10 -> S = 60
S_rect = 60
S_mc = S_rect * (hits / N)  # Площадь по методу Монте-Карло

S_true = 21.08

# Погрешность
error = abs(S_mc - S_true) / S_true * 100

print(f"Попаданий: {hits}")
print(f"Площадь (Монте-Карло): {S_mc:.2f}")
print(f"Точная площадь: {S_true}")
print(f"Погрешность: {error:.2f}%")

tr.done()