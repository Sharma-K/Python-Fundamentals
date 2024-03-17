class student():
    def __init__(self, name, roll):
        self.name = name
        self.roll = roll
    
    def changeRoll(self, id):
        self.id = id
    
    def print(self):
        print("{} - {}".format(self.name, self.roll))

keshav = student("Keshav", 101)
keshav.print()
keshav.changeRoll(873)
keshav.print()