class Direction(object):
    Up, Down = 0,1

class Command(object):
    def __init__(self):
        self.name = "Anonymous"


class EnterCmd(Command):
    def __init__(self):
        Command.__init__(self)
        self.floorFrom = 1
        self.direction = Direction.Up
        
    def Execute(self):
        print "%s enter lift at %d floor." % (self.name, self.floorFrom)
        
class ExitCmd(Command):
    def __init__(self):
        Command.__init__(self)
        self.floorTo = 0;
    def Execute(self):
        print "%s leave lift at %d floor." % (self.name, self.floorTo)
        
import time 
import random    
if __name__ == "__main__" :
	human = ["Zhao","Qian","Sun","Li","Zhou","Wu","Zheng","Wang","Feng","Chen","Chu","Wei","Jiang","Shen","Han","Yang"]
	for name in human:
		cmd = EnterCmd()
		cmd.name = name
		cmd.floorFrom = random.randint(1,20)
		cmd.Execute()
		
	for name in human:
		cmd = ExitCmd()
		cmd.name = name
		cmd.floorTo = random.randint(1,20)
		cmd.Execute()		