arr=[1,4,2,23,87,5,6,7,11]
arr.sort()
print(arr)
target=100
def binarySearch(arr,target):
    s=0
    e=len(arr)-1
    m=(s+e)//2
    while s<=e:
        m=(s+e)//2
        if arr[m]==target:
            return m
        elif arr[m]<target:
            s=m+1
        elif arr[m]>target:
            e=m-1
    return -1    

result=binarySearch(arr,target)

if result!=-1:
    print("Element is present in index {}".format(result))
else:
    print("Element is not foumd")