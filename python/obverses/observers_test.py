import observers

if __name__ == "__main__" :
    cat  = observers.Cat()
    mouse1 = observers.Mouse()
    mouse2 = observers.Mouse()
    mouse3 = observers.Mouse()
    human = observers.Human()

    cat.Register( mouse1.Run )
    cat.Register( mouse2.Run )
    cat.Register( mouse3.Run )
    cat.Register( human.WakeUp )
    
    cat.Miaow()
