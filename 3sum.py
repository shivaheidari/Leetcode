from multiprocessing.dummy import Array


def threeSum( nums):
        
        #making the coupled summation array
        couple=[]
        result=[]
        for i in range(0,len(nums)-1):
                   
            couple.append(nums[i]+nums[i+1])
        print("couple",couple)
        
        #making the results
        for i in range(0,len(nums)):
            summation=0
            if i ==0:
                for j in range(1,len(couple)):
                    print("i0",j)
                    summation=nums[0]+couple[j]
                    if summation ==0:
                        result.append([nums[0],nums[j],nums[j+1]])

            else:
                for j in range(0,len(couple)):
                    if j!=i and j!=i-1:
                        print("1other",j)
                        summation=nums[i]+couple[j]
                        if summation==0:
                            result.append([nums[i],nums[j],nums[j+1]])
        return result

            
          

print(threeSum([1,0,-1]))