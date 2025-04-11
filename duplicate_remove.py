"""

Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same.

Return the number of unique elements (k). The first k elements of nums should hold the unique elements. The remaining elements are not important.



"""

def remove_duplicate(nums):
    left = 0
    right = 1
    unique_chars = []
    while right < len(nums)-1:
        print(left, right)
        unique_chars.append (nums[left])
        print(unique_chars)
        while nums[left] == nums[right] and right < len(nums)-1:
            right += 1
        left += 1
        nums [left] = nums[right]
    return unique_chars
        
print(remove_duplicate([1,1,1,2,2,3,4,4,4]))
        
