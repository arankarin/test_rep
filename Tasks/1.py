class Glass:
    def __init__(self):
        #print(dir(self))
        self.capacity_volume = 500
        self.occupied_volume = 0


    def add_water(self, water):
        final_volume = self.occupied_volume - self.capacity_volume
        return final_volume


    def __str__(self): # Строка для вывода на экран (для пользователя)
        return f'Capacity: {self.capacity_volume}\nCurrent: {self.occupied_volume}'


    # def __repr__(self): # Строка для интерактивной оболочки (для программиста)
    #     return f'Glass({self.capacity_volume}, {self.occupied_volume})'

glass1 = Glass()
print(glass1)
glass1.add_water(400)
print(glass1)