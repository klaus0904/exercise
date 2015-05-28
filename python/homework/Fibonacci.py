
def fibonacci(num) :
    pre = 1;
    pre_of_pre = 0;
    current = 0;
    sum = pre + pre_of_pre;
    for i in range(2, num) :
        #print pre
        #print pre_of_pre
        current = pre + pre_of_pre
        #print current
        print "\n"
        sum += current
        pre_of_pre = pre
        pre = current
        
    return sum;
        
        
if __name__ == "__main__" :
    print fibonacci(8)
