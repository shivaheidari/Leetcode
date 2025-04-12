"""
The array contains elements in a known range (e.g., 1 to n).

Minimizing writes is critical (e.g., flash memory with limited write cycles).


"""


def cycle_sort(nums):
    n = len(nums)
    
    for cycle_start in range(n - 1):
        item = nums[cycle_start]
        
        # Find the correct position for `item`
        pos = cycle_start
        for i in range(cycle_start + 1, n):
            if nums[i] < item:
                pos += 1
        
        # Skip if already in place
        if pos == cycle_start:
            continue
        
        # Handle duplicates
        while item == nums[pos]:
            pos += 1
        nums[pos], item = item, nums[pos]
        
        # Rotate the rest of the cycle
        while pos != cycle_start:
            pos = cycle_start
            for i in range(cycle_start + 1, n):
                if nums[i] < item:
                    pos += 1
            while item == nums[pos]:
                pos += 1
            nums[pos], item = item, nums[pos]
    
    return nums


def test():
    print(cycle_sort(([1,2,5,0, 6,8])))
    assert cycle_sort([1,2,5,0, 6,8]) == [0,1,2,5,6,8]
    assert cycle_sort([5,2,1,3]) == [1,2,3,5] 

print(test())