#Задание 1
class Kassa:
    def __init__(self):
        self.money = 0

    def top_up(self, x):
        self.money += x
        print("После зачисления на счету: ", self.money)

    def count_1000(self):
        print("Целых тысяч на счету: ", self.money // 1000)

    def take_away(self, x):
        if x > self.money:
            raise ValueError("Недостаточно денег")
        self.money -= x
        print("После снятия на счету:", self.money)

k = Kassa()
k.top_up(5500)
k.count_1000()
k.take_away(1000)
a = Kassa()
a.top_up(500)
a.count_1000()
a.take_away(1000)
print(k.money)