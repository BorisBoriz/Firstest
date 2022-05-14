import random
from time import sleep

class Student:
    def __init__(self, name):
        self.name = name
        self.progress = 0
        self.gladness = 0
        self.money = 1000
    def greeting(self):
        print(f"I am {self.name}")
    def rest(self):
        uprest = random.randint(1, 3)
        moneyspend = random.randint(1, 150)
        print(f"{self.name} | gladness up on {uprest}. Now gladness is {self.gladness + uprest}. Money down on {moneyspend}. Now money is {self.money - moneyspend}")
        self.gladness += uprest
        self.money -= moneyspend
    def study(self):
        downrest = random.randint(1, 3)
        upprogress = random.randint(1, 3)
        print(f"{self.name} | Progress up on {upprogress}. Now progess is {self.progress + upprogress}. Gladness down on {downrest}. Now gladness is {self.gladness - downrest}")
        self.gladness -= downrest
        self.progress += upprogress
    def Work(self):
        downrest = random.randint(1, 3)
        moneyearn = random.randint(1, 300)
        upprogress = random.randint(1, 3)
        print(f"{self.name} | Money earn on {moneyearn}. Now money up on {self.money + moneyearn}. Gladness down on {downrest}. Now gladness is {self.gladness - downrest}. Progress up on {upprogress}. Now you get expirience on work = {self.progress + upprogress}")
        self.money += moneyearn
        self.gladness -= downrest
        self.progress += upprogress
    def pwin(self):
        print(f"{self.name} первый достиг максимальный прогресс умный но с долгами и не счастлив")
    def gwin(self):
        print(f"{self.name} первый достиг максимальное счастье но он глупый и с долгами")
    def mwin(self):
        print(f"{self.name} первый достиг максимальных денег, также с долгами и не умный и не счастлив")

students = []
students.append(Student("Maxim"))
students.append(Student("Sergey"))
students.append(Student("Ivan"))
students.append(Student("Petr"))
students.append(Student("Georgiy"))

for student in students:
    student.greeting()

progress_winner = None
gladeness_winner = None
millionaire_winner = None

day = 1

while True:
    print("Day: ", day)
    for student in students:
        actions = [student.rest, student.study]
        random.choice(actions)()
        if student.gladness >= 300 and not gladeness_winner:
            gladeness_winner = student
        if student.gladness >= 300 and not millionaire_winner:
            gladeness_winner = student
        if student.progress >= 300 and not progress_winner:
            progress_winner = student
        if student.progress >= 300 and not millionaire_winner:
            progress_winner = student
        if student.money >= 1000 and not gladeness_winner:
            millionaire_winner = student
        if student.money >= 1000 and not progress_winner:
            millionaire_winner = student
    day+= 1
    if progress_winner and gladeness_winner:
        break
progress_winner.pwin()
gladeness_winner.gwin()
millionaire_winner.mwin()

