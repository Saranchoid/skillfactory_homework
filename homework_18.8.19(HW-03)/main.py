number_of_tickets = int(input('введите количество билетов: '))
totalsum = 0
for i in range(number_of_tickets):
    age = int(input(f"введите возраст для билета №{i+1}: "))
    if 18 <= age <= 25:
        totalsum += 990
    elif age > 25:
        totalsum += 1390

if number_of_tickets >= 3:
    totalsum = totalsum * 0.9
print("сумма к оплате: ", totalsum)
