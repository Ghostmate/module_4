class House():
    houses_history = []

    def __new__(cls, *args):
        cls.houses_history.append(args[0])
        return super().__new__(cls)

    def __enter__(self):
        return self

    def __init__(self, name, floors):
        self.name = name
        self.number_of_floors = floors

    def go_to(self, new_floor):
        if (isinstance(new_floor, int) and
                new_floor < self.number_of_floors and
                new_floor > 0):
            for i in range(1, new_floor + 1):
                print(i)
        else:
            print("Такого этажа не существует.")

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return ("Название: <" + str(self.name)
                + ">, кол-во этажей: <" +
                str(self.number_of_floors) + ">")

    def __eq__(self, other):
        return self.number_of_floors == other.number_of_floors

    def __lt__(self, other):
        return self.number_of_floors < other.number_of_floors

    def __le__(self, other):
        return self.number_of_floors <= other.number_of_floors

    def __gt__(self, other):
        return self.number_of_floors > other.number_of_floors

    def __ge__(self, other):
        return self.number_of_floors >= other.number_of_floors

    def __ne__(self, other):
        return self.number_of_floors != other.number_of_floors

    def __add__(self, other):
        value = 0
        if isinstance(other, House):
            value = other.number_of_floors
        elif isinstance(other, int):
            value = other
        return self.__iadd__(value)

    def __radd__(self, other):
        return self.__add__(other)

    def __iadd__(self, value):
        self.number_of_floors += value
        return self

    def __del__(self):
        print("<" + self.name + "> снесён, но он останется в истории")


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
