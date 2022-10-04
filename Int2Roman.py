def int2roman(nums):
   result=""
   keys=[1000,900,500,400,100,90,50,40,10,9,5,4,1]
   vals=["M","CM","D","CD","C","XC","L","XL","X","IX","V","IV","I"]
   
   for i in range(0,len(keys)):
        while(nums>=keys[i]):
            nums-=keys[i]
            result+=vals[i]
    

   
   return result

print(int2roman(3))