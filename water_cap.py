"""

Given an array height of length n, where each element represents a vertical line at  position i, find two lines that, together with the x-axis, form a container that holds the most water.
Return the maximum amount of water the container can store.

Example:
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The lines at positions 1 (height=8) and 8 (height=7) form the container with the most water (width=7, height=7 → area=49).
"""

def bforce(arr):
    max_cap = 0

    for i in range(len(arr)):
        for j in range(len(arr)): 
            height = min(arr[i], arr[j])
            width = j - i 
            cap = height * width
            max_cap = max(max_cap, cap)

            
    return max_cap


def maxArea(height):
    left, right = 0, len(height) - 1
    max_area = 0
    
    while left < right:
        width = right - left
        current_height = min(height[left], height[right])
        max_area = max(max_area, width * current_height)
        
        # Move the pointer with the smaller height
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    
    return max_area



print(maxArea([1,8,6,2,5,4,8,3,7]))

