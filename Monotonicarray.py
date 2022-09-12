class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        dec_monotonic=0
        As_monotonic=0
        for i in range(0,len(nums)-1):
            print(i)
            if(nums[i]>=nums[i+1]):
                dec_monotonic+=1
            if(nums[i]<=nums[i+1]):
                As_monotonic+=1
        if (dec_monotonic==len(nums)-1 or As_monotonic==len(nums)-1 ):
            return True
        else:
            return False 