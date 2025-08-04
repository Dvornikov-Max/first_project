#Задание 2
class Turtle:
    def __init__(self, x=0, y=0, s=1):
        self.x = x
        self.y = y
        self.s = s

    def go_up(self):
        self.y += self.s

    def go_down(self):
        self.y -= self.s

    def go_left(self):
        self.x -= self.s

    def go_right(self):
        self.x += self.s

    def evolve(self):
        self.s += 1

    def degrade(self):
        if self.s <= 1:
            raise ValueError("Скорость не может быть меньше или равна 0")
        self.s -= 1

    def count_moves(self, x2, y2):
        dx = abs(self.x - x2)
        dy = abs(self.y - y2)
        return (dx + dy) // self.s

t = Turtle()
t.go_up()
t.evolve()
print(t.count_moves(10,5))