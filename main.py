name_of_company = "CAR SHOP on console"
print("%s" % name_of_company)
location = "Moscow, Russia"
print("Место расположения: %s " % location)

print("Доступный ассортимент")
d = dict(car1="BMW - 5 000 000 руб", car2="Porshe - 3 500 000 руб")
d["car3"] = "Toyota - 1 500 000 руб"
d["car4"] = "Aston Martin - 17 490 000 руб"
d["car5"] = "Range Rover - 4 000 000 руб"
d["car6"] = "Jaguar - 6 400 000 руб"
eval('''print("Всего машин в салоне: ", len(d))''')
eval('''print("Авто-словрь", d.values())''')


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
