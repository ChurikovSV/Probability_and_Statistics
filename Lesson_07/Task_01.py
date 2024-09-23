# Даны две независимые выборки. Не соблюдается условие нормальности
# x1 380,420, 290
# y1 140,360,200,900
# Сделайте вывод по результатам, полученным с помощью функции


# Тест Манна-Уитни (U-test)
import numpy as np
from scipy.stats import mannwhitneyu

# Функция для выполнения теста Манна-Уитни
def mann_whitney_test(sample1, sample2):
    # Выполнение U-теста
    stat, p_value = mannwhitneyu(sample1, sample2, alternative='two-sided')
    # Вывод результатов
    print("Статистика U-теста:", stat)
    print("P-значение:", p_value)
    if p_value < 0.05:
        print("Вывод: Есть статистически значимые различия между выборками.")
    else:
        print("Вывод: Статистически значимых различий между выборками нет.")

# Ваши выборки
x1 = np.array([380, 420, 290])
y1 = np.array([140, 360, 200, 900])

# Вызов функции
mann_whitney_test(x1, y1)