money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен

count_mounth = 0

while True:
    need_money = spend - salary
    if need_money > money_capital:
        break

    count_mounth += 1
    money_capital -= need_money
    spend *= 1 + increase

print("Количество месяцев, которое можно протянуть без долгов:", count_mounth)
