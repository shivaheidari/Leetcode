class Solution:
    def myPow(self, x: float, n: int) -> float:
       if n==0:
           return 1
       if n==1:
           return x
       posn=abs(n)
       if posn % 2 == 0:
            result=self.myPow(x,posn/2)
            final=result*result
       else:
            result =self.myPow(x,(posn-1)/2)
            final=result*result*x
       if n>0:
            return final
       else:
            return 1/final
