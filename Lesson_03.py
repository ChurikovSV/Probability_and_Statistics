import math

# 1. Даны значения зарплат из выборки выпускников: 100, 80, 75, 77, 89, 33, 45, 25, 65, 17, 30, 24, 57, 55, 70, 75, 65, 84, 90, 150.
# Посчитать (желательно без использования статистических методов наподобие std, var, mean) среднее арифметическое, среднее квадратичное отклонение, смещенную и несмещенную оценки дисперсий для данной выборки.

# Данные
data_salary = [100, 80, 75, 77, 89, 33, 45, 25, 65, 17, 30, 24, 57, 55, 70, 75, 65, 84, 90, 150]
n = len(data_salary)

average = sum(data_salary) / len(data_salary)
print('Среднее арифметическое', average)
sum_squared_deviations = 0
for salary in data_salary:
    sum_squared_deviations += (salary - average) ** 2
print('Вычисление суммы квадратов отклонений от среднего', sum_squared_deviations)
print('Смещенная дисперсия', sum_squared_deviations / n)
print('Среднее квадратичное отклонение', math.sqrt(sum_squared_deviations / n))
print('Несмещенная дисперсия ', sum_squared_deviations / (n - 1))

