class Fan:
    def __init__(self, make, radius, color):
        self.make = make
        self.radius = radius
        self.color = color
        self.speed = 0
        self.is_on = False
        
    def __repr__(self):
        return repr((self.make, self.radius, self.color, self.speed, self.is_on))
        
    def switch_on(self):
        self.is_on = True
        self.speed = 3
        
    def switch_off(self):
        self.is_on = False
        self.speed = 0
    
    def increase_speed(self):
        if self.is_on and self.speed > 0:
            self.speed += 1
            
    def decrease_speed(self):
        if self.is_on and self.speed <= 5:
            self.speed -= 1

fan = Fan('Crompton', 50, 'Black')

# print(fan)

fan.switch_on()
print(fan)

fan.increase_speed()
print(fan)

fan.increase_speed()
print(fan)

fan.decrease_speed()
print(fan)

fan.switch_off()
print(fan)
