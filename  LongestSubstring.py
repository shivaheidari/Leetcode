"""

Given a string s and an integer k, return the length of the longest substring that contains at most k distinct characters.

Example 1:
Input: s = "eceba", k = 2
Output: 3


"""

def longest(s,k):

    #shrink: hash len (hash) <= k ow: shrink from left
    #expand: len(hash) 
    #distinct: hash len (hash) <= k ow: shrink from left
    dist = {}
    longest = 0
    i = j = 0
   
    while j < len(s):
        chr = s[j]
        dist[chr] = dist.get(chr, 0) + 1
        j += 1
        
        #shrink
        while len(dist) > k:
            left_chr = s[i]
            dist[left_chr] -= 1
            if dist[left_chr] == 0:
                del dist[left_chr]
            i += 1
        longest = max (longest, j - i)
    return longest

print(longest("aaabcd", 2))
