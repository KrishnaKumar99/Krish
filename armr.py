
lo = int(input())
up = int(input())
for i in range(lo,up+1):
    sum = 0
    temp = i
    while(temp>0):
        split = temp%10
        sum = sum + (split ** 3)
        temp = temp // 10
    if i == sum:
        print(i)
