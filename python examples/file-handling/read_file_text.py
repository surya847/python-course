fhand = open('mbox_mid.txt')
count = 0
ids=[]
for line in fhand:
    if line.startswith('From:') :
     print(line)
     count = count + 1
     id=line.split()
     print(id)
     ids.append(id[1])
print("No of lines start with word From is ", count)
print("List of id's  is ", ids)
