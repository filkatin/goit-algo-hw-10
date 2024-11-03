import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as spi

# Визначення функції та межі інтегрування
def f(x):
    return x ** 2

a = 0  # Нижня межа
b = 2  # Верхня межа

# Налаштування кількості точок для методу Монте-Карло
num_points = 10000

# Генерація випадкових точок
x_rand = np.random.uniform(a, b, num_points)
y_rand = np.random.uniform(0, f(b), num_points)

# Обчислення кількості точок під кривою
under_curve = y_rand < f(x_rand)
monte_carlo_area = (b - a) * f(b) * np.sum(under_curve) / num_points

# Обчислення інтегралу аналітично за допомогою функції quad
result, error = spi.quad(f, a, b)

# Створення діапазону значень для x
x = np.linspace(-0.5, 2.5, 400)
y = f(x)

# Створення графіка
fig, ax = plt.subplots()

# Малювання функції
ax.plot(x, y, 'r', linewidth=2)

# Заповнення області під кривою
ix = np.linspace(a, b)
iy = f(ix)
ax.fill_between(ix, iy, color='gray', alpha=0.3)

# Випадкові точки
ax.scatter(x_rand, y_rand, color="blue", s=1, alpha=0.1, label="Точки Монте-Карло")
ax.scatter(x_rand[under_curve], y_rand[under_curve], color="red", s=1, alpha=0.1, label="Під кривою")

# Налаштування графіка
ax.set_xlim([x[0], x[-1]])
ax.set_ylim([0, max(y) + 0.1])
ax.set_xlabel('x')
ax.set_ylabel('f(x)')

# Додавання меж інтегрування та назви графіка
ax.axvline(x=a, color='gray', linestyle='--')
ax.axvline(x=b, color='gray', linestyle='--')
ax.set_title('Графік інтегрування f(x) = x^2 від ' + str(a) + ' до ' + str(b))
plt.legend()
plt.grid()
plt.show()

# Виведення результатів
print(f"Метод Монте-Карло: {monte_carlo_area}")
print(f"Аналітичний результат (quad): {result} з помилкою {error}")
