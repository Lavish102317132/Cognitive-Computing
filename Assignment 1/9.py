import random
i=0
while i<5:
    print(random.randint(1,100))
    i=i+1
num=random.randint(1,100)
flag=0
for i in range(2,num):
    if num%i==0:
        flag=1
if flag==0:
    print(f"{num} is a prime number")
else :
    print(f"{num} is not a prime number")
n=random.randint(1,6)
print(n)
a = [1, 2, 3, 4, 5]
random.shuffle(a)
print(a)
b= ['apple', 'banana', 'strawberry', 'orange', 'watermelon']
c= random.choice(b)
print(c)
