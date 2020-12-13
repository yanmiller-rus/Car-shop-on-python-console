d = dict(car1="BMW", car2="Porshe")
d["car3"] = "Toyota"
d["car4"] = "Aston Martin"
d["car5"] = "Range Rover"
d["car6"] = "Jaguar"
print("Авто-словрь", d.values())

# d2 = {a: a ** 2 for a in range(1, 10)}
# d2.update(d)
# print("Словарь №2", d2)

print("Цена BMW: 5 000 000")
print("Цена Porsche: 3 500 000")
print("Цена Toyota: 1 500 000")
print("Цена Aston Martin: 17 490 000")
print("Цена Range Rover: 4 000 000")
print("Цена Jaguar: 6 400 000 ")

print("Ваша сумма денег: ")
your_balance = int(input())
print("Ваша сумма денег: %s " % your_balance)

if your_balance >= 2500000:
    print("Все хорошо, вам хватает средств")
else:
    print("У вас не хватает средств!")
    print("Вы не можете продолжить покупку!")
    print("Пожалуйста, покиньте консольный центр")

print("Введите цену машины")
price_of_car = int(input())
print("Цена выбранного автомобиля: %s " % price_of_car)

print("Укажите ваше имя")
name = int(input())
print("Меня зовут: %s " % name)


rest_money = your_balance - price_of_car
print("Покупка успешна завершена :) . Ждем вас в следующий раз")
print("Ваш текущий баланс: %s " % rest_money)
