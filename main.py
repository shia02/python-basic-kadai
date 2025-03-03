class Human:
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
    def printinfo(self):
        print(self.name + ' ' + str(self.age))

human = Human("test", 30)
human.printinfo()