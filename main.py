class Human:
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

    def check_adult(self):
        if self.age >= 20:
            print(self.name + " is adult.")
        else:
            print(self.name + " is not adult.")

humans = [Human("human1", 21), Human("human2", 19)]
human3 = Human("human3", 20)
humans.append(human3)
for human in humans:
    human.check_adult()