import os
import random as rnd

os.system('COLOR B')


class Animal:
    def __init__(self, speed, live=True, sound=None, _degree_of_danger=0, _cords=[0, 0, 0]):
        self.speed = speed
        self.live = live
        self.sound = sound
        self._DEGREE_OF_DANGER = _degree_of_danger
        self._cords = _cords

    def move(self, dx, dy, dz):
        if dz >= 0:
            self._cords = [dx, dy, dz] * self.speed
        else:
            print("It's too deep, I can't dive :(")

    def get_cords(self):
        print(f"X: {self._cords[0]}, Y: {self._cords[1]}, Z: {self._cords[2]}")

    def speak(self):
        print(self.sound)

    def attack(self):
        if self._DEGREE_OF_DANGER[0] < 5:
            print("Sorry, I'm peaceful :)")
        else:
            print("Be careful, I'm attacking you 0_0")


class Bird(Animal):
    def __init__(self, speed, beak, live=True, sound=None, _degree_of_danger=0, _cords=[0, 0, 0]):
        super().__init__(speed, live, sound, _degree_of_danger, _cords)
        self.beak = beak

    def lay_eggs(self):
        print(f"Here are(is) {rnd.randint(1, 4)} eggs for you")


class AquanticAnimal(Animal):
    def __init__(self, speed, live=True, sound=None, _degree_of_danger=3, _cords=[0, 0, 0]):
        super().__init__(speed, live, sound, _degree_of_danger, _cords)

    def dive_in(self, dz):
        dz /= 2
        self._cords[2] = dz


class PoisonousAnimal(Animal):
    def __init__(self, speed, live=True, sound=None, _degree_of_danger=8, _cords=[0, 0, 0]):
        super().__init__(speed, live, sound, _degree_of_danger, _cords)


class Duckbill(Bird, AquanticAnimal, PoisonousAnimal):
    def __init__(self, speed, live=True, sound="Click-click-click", _degree_of_danger=8, _cords=[0, 0, 0]):
        super().__init__(speed, live, sound, _degree_of_danger, _cords)


db = Duckbill(10)

print(db.live)
print(db.beak)

db.speak()
db.attack()

db.move(1, 2, 3)
db.get_cords()
db.dive_in(6)
db.get_cords()

db.lay_eggs()

try:
    os.system('PAUSE')
except:
    os.system('CLS')
