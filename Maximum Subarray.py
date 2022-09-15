class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        current=0
        max_sub=nums[0]
        for n in nums:
            if current<0:
                current=0
            current+=n
            max_sub=max(current,max_sub)
        return max_sub