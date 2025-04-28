"""

Given a circular integer array nums (where the next element of nums[nums.length - 1] is nums[0]), return the next greater number for every element. If no greater number exists, use -1.

Examples:

Input: nums = [1,2,1]
Output: [2,-1,2]
Explanation: The first 1's next greater is 2; the 2 has no greater, and the last 1 wraps around to 2.

Input: nums = [5,4,3,2,1]
Output: [-1,5,5,5,5]
Explanation: Each element searches the circular array to find the next greater


"""

def bf_greater(nums):
    
    lenght = len(nums)
    results = [-1] * lenght
    for i in range(0, lenght):
        current = nums[i]
        j = (i + 1) % lenght
        while j != i:
            next_val = nums[j]
            if next_val > current:
                results[i] = next_val
                break
            j = (j + 1) % lenght
    #loop
    return results


def opt_greater(nums):
    lenght = len(nums)
    results = [-1]  * lenght
    stack = []
    for i in range(2* lenght):

        while stack and nums[stack[-1]] < nums[i % lenght]:
            j = stack.pop()
            results[j] = nums[i % lenght]

        if i < lenght: #first round
            stack.append(i)
    
    return results
        



print(bf_greater([5,4,3,2,1]))
print(opt_greater([5,4,3,2,1]))
