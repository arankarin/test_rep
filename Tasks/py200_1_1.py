# -*- coding: utf-8

# 
# Курс DEV-PY200. Объектно-ориентированное программирование на языке Python
# Тема 1.1 Основы ООП. Понятие класса, объекта. Создание экземпляра класса

# Лабораторная работа № 1.1 (4 ак.ч.)

# Слушатель (ФИО): Иванов И.И.

# ---------------------------------------------------------------------------------------------
# Понятие класса, объекта (стр. 1-22)

# 1. Создайте класс Glass с атрибутами capacity_volume и occupied_volume
#    Обязательно проверяйте типы (TypeError) и значения переменных (ValueError)

class Glass:
    """Класс Glass атрибутами capacity_volume и occupied_volume"""

    def __init__(self):
        """Инициализация класса атрибутов класса"""
        self.capacity_volume = 500  # объем емкости
        self.occupied_volume = 0  # занятый объем

    # 2. Создайте два и более объектов типа Glass
    #    Измените и добавьте в любой стакан любое кол-во воды (через атрибуты)
    #    Убедитесь, что у других объектов Glass атрибуты экземпляра класса не изменились.
    def add_water(self, water):
        self.occupied_volume = water
        return f'Занятый объем: {self.occupied_volume}'


glass1 = Glass()
glass2 = Glass()
glass1 = glass1.add_water(400)
glass2 = glass2.add_water(300)
print('первый стакан ' + glass1)
print('второй стакан ' + glass2)
print('----' * 10)


# 3. Создайте класс GlassDefaultArg (нужен только __init__) c аргументом occupied_volume
#    По умолчанию occupied_volume равен нулю. Создайте два объекта с 0 и 200
#    Обязательно проверяйте типы (TypeError) и значения переменных (ValueError)

class GlassDefaultArg:
    def __init__(self, occupied_volume=0):
        # raise TypeError
        self.occupied_volume = occupied_volume

    def __str__(self):
        return f'{self.occupied_volume}'


glass1 = GlassDefaultArg()
glass2 = GlassDefaultArg(200)
print(glass1)
print(glass2)
print('----q' * 10)


# 4. Создайте класс GlassDefaultListArg (нужен только __init__)
#    c аргументами capacity_volume, occupied_volume.
#    Пусть аргументом по умолчанию для __init__ occupied_volume = []. Будет список.
#    Попробуйте создать 3 объекта, которые изменяют occupied_volume.append(2) внутри __init__.
#    Создавайте объект GlassDefaultListArg только с одним аргументом capacity_volume.
#    Опишите результат.
#    Подсказка: можно ли использовать для аргументов по умолчанию изменяемые типы?
class GlassDefaultListArg:
    def __init__(self, capacity_volume, occupied_volume=[]):
        self.capacity_volume = capacity_volume
        self.occupied_volume = occupied_volume.append(2)

    def __str__(self):
        return f' dnkjhjkg{self.capacity_volume}'


glass1 = GlassDefaultArg(500)
print(glass1)

print('----' * 10)


# 5. Создайте класс GlassAddRemove, добавьте методы add_water, remove_water
#    Обязательно проверяйте типы (TypeError) и значения переменных (ValueError)
#    Вызовите методы add_water и remove.
#    Убедитесь, что методы правильно изменяют атрибут occupied_volume.


class GlassAddRemove:
    def __init__(self):

        self.capacity_volume = 500  # объем емкости
        self.occupied_volume = 0  # занятый объем

    def add_water(self, waret):
        finish_volume = self.occupied_volume + waret
        if finish_volume > self.capacity_volume:
            print('не вместится')
        else:
            self.occupied_volume = finish_volume

    def remove_water(self, water_r):
        # finish_volume = self.occupied_volume - waret_r
        if water_r > self.occupied_volume:
            print('нет в стакане столько воды')
        else:
            self.occupied_volume -= water_r

    def __str__(self):
        return f' в стакане сейчас {self.occupied_volume}'


glass1 = GlassAddRemove()
print(glass1)
glass1.add_water(100)
print(glass1)
glass1.add_water(400)
print(glass1)
glass1.remove_water(600)
print(glass1)

print('----' * 10)
# 6. Создайте три объекта типа GlassAddRemove,
#    вызовите функцию dir для трёх объектов и для класса GlassAddRemove.
#    а. Получите типы объектов и класса
#    б. Проверьте тип созданного объекта.
glass2 = GlassAddRemove()
glass3 = GlassAddRemove()
print(dir(GlassAddRemove))
print(dir(glass1))
print(dir(glass2))
print(dir(glass3))
print('----' * 10)
# ---------------------------------------------------------------------------------------------
# Внутренние объекты класса (стр. 25-33)

# 7. Получите список атрибутов экземпляра класса в начале метода __init__,
#    в середине __init__ и в конце __init__, (стр. 28-30)
#    а также после создания объекта.
#    Опишите результат.
print(glass1.__dict__)


print('----' * 10)
# 8. Создайте три объекта Glass. (стр. 27)
#    Получите id для каждого объекта с соответсвующим id переменной self.

print(id(glass1.occupied_volume))
print(id(glass2.occupied_volume))
print(id(glass3.occupied_volume))


print('!----!----' * 10)


# 9. Корректно ли следующее объявление класса с точки зрения:
#     - интерпретатора Python;
#     - соглашения о стиле кодирования
#    Запустите код.

class d: # Класс с верхнего регистра
    def __init__(f, a=2):
        f.a = a

    def print_me(p): # необхлдимо def print_me(f)
        print(p.a)


d.print_me(d())

print('!----!----' * 10)

# 10. Исправьте
class A:
    def __init__(self, a):
        if 10 < a < 50:
            print('+3 =')
            self.a = a
            self.a += 3
            return
        self.a = a

    def __str__(self):
        return f' значение {self.a}'


a = A(12)
print(a)

# Объясните так реализовывать __init__ нельзя?


# 11. Циклическая зависимость (стр. 39-44)
#

class Node:
    def __init__(self, prev=None, next_=None):
        self.__prev = prev
        self.__next = next_

    def set_next(self, next_):
        self.__next = next_

    def set_prev(self, prev):
        self.__prev = prev

    def __str__(self):
        ...

    def __repr__(self):
        ...


class LinkedList:

    def insert(self, node, index=0):
        '''
        Insert Node to any place of LinkedList
        node - Node
        index - position of node
        '''
        ...

    def append(self, node):
        '''
        Append Node to tail of LinkedList
        node - Node
        '''
        ...

    def clear(self):
        '''
        Clear LinkedList
        '''
        ...

    def find(self, node):
        ...

    def remove(self, node):
        ...

    def delete(self, index):
        ...
























