prefix = 'math.'

def mpcmath_ex(ex):
    
    i = 0
    
    result = 0
    
    ex = ['0','+'] + ex
    
    while i < len(ex):
        
        if ex[i] == '+':
            result += int(ex[i+1])
            
        elif ex[i] == '-':
            result -= int(ex[i+1])
        
        i += 1
    return str(result)
    
funcs = {'ex':mpcmath_ex}
