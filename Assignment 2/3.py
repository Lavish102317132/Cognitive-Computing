import random
l=[]
i=0
while i<100:
    l.append(random.randint(100,900))
    i=i+1
print(l)
even=0
odd=0
prime=0
for i in l:
    if i%2==0:
        even=even+i
    else :
        odd=odd+i
    for j in range(2,i):
        if i%j==0:
            break
        else:
            prime=prime+i
print(odd,even,prime)            
