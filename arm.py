num = int(input())
sum = 0
tempo = num

while tempo>0 :
    numsplit = tempo % 10
    sum = sum + (numsplit ** 3)
    tempo = tempo // 10
if num == sum:
    print("yes")
else:
    print("no")
