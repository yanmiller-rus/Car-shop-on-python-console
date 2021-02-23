def info():
    name_of_company = "CAR SHOP ON CONSOLE"
    the_location = "Moscow, Russia"
    print("Название компании:", name_of_company)
    print("Местоположение:", the_location)


def get_available_cars():
    print("Доступный ассортимент")
    cars = {
        'Toyota': '1 500 000 руб', 'Aston Martin': '17 490 000 руб', 'Range Rover': '4 000 000 руб', 'Jaguar': '6 400 000 руб'
           }
    print("Всего машин в салоне: ", len(cars))
    print("Авто-словрь")
    for key, values in cars.items():
        print(key, values)


def buy_car():
    print("Ваша сумма денег: ")
    your_balance = int(input())
    print("Ваша сумма денег: %s " % your_balance)

    if your_balance >= 1500000:
        print("Все хорошо, вам хватает средств для продолжения покупки")
        print("Введите цену машины")
        price_of_car = int(input())
        print("Цена выбранного автомобиля: %s " % price_of_car)

        print("Укажите ваше имя")
        name = str(input())
        print("Ваше имя: %s " % name)

        rest_money = your_balance - price_of_car
        print("Покупка успешна завершена :) . Ждем вас в следующий раз")
        print("Ваш текущий баланс: %s " % rest_money)

    else:
        print("У вас не хватает средств!")
        print("Вы не можете продолжить покупку!")
        print("Пожалуйста, покиньте консольный центр!")


info()
print("===================================")
get_available_cars()
buy_car()