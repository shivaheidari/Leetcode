   
#find diffrent distinct ways 
from http import client

dict={}
def climbStairs(n):
        if(n==1):
            dict[1]=1
            return 1
        if (n==2):
            dict[2]=2
            return 2
        if n not in dict:
              dict[n]=climbStairs(n-1)+climbStairs(n-2)
        print(dict)
        return dict[n]
print(climbStairs(30))