p = list(map(int,input().split()))
n = p[0]
k = p[1]
x = []
for i in range (0,n,1):
   try:
       x.append(input().replace(" ","")[k])
   except:
       x.append("")
for i in x:
    print(i)
   
