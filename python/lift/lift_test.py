#coding=utf8


import time 
import random
import lift    
import command


if __name__ == "__main__" :
    floor_number = 20
    mylift = lift.Lift(20)
    print mylift.currentFloor
    human = ["Zhao","Qian","Sun","Li","Zhou","Wu","Zheng","Wang","Feng","Chen","Chu","Wei","Jiang","Shen","Han","Yang"]
    for name in human:
        cmd = command.EnterCmd()
        cmd.name = name
        cmd.floorFrom = random.randint(1,floor_number)
        cmd.direction = random.randint(0, 1) #不考虑 顶楼上楼和底楼下楼情况
        mylift.AddEnterCmd(cmd)

    
    mylift.Stop()

