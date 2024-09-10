class House:
    def __init__(self, name, floors ):
        self.name = name
        self.number_of_floors = floors
    def go_to(self,new_floor):
        if (isinstance(new_floor,int) and
                new_floor < self.number_of_floors and
                new_floor > 0):
            for i in range(1,new_floor + 1):
                print(i)
        else:
            print("Такого этажа не существует.")


h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)
h1.go_to(5)
h2.go_to(10)