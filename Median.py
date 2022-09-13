class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A,B=nums1,nums2
        if len(A)>len(B):
            A,B=B,A
        total=len(A)+len(B)
        half=total//2
        l=0
        r=len(A)-1
        
        
        while(True):
            i=(l+r)//2 #index of A
            j=half-i-2 #index of B
            Aleft=A[i] if i>=0 else float("-infinity")
            Aright=A[i+1] if (i+1) <len(A) else float("infinity") 
            Bleft=B[j] if j>=0 else float("-infinity")
            Bright=B[j+1] if (j+1)<len(B) else float("infinity")
            #check if the partition is true
            if Aleft<=Bright and Bleft<=Aright:
                #partition is correct 
                if total%2:
                    #odd
                    return min(Aright,Bright)
                else:
                    return (max(Aleft,Bleft)+min(Aright,Bright))/2
            elif Aleft>Bright:
                #the B should be extended
                r=i-1
            else:
                #A should be extended
                l=i+1
            