import random
import json

from time import sleep

class Human:
    def __init__(self, name):
        self.name = name
        self.gladness = 50
        self.money = 100
        self.car = None
        self.computer = None
    def greeting(self, human):
        print(f"Hello {human.name}, I am {self.name}")
    def drive(self):
        if self.car:
            self.car.drive()
    def rest(self):
        self.gladness += random.randint(1, 3)
        self.money -= random.randint(2, 5)
    def work(self):
        self.gladness -= random.randint(1, 2)
        self.money += random.randint(5, 10)

class Home:
    def __init__(self):
        self.humans = []
    def add(self, human):
        self.humans.append(human)
    def show(self):
        names = []
        for human in self.humans:
            names.append(human.name)
        print(names)

class Car:
    def __init__(self, n, y, e):
        self.name = n
        self.year = y
        self.engine = e
        self.owner = None
    def buy(self, human):
        if not self.owner:
            if human.money >= 200:
                human.money -= 200
                self.owner = human
                human.car = self
                print(f"{human.name} купил {self.name}")
            else:
                print(f"Недостаточно денег у {human.name}")
        else:
            print(f"Машина уже пренадлежит {self.owner.name}")
    def drive(self):
        print("chux-chux")

class Computer:
    def __init__(self, c, v, m):
        self.comp = c
        self.videocard = v
        self.monitor = m
        self.ownergamer = None
    def buycomp(self, human):
        if not self.ownergamer:
            if human.money >= 150:
                human.money -= 150
                self.ownergamer = human
                human.computer = self
                print(f"{human.name} купил комрьютер {self.name}")
            else:
                print(f"Недостаточно денег на комьютер у {human.name}")
        else:
            print(f"Компьютер уже пренадлежит {self.ownergamer.name}")
    def gaming(self):
        print("звуки клавиатуры*")

class Player(Human):
    def __init__(self, name, h, w):
        super().__init__(name)
        self.height = h
        self.weight = w
    def save(self):
        with open('save.json', 'w') as f:
            data = {}
            data["name"] = self.name
            data["h"] = self.height
            data["w"] = self.weight
            json.dump(data, f)
    def actions(self):
        print("Выберите действие: ")
        print("1. Отдохнуть")
        print("2. Пойти на работу")
        print("3. Купить машину")
        print("4. Купить компьютер")
        print("5. Баланс")
    def day(self):
        choice = int(input("-> "))
        if choice == 1:
            self.rest()
        elif choice == 2:
            self.work()
        elif choice == 3:
            #Показываем, какие машины есть и предлагаем их купить
            print("Машины: ")
            for i in range(len(autopark)):
                print(i + 1, autopark[i].name)
            choice = int(input("-> "))
            #Выбираем машину и вызываем у нее buy
            autopark[choice - 1].buy(self)
        elif choice == 4:
            print("Компьютеры: ")
            for i in range(len(computers)):
                print(i + 1, computers[i].name)
            choice = int(input("-> "))
            computers[choice - 1].buy(self)
        elif choice == 5:
            print(f"Ваш баланс: {player.money}")
            self.day()

class Thief(Human):
    #Вызываем конструктор
    def __init__(self, name):
        super().__init__(name)
        #strengh = random
        self.stength = random.randint(5, 20)

    def steal(self, human):
        # -human +thief
        human.money -= self.stength
        thief.money += self.stength
        #Вор обокрал кого-то
        print(f"Вор обворовал {human.name}")

class GoodMan(Human):
    def __init__(self, name):
        super().__init__(name)
        self.goodact = random.randint(3, 42)
        self.stength = random.randint(5, 20)

    def cashback(self, human):
        human.money += self.goodact
        # награбленное отнимаеться у вора
        thief.money -= self.stength
        print(f"Герой вернул деньги {human.name}")

home = None
computers =None
autopark = None
player = None
thief = None
goodman = None
def game_start():
    global home
    global autopark
    global computers
    global thief
    global goodman

    thief = Thief("Vitaliy")

    goodman = GoodMan("Danil")

    home = Home()

    human_1 = Human("Vanya")
    human_2 = Human("Maxim")
    human_3 = Human("Ilya")
    human_4 = Human("Stepan")
    human_5 = Human("Andrey")
    human_6 = Human("Kristina")
    human_7 = Human("Alina")
    human_8 = Human("Alex")

    home.add(human_1)
    home.add(human_2)
    home.add(human_3)
    home.add(human_4)
    home.add(human_5)
    home.add(human_6)
    home.add(human_7)
    home.add(human_8)

    autopark = [
        Car("BMW", 2022, 100),
        Car("Bentli", 2018, 90),
        Car("Bugatti", 2016, 70),
    ]

    computers = [
        Computer("Asus rog strix", 3070, 244),
        Computer("Lenovo", 1050, 120),
        Computer("Macbook", 650, 60),
    ]

def create_player():
    global player
    h = input("Введите рост персонажа: ")
    w = input("Введите вес персонажа: ")
    name = input("Введите имя персонажа: ")
    player = Player(name, h, w)
    player.save()

def init_player():
    global player
    with open('save.json') as json_file:
        data = json.load(json_file)
        if not data:
            create_player()
        else:
            player = Player(data["name"], data["h"], data["w"])
    home.add(player)

game_start()
init_player()

day = 1
while True:
    print("Day: ", day)
    player.actions()
    player.day()
    for human in home.humans:
        actions = [human.rest, human.work]
        random.choice(actions)()
        if random.randint(1, 100) <= 5:
            random.choice(autopark).buy(human)
        if random.randint(1, 100) <= 10:
            random.choice(computers).buy(human)
    #С шансом 20% вор ворует деньги
    #Жертву выбирает случайно
    if random.randint(1, 100) <= 20:
        thief.steal(random.choice(home.humans))
    if random.randint(1, 100) <= 15:
        goodman.cashback(random.choice(home.humans))

    day += 1