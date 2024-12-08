## star 1
f = open("day1.txt")
data = f.read() 
arr1=[]
arr2=[]
count=0
for row in data.split("\n"):
    arr1.append(int(row.split("  ")[0]))
    arr2.append(int(row.split("  ")[1]))
    count+=1
arr1.sort()
arr2.sort()
sum=0
for i in range(count):
    sum+=  (arr2[i] - arr1[i]) if (arr2[i]>arr1[i]) else (arr1[i]-arr2[i])
print(sum)

## star 2
f = open("day1.txt")
data = f.read() 
arr1=[]
arr2=[]
count=0
for row in data.split("\n"):
    arr1.append(int(row.split("  ")[0]))
    arr2.append(int(row.split("  ")[1]))
    count+=1
arr1.sort()
arr2.sort()
sum=0
for i in range(count):
    sum+=(arr1[i]*arr2.count(arr1[i]))
print(sum)