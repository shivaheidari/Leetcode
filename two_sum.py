import numpy as np

"""
Given an array of integers nums and an integer target, return the indices of the two numbers such that they add up to target.


"""
def TwoSum(x, target):

    node_map = {}
    result = []
    for i, val in enumerate(x):
        compelment = target - i 
        if compelment in node_map:
            result.append([node_map[compelment],i])
            

        else:
            node_map[val] = i
    return result

def TwoSum_BF(x,target):

    result = []

    for i in range(len(x)):
        for j in range(i+1, len(x)):
            res = x[i] + x[j]
            if res == target:
                result.append([i,j])
    return result

x = np.array([1, 3, 4, 3, 1])
result = TwoSum(x, 5)
print(result)

