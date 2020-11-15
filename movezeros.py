arr=[1,4,0,23,0,5,6,0,11,0]
print(arr)
j=0
for num in arr:
    if num!=0:
        arr[j]=num
        j=j+1
for i in range(j,len(arr)):
        arr[i]=0
print(arr)
