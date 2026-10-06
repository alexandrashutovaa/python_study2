class Clock:
    def __init__(self):
        self.h = 0
        self.m = 0

    def tick(self, minutes):
        if minutes < 0:
            raise ValueError("Минуты не могут быть меньше 0")
        total = self.h * 60 + self.m + minutes
        total %= 24 * 60
        self.h = total // 60
        self.m = total % 60

    def get_time(self):
        return self.h, self.m


c = Clock()
print(c.get_time())
c.tick(60 * 23 + 15)
print(c.get_time())