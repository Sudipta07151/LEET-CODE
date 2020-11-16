str='abafkbacag'

left=0
right=0
ans=0
m={}

while left<len(str) and right<len(str):
    curr_el=str[right]
    if curr_el in m:
        left=max(left,m[curr_el]+1)
    m[curr_el]=right
    ans=max(ans,right-left+1)
    right=right+1

print(ans)   

