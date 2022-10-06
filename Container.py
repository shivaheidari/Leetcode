def max_container(arr):

    max_cont=0
    l=0
    r=len(arr)-1
    while (l<r):
        area=(r-l)*min(arr[l],arr[r])
        if area>max_cont:
            max_cont=area
        if (arr[r]>=arr[l]):
            l+=1
        else:
            r-=1

    return max_cont


print(max_container([1,1,4])) 