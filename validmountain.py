arr=[1,2,3,6,7,2,1]

def validMountain(arr):
    i=1
    while i<len(arr) and arr[i]>arr[i-1]:
        i=i+1
    if i==1 or i==len(arr):
        return False
    while i<len(arr) and arr[i]<arr[i-1]:
        i=i+1
    return i==len(arr)

result=validMountain(arr)
print(result)