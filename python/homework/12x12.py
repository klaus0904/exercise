def print12x12() :
    str_temp = ""
    for i in range(1,13) :
        for j in range(1, i+1) :
            str_temp += str(j) + "*" + str(i) + "=" + str(i*j) + "  "            
        str_temp += "\n"
    print str_temp
        
        
if __name__ == "__main__" :
    print12x12()
