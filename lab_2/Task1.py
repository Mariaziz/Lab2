salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен
need_money = spend - salary
# TODO Рассчитайте подушку безопасности, чтобы протянуть 10 месяцев без долгов
for _ in range(months - 1):
    spend *= (1 + increase)
    need_money += spend - salary
need_money = round(need_money)
print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", need_money)
