class Solution:
    def bulbSwitch(self, n: int) -> int:
        if n==0:
            return 0
        return int(floor(sqrt(n)))
        # for i in range(2,n+1):
        #     if math.isqrt(i) ** 2 == i:
        #         perfect_sq+=1
        # return perfect_sq