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
    if k == 0:
        return 0
    unique_chrs = len(set(s))
    if k >= unique_chrs:
        return len(s)
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


"""
Define i (left) and j (right) clearly.

Decide if j is inclusive or exclusive.

Shrink before expanding.

Ensure the window is valid before growing.

Update results inside the loop.

Avoid missing the last valid window.

Handle edge cases early (k=0, k ≥ unique chars).

Use hash maps (dict/defaultdict) for frequency tracking.

Decrement counts before deleting keys.

Test with simple cases first ("aab", k=1).

Helps catch off-by-one errors.

"""