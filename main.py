class Shop:

    def __init__(self, name, balance):
        self.name = name
        print('Введите свой баланс')
        self.balance = int(input())

    @staticmethod
    def info():
        name_of_company = "MLR Technology"
        the_location = "Moscow, Russia"
        print("Название компании:", name_of_company)
        print("Местоположение:", the_location)

    @staticmethod
    def get_available_cars():
        print("Доступный ассортимент")
        cars = {
            'Toyota': '1 500 000 руб', 'Aston Martin': '17 490 000 руб', 'Range Rover': '4 000 000 руб',
            'Jaguar': '6 400 000 руб'
        }

        print("Всего моделей в салоне: ", len(cars))
        print("Авто-словрь")

        for key, values in cars.items():
            print(key, values)


    def check_my_balance(self):
        print(self.balance)


    def increase_balance(self):
        print('Введите сумму для пополнения счета')
        print('==================================')
        money = int(input())
        self.balance += money

    def take_off(self):
        print('Введите сумму для снятия')
        print('========================')
        taking = int(input())
        self.balance -= taking

    def buy_car(self):

        if self.balance >= 1500000:
            print("Все хорошо, вам хватает средств для продолжения покупки")
            print("Введите цену машины")
            price_of_car = int(input())
            print("Цена выбранного автомобиля: %s " % price_of_car)

            print("Укажите ваше имя")
            name = str(input())
            print("Ваше имя: %s " % name)

            rest_money = self.balance - price_of_car
            print("Покупка успешна завершена :) . Ждем вас в следующий раз")
            print("Ваш текущий баланс: %s " % rest_money)

        else:
            print("У вас не хватает средств!")
            print("Пожалуйста, пополните ваш счет для продолжения покупки")
            client_1.increase_balance()
            client_1.check_my_balance()
            if self.balance >= 1500000:
                client_1.buy_car()
            else:
                print('Средств все еще не достаточно для транзакции :(')
                print('Продолжайте пополнять счет хотя бы до 1 500 000')
                client_1.increase_balance()


client_1 = Shop('Yan Miller', balance='')
client_1.info()
print('==============================')
client_1.get_available_cars()
print('==============================')
print('Для покупки нажмите 1')
c = int(input())
if c == 1:
    client_1.buy_car()
else:
    print('Ошибка')
