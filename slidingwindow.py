arr=[1,4,2,23,8,5,6,71,11]

def maxWindowSum(arr,windowSize):
    if len(arr)<windowSize:
        print("WINDOW-SIZE IS GREATER THAN ARRAY SIZE----invalid operation!!!")
        return -1
    windowSum=sum(arr[i] for i in range(windowSize))
    maxSum=windowSum
    for i in range(len(arr)-windowSize):
        windowSum=windowSum-arr[i]+arr[i+windowSize]
        maxSum=max(windowSum,maxSum)
    return maxSum


result=maxWindowSum(arr,2)

if(result!=-1):
    print("max sum of windowsize 2 is {} ".format(result))

