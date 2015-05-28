#coding=utf8  
from command import Direction 
from command import ExitCmd
from command import EnterCmd
from state import StateRun 
from state import StateStop 
from state import StateDoorOpened 
from state import StateDoorClosed 

import random
import state
     
class Lift(object):
    def __init__(self, floor_number) :
        self.enterCmdList = []
        self.exitCmdList = []
        self.cmdNeedToExecuteList = []
        self.currentFloor = 1
        self.currentDirection = Direction.Up
        self.maxFloorNum = floor_number
        
    def AddEnterCmd(self, enter_cmd):
        self.enterCmdList.append(enter_cmd)
        
    def Run(self):  
        self.state = StateRun(self)
        
    def IsNeedToStop(self):      
        return self.IsSomeoneWannaEnter() or  self.IsSomeoneWannaExit()
     
    def IsSomeoneWannaEnter(self):
        for enter_cmd in self.enterCmdList:
            if self.currentFloor == enter_cmd.floorFrom \
                and  self.currentDirection == enter_cmd.direction :
                return True
        return False
    
    def IsSomeoneWannaExit(self):
        for exit_cmd in self.exitCmdList:
            if self.currentFloor == exit_cmd.floorTo :
                return True 
        return False
        
    def NeedToRun(self):
        for exit_cmd in self.exitCmdList:
            if self.currentFloor != exit_cmd.floorTo :
                return True 
                
        for enter_cmd in self.enterCmdList:
            if self.currentFloor != enter_cmd.floorFrom :
                return True                
        return False        
        
    def GoToNextFloor(self):
        if self.currentDirection == Direction.Up :
            self.currentFloor += 1
            if self.currentFloor == self.maxFloorNum :
                self.currentDirection = Direction.Down
                
        elif self.currentDirection == Direction.Down :
            self.currentFloor -= 1
            if self.currentFloor == 1 :
                self.currentDirection == Direction.Up
        else :
            assert(false)
            
    def ExecuteEnterOrExitCmd(self):
        #下电梯
        other_floor_cmd_list = []       
        for exit_cmd in self.exitCmdList:
            if self.currentFloor == exit_cmd.floorTo :
                exit_cmd.Execute()
            else :
                other_floor_cmd_list.append(exit_cmd)
        self.exitCmdList = other_floor_cmd_list
        #上电梯
        for enter_cmd in self.enterCmdList:
            if self.currentFloor == enter_cmd.floorFrom \
                and  self.currentDirection == enter_cmd.direction  :
                exit_cmd = ExitCmd()
                exit_cmd.name = enter_cmd.name
                exit_cmd.floorTo = random.randint(1, self.maxFloorNum)
                while exit_cmd.floorTo == self.currentFloor :
                    exit_cmd.floorTo = random.randint(1, self.maxFloorNum)
                self.exitCmdList.append(exit_cmd)
                print "%s want to go %d floor." % (exit_cmd.name, exit_cmd.floorTo)
    
    def Stop(self) :
        self.state = StateStop(self)
        
