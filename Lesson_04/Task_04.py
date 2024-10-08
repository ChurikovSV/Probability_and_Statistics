# Рост взрослого населения города X имеет нормальное распределение. Причем, средний рост равен 174 см,
# а среднее квадратичное отклонение равно 8 см.
# Какова вероятность того, что случайным образом выбранный взрослый человек имеет рост:
# а) больше 182 см
# б) больше 190 см
# в) от 166 см до 190 см
# г) от 166 см до 182 см
# д) от 158 см до 190 см
# е) не выше 150 см или не ниже 190 см
# ё) не выше 150 см или не ниже 198 см
# ж) ниже 166 см.

from scipy.stats import norm

mu = 174  # средний рост
sigma = 8  # среднее квадратичное отклонение

# а) больше 182 см = 15.86%
# z = 1
# z(1) = 0.84134
X = 182
z = (X - mu)/sigma
z_1 = 1 - 0.84134
print(z_1)

# б) больше 190 см = 2.27%
# z = 2
# z(2) = 0.97725
X = 190
z = (X - mu)/sigma
print(1 - 0.97725)

# в) от 166 см до 190 см = 81.85%
# z(-1) = 0.1587   z(2) = 0.97725
# z_v = 0.8185499999999999
X = 166
z = (X - mu)/sigma
z_v = 0.97725 - 0.1587
print(z_v)

# Решение с помощью встроенного метода
mu = 174
sigma = 8

# Вероятности
P_a = 1 - norm.cdf(182, mu, sigma) # 15.86%
P_b = 1 - norm.cdf(190, mu, sigma) # 2.27%
P_v = norm.cdf(190, mu, sigma) - norm.cdf(166, mu, sigma) # 81.85%
P_g = norm.cdf(182, mu, sigma) - norm.cdf(166, mu, sigma) # 68.26%
P_d = norm.cdf(190, mu, sigma) - norm.cdf(158, mu, sigma) # 95.44 %
P_e = norm.cdf(150, mu, sigma) + (1 - norm.cdf(190, mu, sigma)) # 2.41%
P_yo = norm.cdf(150, mu, sigma) + (1 - norm.cdf(198, mu, sigma)) # 0.27%
P_zh = norm.cdf(166, mu, sigma) # 15.86%

# Вывод результатов
print(P_a, P_b, P_v, P_g, P_d, P_e, P_yo, P_zh)