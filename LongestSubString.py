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
print(sliding_window("abcc"))












