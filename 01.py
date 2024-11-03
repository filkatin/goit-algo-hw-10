from pulp import LpMaximize, LpProblem, LpVariable

model = LpProblem("Maximize_Production", LpMaximize)

x1 = LpVariable("Лимонад", lowBound=0, cat="Integer")
x2 = LpVariable("Фруктовий сік", lowBound=0, cat="Integer")

# Цільова функція
model += x1 + x2, "Загальна продукція"

# Обмеження ресурсів
model += 2 * x1 + 1 * x2 <= 100, "Обмеження вода"
model += 1 * x1 <= 50, "Обмеження цукор"
model += 1 * x1 <= 30, "Обмеження лимонний сік"
model += 2 * x2 <= 40, "Обмеження фруктове пюре"

model.solve()

# Результати
print("Оптимальний план:")
print(f"Лимонад, од: {x1.varValue}")
print(f"Фруктовий сік, од: {x2.varValue}")
