arr=[1,2,3,4,11,33,44,11,11,55,10,23,11]
arr.sort()
print(arr)

def firstlastelpos(arr,target):
    f_left=0
    f_right=len(arr)-1
    while f_left<=f_right:
        first_mid=(f_left+f_right)//2
        if arr[first_mid]==target:
            if first_mid==0 or arr[first_mid-1]!=target:
                break
            f_right=first_mid-1
        elif arr[first_mid]>target:
            f_right=first_mid-1
        else:
            f_left=first_mid+1
    
    e_left=0
    e_right=len(arr)-1
    while e_left<=e_right:
        last_mid=(e_left+e_right)//2
        if arr[last_mid]==target:
            if last_mid==len(arr)-1 or arr[last_mid+1]!=target:
                break
            e_left=last_mid+1
        elif arr[last_mid]>target:
            e_right=last_mid-1
        else:
            e_left=last_mid+1
    return (first_mid,last_mid)

result=firstlastelpos(arr,11)
print(result)

