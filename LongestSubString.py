def solution(s):
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

print(solution(""))