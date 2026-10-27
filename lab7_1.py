import turtle as tr
import math

# Границы масштабирования
x_min = float(input("Введите X нач (например, -10): "))
x_max = float(input("Введите X кон (например, 10): "))

# Настройка окна
tr.setup(1000, 800)
tr.title("Задание 1: График функции (Вариант 30)")
tr.speed(0)

# Автоматический масштаб
tr.setworldcoordinates(x_min - 1, -5, x_max + 1, 5)

#  Рисуем оси с подписями
tr.penup()
tr.goto(x_min - 1, 0)  # Ось X
tr.pendown()
tr.goto(x_max + 1, 0)
tr.write(" X", font=("Arial", 14, "bold"))  # Подпись оси X

tr.penup()
tr.goto(0, -4)  # Ось Y
tr.pendown()
tr.goto(0, 4)
tr.write(" Y", font=("Arial", 14, "bold"))  # Подпись оси Y

# --- Рисуем график ---
tr.penup()
tr.color("red")
tr.width(3)

x = x_min
step = 0.05  # Мелкий шаг для плавности
while x <= x_max:
    if x < -6:
        if 4 - (x + 8) ** 2 < 0:
            y = None  # Если корень отрицательный
        else:
            y = -math.sqrt(4 - (x + 8) ** 2)
    elif x < -4:
        y = 2
    elif x < 2:
        y = -(2 / 3) * x - (2 / 3)
    else:
        y = x - 4

    # Если Y вычислился
    if y is not None:
        tr.goto(x, y)
        tr.pendown()
    else:
        tr.penup()  # Если функции нет

    x += step

tr.penup()
tr.done()