low = int(input())
up = int(input())
for i in range(low+1,up):
    if i>1:
        for j in range(2,i):
            if (i%j==0):
                break
        else:
            print(i)
