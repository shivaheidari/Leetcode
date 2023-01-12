class Solution:
    op= ["+", "-", "*"]
    def diffWaysToCompute(self, expression: str) -> List[int]:
        res=[]
        if ('+' not in expression) and ("-" not in expression) and ('*' not in expression):
            return [int(expression)]

        else:
            for i,v in enumerate(expression):
                if v in self.op:
                    left_wing = self.diffWaysToCompute(expression[:i])
                    right_wing= self.diffWaysToCompute(expression[i+1:])
                    for left_i, left_v in enumerate(left_wing):
                        for right_i, right_v in enumerate(right_wing):
                            if v == "+":
                                res.append(left_v+right_v)
                            elif v == "-":
                                res.append(left_v-right_v)
                            else:
                                res.append(left_v* right_v)

        return res