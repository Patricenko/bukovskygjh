def isoperator(now):
    if now == "+" or now == "-" or now == "*" or now == "/":
        return True;
    return False;
n = int(input())
x = list(input())
final = []
for i in range (n):
    if isoperator(x[i]):
        if isoperator(x[i+1]):
            final.append("(")
        elif not isoperator(x[i+1]):
            final.append(f'{x[i+1]}{x[i]}{x[i+2]}')
            i += 2
    elif not isoperator(x[i]):
        
print(final)
            
            
    
