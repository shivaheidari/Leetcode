"""
The array contains elements in a known range (e.g., 1 to n).

Minimizing writes is critical (e.g., flash memory with limited write cycles).


"""



def cycle_sort(nums):
    #number of swap occur to check
    i = 0
    j = 1
    swap = 1
    while i <= len(nums):
        
        while swap != 0:
            swap = 0
            greater = 0
            smaller = 0
            idx = i+1
            while idx <= len(nums)-1:
                if nums[idx] >= nums[i]:
                    greater += 1
                else:
                    smaller += 1
                idx += 1

            #swap
            if smaller !=0:
                swap_idx = len(nums) - smaller 
                val = nums[swap_idx]
                nums[swap_idx] = nums[i]
                nums[i] = val 
                swap += 1
        i += 1  
        j += i 
    return nums

print(cycle_sort([3, 1, 2, 5, 4]))

