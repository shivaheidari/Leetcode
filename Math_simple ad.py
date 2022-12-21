class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        result=digits[-1]+1
        if result<10:
            digits[-1]=result
            return digits
        i=len(digits)-1
        while (result>=10):
            digits[i]=result-10
            i-=1
            result=digits[i]+1
            if i>=0:
                digits[i]=result
            else:
                digits.insert(0,result)
        return digits