tickets = int(input ("Введите количество билетов:"))
num_tickets = [i for i in range(1, tickets+1)]
age = [int(input ("Введите возраст каждого посетителя:")) for i in range(tickets)]
sum = 0
for a, b in zip(num_tickets,age):
    if b < 18:
        sum += 0
    if 18 <= b < 25:
        sum += 990
    if b >= 25:
        sum += 1390
print ("Cумма:", sum)
if tickets >= 3:
    print("Итого к оплате (скидка 10 % при регистрации более 3 человек):", sum-(sum*10/100))
else:
    print("Итого к оплате:", sum)