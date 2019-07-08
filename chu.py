myl = []
n = int(input())
k = int(input())

for i in range(0, n):
	ca = int(input())
	myl.append(ca)
print (sum(myl[:k]))
