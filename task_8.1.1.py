class Vehicle:
    def __init__(self,name,mileage):
        self.name = name
        self.mileage = mileage
    def get_vehicle_type(self, vehicles):
        if vehicles == 2:
            return f"Это мотоцикл марки {self.name}"
        elif vehicles == 3:
            return f"Это трицикл марки {self.name}"
        elif vehicles == 4:
            return f"Это автомобиль марки {self.name}"
        elif vehicles > 4 or vehicles < 2:
            return f"Я не знаю таких ТС!!!"

    def get_vehicle_advice(self,mileage):
        if mileage < 50000:
            return f"Неплохо {self.name} можно брать."
        elif 50001 < mileage < 100000:
            return f"{self.name} надо внимательно проверить"
        elif 100001 < mileage < 150000:
            return f"{self.name} надо провести полную диагностику."
        elif mileage > 150000:
            return f"{self.name} лучше не покупать"

name = input("Введите марку ТС ")
mileage = int(input("Введите пробег "))
vehicles = int(input("Введите количество колес "))
vehicles__ = Vehicle(name,mileage)
type_vehicles = vehicles__.get_vehicle_type(vehicles)
advice = vehicles__.get_vehicle_advice(mileage)

for i in range(5):
    vehicles_inform = {'Марка_и_тип': type_vehicles, 'Стоит_ли_брать': advice}
    with open(f"{name}.txt" ,'w',encoding = 'utf-8') as file:
        file.write(str(vehicles_inform))

#Хотелось бы узнать почему цилкы не работают... из за with open?







