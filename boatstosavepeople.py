arr=[1,3,4,2,5,4,3,1,5,3]


def boatsRequired(arr,limitOfBoat):
    arr.sort()
    print(arr)
    start=0
    end=len(arr)-1
    no_of_boats=0
    while start<=end:
        if(start==end):
            no_of_boats=no_of_boats+1
        elif start+end<=limitOfBoat:
            start=start+1
            end=end-1
            no_of_boats=no_of_boats+1
        else:
            no_of_boats=no_of_boats+1
            end=end-1
    return no_of_boats

result=boatsRequired(arr,5)

print(result)