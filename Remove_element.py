# input : num: list
# out put : k: the umber of elements which are not equal to val
# inplace : yes

def removeElement(num_list, val):
    k = 0
    i=0
    j = len(num_list)-1
    print(j)
    while i <= j:
       if num_list[i] == val: 
        var = num_list[j]
        num_list[j] = num_list[i]
        num_list[i] = var
        j -= 1
       else:
        i += 1
        k += 1   
    print(num_list)
    return k
   
num_list = [3,4,3,1,2,3]
val = 3

print(removeElement(num_list, val))