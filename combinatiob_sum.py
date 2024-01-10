#combination sum: given array of distinct values and target value, find all unique combinations in array where the numbers sum to target value.
from functools import reduce
candidates = [2,3,6,7]
target = 7
result = []
j = 0
subres = []

