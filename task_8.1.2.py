class Pump:
    def __init__(self,pump_type,pumped_water,pressure):
        self.pump_type = pump_type
        self.pumped_water = pumped_water
        self.pressure = pressure

    def choice_pump_type(self,pump_type):
        if pump_type == 'цнс':
            return f"Тип насоса {self.pump_type} подходит"
        else:
            return f"Такой тип {self.pump_type} нам не подходит"

    def choice_pumped_water(self,pumped_water):
        if pumped_water == 240:
            return f"Закачка {self.pumped_water} подходит"
        else:
            return f"Закачка {self.pumped_water} не подходит"

    def choice_pressure(self,pressure):
        if pressure == 240:
            return f"Давление {self.pressure} подходит"
        else:
            return f"Давление {self.pressure} не подходит"

pump_type = input('Введите тип насоса').strip().lower()
pumped_water = int(input("Введите закачку насоса"))
pressure = int(input("Введите давление насоса"))

pump = Pump(pump_type,pumped_water,pressure)
pump_type_choice = pump.choice_pump_type(pump_type)
pump_pumped_water = pump.choice_pumped_water(pumped_water)
pump_pressure_choice = pump.choice_pressure(pressure)


pump_inform = {f'Тип насоса {pump_type}': pump_type_choice ,f'Закачка воды {pumped_water}' : pump_pumped_water,f'Давление воды {pressure}' : pump_pressure_choice}
with open(f"{pump_type}.txt" ,'w',encoding = 'utf-8') as file:
    file.write(str(pump_inform))
