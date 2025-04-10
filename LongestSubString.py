import numpy as np

def naive_solution(s):
    if s =="":
                
        return 0
    if len(s)==1:
        return 1
    substring_vals={}
    longest=""
    temp=""
    for i in range(0,len(s)):
        for j in range(i,len(s)):
            if s[j] not in substring_vals:
                substring_vals[s[j]]=1
                temp=temp+s[j]
            else:
                if len(longest)<len(temp):
                    longest=temp
                temp=""
                substring_vals={}
                break
    
            
    return len(longest)

def sliding_window(s):
    if s=="":
        return 0
    if s==" ":
        return 1
    l=r=0
    dict={}
    temp=""
    longest=""
    while r <= len(s)-1:
        if s[r] not in dict:
            dict[s[r]]=r
            r=r+1
            temp=s[l:r]
        else:
                temp=s[l:r-1]
                if len(temp)>len(longest):
                    longest=temp
                l=dict[s[r]]+1
                dict[s[r]]=r
        if len(longest)<len(temp):
            longest=temp
    print(dict)
    return len(longest)





"""
Given a string s, find the length of the longest substring without repeating characters.
"""
def longest(s):
    
    #slidig window + hashing
    left = 0 
    right = 0
    longest = 0

    for i, ch in s:
        seens = {}
        if ch not in seens:
            seens[ch] = i
            longest = max(longest, right - left + 1)
        else:
            left = max (left, seens[ch] + 1)
    return longest
            
        
"""
 Longest Substring with At Most Two Distinct Characters

"""

def longest_two(s):

    left = 0
    right = 0
    longest = 0
    seen = {} #values index, count
    for i, ch in enumerate(s): 
      
        if ch not in seen:
            seen[ch] = np.array([i, 1])
            right = i + 1
        else: 
            count = seen[ch][1]
            print(count)
            if count >= 2:
                longest = max (longest, right - left)
                left = max(left, seen[ch][0] + 1)
            else:
                seen[ch][1] += 1
            right = i + 1

    
    longest = max (longest, (right - left ))      
    return longest
"""


Problem Statement:
Given a string s and an integer k, find the length of the longest substring where every character appears at least k times.

Examples:

Input: s = "aaabb", k = 3
Output: 3
Explanation: The longest substring is "aaa", where 'a' repeats 3 times.

Input: s = "ababbc", k = 2
Output: 5
Explanation: The longest substring is "ababb", where 'a' appears 2 times and 'b' appears 3 times.
"""
            
def longest_distinct (s,k):
    longest = 0
    seen = {}
    left = 0
    right = 0
    for ch in s:
        seen.get(ch, 0) + 1
        
        

    





