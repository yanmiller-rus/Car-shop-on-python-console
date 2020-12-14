d = dict(car1="BMW", car2="Porshe")
d["car3"] = "Toyota"
d["car4"] = "Aston Martin"
d["car5"] = "Range Rover"
d["car6"] = "Jaguar"
eval('''print("Всего машин в магазине: ", len(d))''')
eval('''print("Авто-словрь", d.values())''')

# d2 = {a: a ** 2 for a in range(1, 10)}
# d2.update(d)
# print("Словарь №2", d2)

eval('''print("Цена BMW: 5 000 000")''')
eval('''print("Цена Porsche: 3 500 000")''')
eval('''print("Цена Toyota: 1 500 000")''')
eval('''print("Цена Aston Martin: 17 490 000")''')
eval('''print("Цена Range Rover: 4 000 000")''')
eval('''print("Цена Jaguar: 6 400 000 ")''')

eval('''print("Ваша сумма денег: ")''')
your_balance = int(input())
eval('''print("Ваша сумма денег: %s " % your_balance)''')

if your_balance >= 2500000:
    eval('''print("Все хорошо, вам хватает средств для продолжения покупки")''')
else:
    eval('''print("У вас не хватает средств!")''')
    eval('''print("Вы не можете продолжить покупку!")''')
    eval('''print("Пожалуйста, покиньте консольный центр")''')

eval('''print("Введите цену машины")''')
price_of_car = int(input())
eval('''print("Цена выбранного автомобиля: %s " % price_of_car)''')

eval('''print("Укажите ваше имя")''')
name = str(input())
eval('''print("Ваше имя: %s " % name)''')


rest_money = your_balance - price_of_car
eval('''print("Покупка успешна завершена :) . Ждем вас в следующий раз")''')
eval('''print("Ваш текущий баланс: %s " % rest_money)''')
