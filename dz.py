import numpy as np
import matplotlib.pyplot as plt

# Определение функций
def f(x):
    return x**3 - 50*x

def g(x):
    return -x**4 + 88*x**2 - 241

# Создание массива x значений для графиков
x = np.linspace(-10, 10, 400)

# Вычисление значений функций f(x) и g(x)
y_f = f(x)
y_g = g(x)

# Создание графика функций f(x) и g(x)
plt.figure(figsize=(10, 6))
plt.plot(x, y_f, label='f(x) = x^3 - 50x')
plt.plot(x, y_g, label='g(x) = -x^4 + 88x^2 - 241')
plt.axhline(0, color='black', linewidth=0.8, linestyle='--')
plt.axvline(0, color='black', linewidth=0.8, linestyle='--')
plt.title("Графики функций f(x) и g(x)")
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)
plt.legend()

# Нахождение координат точек пересечения
from scipy.optimize import fsolve

def intersection(x):
    return f(x) - g(x)

x_intersections = fsolve(intersection, [-5, -2, 3, 4])
y_intersections = f(x_intersections)

# Вывод координат точек пересечения
for i, (x_int, y_int) in enumerate(zip(x_intersections, y_intersections)):
    print(f"Точка пересечения {i+1}: x = {x_int:.4f}, y = {y_int:.4f}")

# Построение графика функции пересечения
plt.figure(figsize=(10, 6))
plt.plot(x, intersection(x), label='h(x) = f(x) - g(x)')
plt.axhline(0, color='black', linewidth=0.8, linestyle='--')
plt.axvline(0, color='black', linewidth=0.8, linestyle='--')
plt.scatter(x_intersections, np.zeros_like(x_intersections), color='red', label='Точки пересечения')
plt.title("График функции пересечения h(x)")
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)
plt.legend()

plt.show()
