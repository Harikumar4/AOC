## star 1
f = open("day7.txt")
data = f.read() 
arr=[]
count=0
for row in data.split("\n"):
    arr.append(row.split(":"))
    arr[count][1]=arr[count][1].split(" ")
    arr[count][0]=int(arr[count][0])
    arr[count][1].pop(0)
    for i in range(len(arr[count][1])):
        arr[count][1][i]=int(arr[count][1][i])
    count+=1
count=0
sum=0

def recur(arr1,count,current_value,check_sum):
    if(count>=len(arr1)-1):
        return current_value==check_sum
        
    add=recur(arr1,count+1,current_value+arr1[count+1],check_sum)
    mul=recur(arr1,count+1,current_value*arr1[count+1],check_sum)
    return add==1 or mul==1


for i in range(len(arr)):
    check=recur(arr[i][1],0,arr[i][1][0],arr[i][0])
    if(check==1):
        sum+=arr[i][0]
print(sum)

## star 2
f = open("day7.txt")
data = f.read() 
arr=[]
count=0
for row in data.split("\n"):
   arr.append(row.split(":"))
   arr[count][1]=arr[count][1].split(" ")
   arr[count][0]=int(arr[count][0])
   arr[count][1].pop(0)
   for i in range(len(arr[count][1])):
       arr[count][1][i]=int(arr[count][1][i])
   count+=1
count=0
sum=0

def recur(arr1,count,current_value,check_sum):
   if(count>=len(arr1)-1):
       return current_value==check_sum
       
   add=recur(arr1,count+1,current_value+arr1[count+1],check_sum)
   mul=recur(arr1,count+1,current_value*arr1[count+1],check_sum)
   concat_val = int(str(current_value) + str(arr1[count+1]))
   concat=recur(arr1,count+1,concat_val,check_sum)
   
   return add==1 or mul==1 or concat==1

for i in range(len(arr)):
   check=recur(arr[i][1],0,arr[i][1][0],arr[i][0])
   if(check==1):
       sum+=arr[i][0]
print(sum)