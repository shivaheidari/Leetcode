"""
Given a sorted integer array nums, remove duplicates in-place such that duplicates appear at most twice (allow two occurrences of each element). Return the new length 
of the array.
Example:
Input: nums = [1,1,1,2,2,3]
Output: 5 (because nums = [1,1,2,2,3,_...]; first 5 elements are valid).
"""

def InplaceRmv(nums):
    if not nums:
        return 0
    i = 0  
    count = 1 
    
    for j in range(1, len(nums)):
        if nums[j] == nums[j - 1]:
            count += 1
        else:
            count = 1 
        
        if count <= 2:
            nums[i] = nums[j]
            i += 1
    
    return i

# Test Cases
print(InplaceRmv([1, 1, 1, 2, 2, 3]))         
print(InplaceRmv([1, 1, 1, 2, 2, 3, 3, 3])) 