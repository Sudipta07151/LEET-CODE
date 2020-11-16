arr=[1,8,6,2,5,4,8,3,7]

def maxWater(arr):
    lPTR=0
    rPTR=len(arr)-1
    maxWater=0
    while(lPTR<rPTR):
        maxWater=max(maxWater,min(arr[lPTR],arr[rPTR])*(rPTR-lPTR))
        if arr[lPTR]<arr[rPTR]:
            lPTR=lPTR+1
        else:
            rPTR=rPTR-1
    return maxWater


result =maxWater(arr)
print(result)