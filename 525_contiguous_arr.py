class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        # Replace 0s with -1s
        for i in range(len(nums)):
            if nums[i] == 0:
                nums[i] = -1
        
        sum_index = {0: -1}
        max_len = 0
        cumulative_sum = 0
        
        for i in range(len(nums)):
            cumulative_sum += nums[i]
            
            if cumulative_sum in sum_index:
                max_len = max(max_len, i - sum_index[cumulative_sum])
            else:
                sum_index[cumulative_sum] = i
        print(sum_index)
        return max_len
