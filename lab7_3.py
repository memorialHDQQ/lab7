import turtle as tr
import math

tr.setup(1000, 800)
tr.title("Задание 3: График ряда Тейлора (Вариант 30)")
tr.speed(0)

# ОДЗ
tr.setworldcoordinates(-1, -3, 7, 4)

# Сами оси
tr.penup()
tr.goto(-1, 0);
tr.pendown();
tr.goto(7, 0)
tr.write(" X", font=("Arial", 14, "bold"))
tr.penup()
tr.goto(0, -3);
tr.pendown();
tr.goto(0, 4)
tr.write(" Y", font=("Arial", 14, "bold"))

# Функция Тейлора
def taylor_ln(x, eps=0.001):
    if x <= -0.5 or x > 6.5:
        return None

    y = math.log(7)
    an = 2 * (x - 3) / 7
    y += an
    n = 2
    while abs(an) >= eps:
        k = - (2 * (x - 3) / 7) * (n - 1) / n
        an *= k
        y += an
        n += 1
    return y

tr.penup()
tr.color("green")
tr.width(3)

x = -0.4
while x <= 6.5:
    y = taylor_ln(x)
    if y is not None:
        tr.goto(x, y)
        tr.pendown()
    x += 0.05

tr.penup()
tr.done()