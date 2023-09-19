def faktorial(n):
    if n == 0: return 1
    return n*faktorial(n-1)
#print(faktorial(int(input())))

def fibonacci(n, n1, n2, hlbka):
    if hlbka == 0: return
    if n == 0: n, n1 = 1, 0; print(0)
    print(n)
    return fibonacci(n+n1,n1+n2,n1, hlbka-1)
fibonacci(0,0,0,int(input()))