class House:
    houses_history = []  # Список для хранения названий домов

    def __new__(cls, *args, **kwargs):
        # Добавление названия дома в историю
        cls.houses_history.append(args[0])  # Доступ к названию из *args
        return super().__new__(cls)  # Вызов стандартного метода new

    def __init__(self, first, second=25, third=3.14):
        self.first = first
        self.second = second
        self.third = third

    def __del__(self):
        print(f"{self.first} снесён, но он останется в истории")

# Создание объектов
h1 = House('ЖК Эльбрус', 10)
print(House.houses_history)

h2 = House('ЖК Акация', 20)
print(House.houses_history)

h3 = House('ЖК Матрёшки', 20)
print(House.houses_history)

# Удаление объектов
del h2
del h3

print(House.houses_history)
del h1

print(House.houses_history)


