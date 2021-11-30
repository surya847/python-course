n=5
k=[]
for i in range(1,n+1):
    m=int(input("Enter the first element {0}:".format(i)))
    k.append(m)
print(k)
print("sum: ",sum(k))
print("avg: ",sum(k)/len(k))
