


def naive_longestPalindrome(s):
        longest=""
        for i in range(0,len(s)):
            
            for j in range(i,len(s)):
             
                sr=s[i:j+1]
               
                reverse=sr[::-1]
                if sr==reverse and len(sr)>len(longest):
                      longest=sr  
        return longest   
                
                   

                
def longestPalindrome(s):
    
    res=""
    reslen=0
    for i in range(len(s)):
        print(i)
        l,r =i,i

        #for odd lenght
        while l>=0 and r<len(s) and s[l]==s[r]:
            if (r-l+1)>reslen:
                res=s[l:r+1]
                reslen=len(res)
            l-=1
            r+=1
        #for even length
        l,r=i,i+1
        while l>=0 and r<len(s) and s[l]==s[r]:
            if (r-l+1)>reslen:
                res=s[l:r+1]
                reslen=len(res)
            l-=1
            r+=1

    return res





print(longestPalindrome("abba"))



       




