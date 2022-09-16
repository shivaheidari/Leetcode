#Given two strings s and t, return true if s is a subsequence of t, or false otherwise.
#s="abc", t="ahbgdc" return True
#current=-1 if it doensnt exitst
def find_sub(s,t,memo={}):
    if len(s)==1 and s[0] not in memo:
        exist=0
        for i in range(0,len(t)):
            if s==t[i]:
                exist=1
                memo[s]=i
        if exist==1:
            return True
        else: return False
    if s in memo:
        return memo[s]

    else:
        left=find_sub(s[0:len(s)-1],t,memo)
        current=find-sub(s[-1])
        if current and left<current:
            memo[s]=current
            return True
        else:
            return False
print(find_sub("x","abc"))
