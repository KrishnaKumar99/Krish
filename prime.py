pr = int(input())
if (pr>1):
    for i in range(2,pr):
        if (pr%i==0):
            print("no")
            break
    else:
        print('yes')
else:
    print("no")
