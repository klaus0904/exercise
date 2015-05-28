
def is_huiwen(check_str) :
    str_len = len(check_str)
    str_left = check_str[0:str_len/2]
    str_right = check_str[:-(str_len/2)-1:-1]

    return str_left == str_right
    
if __name__ == "__main__" :
    str_set = ["123456654321","abcdcba","123454321", "liyong", "this is a python program"]
    
    for check_str in str_set :
        if is_huiwen(check_str) :
            print check_str
