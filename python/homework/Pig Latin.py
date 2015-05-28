
def trans_to_pig_latin(str):
    if len(str) == 1 :
        return str + "ay"
        
    first_char = str[0]
    second_char = str[1]
    other_str = str[2:]
    
    if first_char.isupper()  :
        first_char = first_char.lower()
        second_char = second_char.upper()

    return second_char + other_str + first_char + "ay"
    
if __name__ == "__main__" :
    test_str = ("This is a test string").split()
    str_after_trans =  [ trans_to_pig_latin(word) for word in test_str ]
        
    print str_after_trans
