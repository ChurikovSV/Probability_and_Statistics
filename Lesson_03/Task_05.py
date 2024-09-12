# Устройство состоит из трех деталей. Для первой детали вероятность выйти из строя в первый месяц
# равна 0.1, для второй - 0.2, для третьей - 0.25.
# акова вероятность того, что в первый месяц выйдут из строя:
# а). все детали
# б). только две детали
# в). хотя бы одна деталь
# г). от одной до двух деталей?

# Вероятности выхода из строя каждой детали
P_fail_1 = 0.1
P_fail_2 = 0.2
P_fail_3 = 0.25

# Вероятности не выйти из строя
P_not_fail_1 = 1 - P_fail_1
P_not_fail_2 = 1 - P_fail_2
P_not_fail_3 = 1 - P_fail_3

P_all_fail = P_fail_1 * P_fail_2 * P_fail_3
print('Вероятность выхода из строя всех деталей составляет - ', P_all_fail)

P_two_fail = (P_fail_1 * P_fail_2 * P_not_fail_3) + (P_fail_1 * P_not_fail_2 * P_fail_3) + (P_not_fail_1 * P_fail_2 * P_fail_3)
print('Вероятность выхода из строя только двух деталей составляет - ', P_two_fail)

P_at_least_one_fail = 1 - (P_not_fail_1 * P_not_fail_2 * P_not_fail_3)
print('Вероятность выхода из строя хотя бы одной детали составляет - ', P_at_least_one_fail)

P_one_or_two_fail = P_two_fail + (P_fail_1 * P_not_fail_2 * P_not_fail_3) + (P_not_fail_1 * P_fail_2 * P_not_fail_3) + (P_not_fail_1 * P_not_fail_2 * P_fail_3)
print('Вероятность выхода из строя от одной до двух деталей составляет - ', P_one_or_two_fail)