"""
Given an array of daily temperatures temperatures, return an array answer where answer[i] is the number of days you have to wait after the 
i-th day to get a warmer temperature. 
If no future day is warmer, let answer[i] = 0.

Example:
Input: temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
Output: [1, 1, 4, 2, 1, 1, 0, 0]

"""

def dailytemp(nums):
    temps = []
    for i in range(0,len(nums)):
         print(i)
         j = i + 1
         current = nums[i]
         deltat = 0
         while (j<len(nums)):
              print(i, j)
              nday = nums[j]
              if nday > current:
                   deltat = j - i
                   break
              j += 1
         temps.append(deltat)
   

    return temps

def daily_stack(nums):
     stack = []
     answers = [0] * len(nums)

     for i in range(len(nums)):
          while stack and nums[i] > nums[stack[-1]]:
               j = stack.pop()
               answers[j] = i - j
          stack.append(i)
     return answers
 
print(dailytemp([73, 74, 75, 71, 69, 72, 76, 73]))
print(daily_stack([73, 74, 75, 71, 69, 72, 76, 73]))
