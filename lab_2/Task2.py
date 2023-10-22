money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен
ost = money_capital + salary - spend
count = 1
while ost >= 0:
    spend *= (increase + 1)
    ost += - spend + salary
    if ost < 0:
        break
    count += 1
print("Количество месяцев, которое можно протянуть без долгов:", count)
