f = open("day2.txt")
data = f.read() 
arr=[]
count=0
for row in data.split("\n"):
    arr.append(row.split(" "))
    for j in range (len(arr[count])):
         arr[count][j]=int(arr[count][j])
    count+=1
count=0
for i in arr:
    flag=0
    if(i[0]>i[1]):
            isincreasing=1
            isdecreasing=0
    elif(i[1]>i[0]):
            isdecreasing=1
            isincreasing=0
    for j in range(len(i)-1):
        if(i[j]>i[j+1] and (isdecreasing==1 or (i[j]-i[j+1] > 3))):
            flag=1
            break
        elif(i[j+1]>i[j] and (isincreasing==1 or (i[j+1]-i[j] > 3))):
            flag=1
            break
        elif(i[j+1]==i[j]):
             flag=1
             break
    if(flag==0):
         count+=1
print(count)