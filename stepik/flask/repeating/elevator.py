class Elevator:
    MAX_FLOOR = 0
    current_floor = 0

    def __init__(self, mx, cr):
        self.MAX_FLOOR = mx
        self.current_floor = cr

    def up(self):
        if self.current_floor > self.MAX_FLOOR:
            print('Лифт не может опуститься выше')
        elif self.current_floor + 1 <= self.MAX_FLOOR:
            self.current_floor += 1
            print(f'Лифт поднимается на {self.current_floor} этаж')
        else:
            print('Лифт не может подняться выше')

    def down(self):
        if self.current_floor < 0 or self.current_floor>self.MAX_FLOOR:
            print('Лифт не может опуститься выше')
        elif self.current_floor - 1 >= 1:
            self.current_floor -= 1
            print(f'Лифт опускается на {self.current_floor} этаж')
        else:
            print('Лифт не может опуститься ниже')
