p = list(map(int,input().split()))
n = p[0]
k = p[1]
x = []
for i in range (0,n,1):
   a = input()
   maxa = len(a)+1
   t = 0
   for j in range (0,maxa):
       if j >= maxa-1:
           x.append("")
           break
       elif a[j] == " ":
           t -= 1
       elif t == k:
           x.append(a[j])
           break
       t += 1
for i in x:
    print(i)
