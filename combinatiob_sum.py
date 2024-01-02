#combination sum: given array of distinct values and target value, find all unique combinations in array where the numbers sum to target value.

candidates = [2,3,6,7]
target = 7
result = []
j = 0
for index, value in enumerate(candidates):
    subres = []
    while j<=len(candidates):
        subres.append(candidates[j])
        if sum(subres) == target:
            result.append(subres)
            j = 0
            break
        elif sum(subres) > target:
            j = j+1
            subres = []
        else:
            subres.append(candidates[j])
            j = j+1


print(result)