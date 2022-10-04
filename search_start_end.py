def find_st(nums,target):     
        start=-1
        end=-1
        if nums==0 or target=="":
            
            return [start,end]
        head=0
        tail=len(nums)
        while start==-1 and 0<=head<tail<len(nums):
            
            mid=(tail-head)//2

            if nums[mid]==target:
                start=mid

            elif nums[mid]>target:
                    tail=mid-1
            else:
                    head=mid+1
        if start!=-1:
            for i in range(head,tail):
                if nums[i]==target:
                    end=i
        return [start,end]

print(find_st([2,2],2))