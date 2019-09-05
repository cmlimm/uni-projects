class Hero:
    """
    Создание героя
    """
    def __init__(self, name, x=0, y=0, hp=10, dmg=2, speed=2, fd=2):
        self.name = name
        self.x = x
        self.y = y
        self.hp = hp
        self.dmg = dmg
        self.speed = speed
        self.fd = fd
        print("У нас новый герой " + self.name)
        print("Место появления: " + str(self.x) + " " + str(self.y))
        print("Здоровье: " + str(self.hp))
        print("Урон: " + str(self.dmg))
        print("Скорость: " + str(self.speed))
        print("Дальность атаки: " + str(self.fd))
        print()

    """
    Движение
    """
    def run(self, direction):
        if self.hp > 0:
            self.x += direction*self.speed
            print(self.name + " пробежал на " + str(self.speed) +
                ". Теперь его координаты: " + str(self.x) + " " + str(self.y))
        else:
            print(elf.name + " мертв и не может бегать")
        print()

    """
    Стрельба
    """
    def shoot(self, target):
        if self.hp > 0 and target.hp > 0:
            if ((self.x-target.x)**2+(self.y-target.y)**2) <= self.fd**2:
                target.hp -= self.dmg
                print(self.name + " нанес " + target.name + " " + str(self.dmg) + " урона")
                if target.hp <= 0:
                    print(target.name + " умер!")
                else:
                    print("Здоровье " + target.name + " теперь равно " + str(target.hp))
            else:
                print(self.name + " попытался попасть в " + target.name + " и промахнулся!")
        elif self.hp < 0:
            print(self.name + " мертв и не может стрелять")
        elif target.hp < 0:
            print(target.name + " мертв и в него нельзя стрелять")
        print()
    """
    Подбирание предметов
    """
    def loot(self, good, target):
        if self.hp > 0 and target.hp > 0:
            if good.x == self.x and good.y == self.y:
                print(self.name + " пытается использовать " + good.name + " на " + target.name)
                good.use(target)
            else:
                print(target.name + "слишком далеко от" + good.name)
        elif self.hp < 0:
            print(self.name + " мертв и не может использовать предметы")
        elif target.hp < 0:
            print(target.name + " мертв и на него нельзя использовать предметы")
        print()
"""
Летающий герой
"""
class FlyingHero(Hero):
    def __init__(self, name, x=0, y=0, hp=10, dmg=2, speed=2, fd=2):
        super().__init__(name, x, y, hp, dmg, speed, fd)
        print("Этот герой летает!")
        print()
    """
    Полет
    """
    def fly(self, direction):
        if self.hp > 0:
            self.y += direction*self.speed
            if direction >= 0:
                print(self.name + " взлетел на " + str(self.speed) +
                    "\nТеперь его координаты: " + str(self.x) + " " + str(self.y))
            elif self.y >= 0 and direction < 0:
                print(self.name + " опустился на " + str(self.speed) +
                    "\nТеперь его координаты: " + str(self.x) + " " + str(self.y))
            elif self.y < 0 and direction < 0:
                self.y = 0
                self.hp -= 1
                if self.hp > 0:
                    print(self.name + " не рассчитал ускорение и получил 1 урон, его здоровье: " + self.hp +
                        "\nТеперь его координаты: " + str(self.x) + " " + str(self.y))
                else:
                    print(self.name + " не рассчитал ускорение. Больше его с нами нет.")
        else:
            print(self.name + " мертв и не может летать")
        print()

class Goods:
    """
    Создание предмета
    """
    def __init__(self, name, aspect, isBuff, x=0, y=0):
        self.name = name
        self.aspect = aspect
        self.x = x
        self.y = y
        self.used = False
        print("Появился предмет " + self.name + " по координатам " + str(self.x) + " " + str(self.y))
        if isBuff:
            self.isBuff = 1
            print("Предмет положительно влияет на параметр " + self.aspect)
        else:
            self.isBuff = -1
            print("Предмет отрицательно влияет на параметр " + self.aspect)
        print()
    """
    Использование предмета
    """
    def use(self, target):
        if not self.used:
            if self.aspect == "hp":
                target.hp += self.isBuff*1
                self.used = True
                print("Теперь здоровье " + target.name + " равняется " + str(target.hp))
            elif self.aspect == "dmg":
                target.dmg += self.isBuff*2
                self.used = True
                print("Теперь урон " + target.name + " равняется " + str(target.dmg))
            elif self.aspect == "speed":
                target.speed += self.isBuff*1
                self.used = True
                print("Теперь скорость " + target.name + " равняется " + str(target.speed))
            elif self.aspect == "fd":
                target.fd += self.isBuff*2
                self.used = True
                print("Теперь дальность атаки " + target.name + " равняется " + str(target.fd))
        else:
            print("Предмет " + self.name + " уже использован")

hero1 = Hero("One")
hero2 = FlyingHero("Two")
hero1.shoot(hero2)
hero2.shoot(hero1)
hero2.run(-1)
hero1.run(1)
hero2.fly(1)
hero1.shoot(hero2)
hero1.run(-1)
hero1.shoot(hero2)
hero1.run(-1)
hero1.shoot(hero2)
speedBoost = Goods("Фейзы", "speed", True, -2, 0)
hero1.loot(speedBoost, hero1)
hero2.run(1)
hero1.shoot(hero2)
hero1.run(1)
fdBoost = Goods("Прицел", "fd", True, 1, 0)
hero1.loot(fdBoost, hero1)
hero1.shoot(hero2)
hero1.loot(fdBoost, hero1)
hero1.shoot(hero2)
poision = Goods("Смертб", "hp", False, 1, 0)
hero1.loot(poision, hero2)
hero2.fly(-1)
hero2.fly(-1)
