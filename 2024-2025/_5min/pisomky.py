def reverse(p: list, b, e) -> list:
    n = 1
    for i in range(b, (e+b)//2):
        p[i], p[e-n] = p[e-n], p[i]
        n += 1
    return p

def RPN(arr):
    stack = []
    for i in arr:
        if i in "+-*/":
            a = stack.pop()
            b = stack.pop()
            if i == "+":
                stack.append(a + b)
            elif i == "-":
                stack.append(a - b)
            elif i == "*":
                stack.append(a * b)
            elif i == "/":
                stack.append(float(a / b))
        else:
            stack.append(int(i))
    return stack[0]