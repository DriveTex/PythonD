import random
class student:
    def __init__(self,name):
        self.name="Denis"
        self.radist=1
        self.progres=1
        self.life=True
    def study(self):
        print("Go Study")
        self.radist-=0.5
        self.progres+=1
    def chill(self):
        print("Go Chill")
        self.radist+=1
        self.progres-=0.5
    def sleep(self):
        print("Go Sleep")
        self.radist+=1
    def perevirka(self):
        if(self.radist<0):
            print ("DEPRESION DEAD")
            self.life=False
        elif(self.rogres<0):
            print("STUPID DEAD")
            self.life = False
    def dayoff(self):
        print("Ваша радість:",self.radist )
        print("Ваш прогрес:",self.progres)
    def simulate(self):
        rnd=random.randint(1,3)
        if(rnd == 1):
            self.chill()
        if(rnd == 2):
            self.study()
        if(rnd == 3):
            self.sleep()
            self.perevirka()
            self.dayoff()
ivan=student(name=ivan)
for day in range(10):
    ivan.simulate(day)
    if ivan.life==False
        break