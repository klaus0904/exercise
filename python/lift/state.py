import time

class State(object):
    def __init__(self, lift):
        self.lift = lift
    
class StateRun(State):
    def __init__(self, lift):
        State.__init__(self, lift)
        print "run......."
        self.Run()
        
    def Run(self):
        while not self.lift.IsNeedToStop() :
            self.lift.GoToNextFloor()
        self.lift.Stop()
        
class StateStop(State):
    def __init__(self, lift):
        print "door stop"
        State.__init__(self, lift)
        self.stopState = StateDoorClosed(lift)

class StateDoorOpened(State):
    def __init__(self, lift):
        State.__init__(self, lift)
        print "door open."
        self.lift.ExecuteEnterOrExitCmd()
        self.stopState = StateDoorClosed(lift)

class StateDoorClosed(State):
    def __init__(self, lift):
        State.__init__(self, lift)
        print "door closed."
        self.Checking()
        
    def Checking(self):
        while not self.IsNeedToOpen() and not self.lift.NeedToRun() :
            time.sleep(1)
            
        if self.IsNeedToOpen():
            self.stopState = StateDoorOpened(self.lift)
        if self.lift.NeedToRun():
            self.lift.Run()
        
    def IsNeedToOpen(self):
        return self.lift.IsSomeoneWannaEnter() or self.lift.IsSomeoneWannaExit()
        
        