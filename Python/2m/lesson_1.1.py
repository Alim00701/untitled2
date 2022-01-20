class Car:
    def __init__(self, brand, model, engine, fuel, color, passengers_quantity, prise):
        if isinstance(brand, str):
            self.brand = brand
        else:
            raise ValueError('Brand should be string0')
        if isinstance(model, str):
            self.model = model
        else:
            raise ValueError('Model should be string')
        if isinstance(engine, str):
            self.engine = engine
        else:
            raise ValueError('Engine should be string')
        if isinstance(fuel, float):
            self.fuel = fuel
        else:
            raise ValueError('Fuel should be float')
        if isinstance(color, str):
            self.color = color
        else:
            raise ValueError('Color should be string')
        if isinstance(passengers_quantity, int):
            self.pass_q = passengers_quantity
        else:
            raise ValueError('Passenger should be integer')
        if isinstance(price, int):
            self.prise = prise
        else:
            raise ValueError('Prise should be integer')

    def tunning(self.prise_t):
        total = self.prise + prise_t
        return f'Total prise of Car: {total}\n'

        #self.brand = brand
        #self.model = model
        #self.engine = engine
        #self.fuel = fuel
        #self.color = color
        #self.pass_q = passengers_quantity

    def __str__(self):
        return f'Brand: {self.brand}\n' \ 
               f'Model: {self.model}\n' \
               f'Engine: {self.engine}\n' \ 
               f'Fuel: {self.fuel}\n' \
               f'Color: {self.color}\n' \
               f'Passenger Quantity: {self.pass_q}\n'\
               f'Prise: {self.prise}$\n'


car_1 = Car(brand='Mersedes', model='S-class 500', engine='Germany bomb',
            fuel=5.0, color='black', passengers_quantity=5, prise=500000)
car_2 = Car(brand='Lexus', model='570', engine='Katana',
            fuel=5.7, color='silver', passengers_quantity=8, prise=500000)
print(car_1)
print(car_1.tunning(654))
print(car_2)
print(car_2.tunning(1963))





        #brand = 'Mersedes'
        #model = 'C-class 340'
        #engine = 'Germany'
        #fuel = 3.5
        #color = 'grey'