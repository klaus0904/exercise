
class Cat(object) :
    def __init__(self) :
        self.observers = []
    def Miaow(self) :
        print "Miaow!"
        for observer in self.observers :
            try:
                observer()
            except TypeError :
                print "Error! "+ str(type(observer)) +" is not a function!"

    def Register(self, observer) :
        self.observers.append(observer)

    def UnRegister(self, observer) :
        self.observers.remove(observer)

class Mouse(object) :
    number = 0
    def __init__(self) :
        Mouse.number += 1
        self.name = "Mouse" + str(Mouse.number)
        
    def Run(self) :
        print self.name + " heard miaow, run!"

class Human(object) :
    def WakeUp(self) :
        print "Human heard miaow, wake up!"
    
