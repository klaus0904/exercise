
def is_match( str ) :
    stack = []
    bracket_map = { '{' : '}' , '(' : ')' , '[' : ']' }
    
    right_bracket = "}])"
    
    for char in str:
        if char in bracket_map  :
            stack.append(char)
            continue

        if char in right_bracket :
            if ( 0 == len(stack) or char != bracket_map.get( stack[-1] )) :
                return False
            else :
                #match  
                stack.pop()
            
    if( len(stack) == 0 ) :
        return True
    else :
        return False   