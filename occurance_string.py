class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        match=0
        if len(needle)>len(haystack):
            return -1
        for i in range(0,len(needle)):
            # print("i",i)
            for j in range(0,len(haystack)):
                # print("j",j)
                if haystack[j]==needle[i]:
                    match=1
                    k=min(len(needle),len(haystack))
                    # print("k",k)
                    for t in range(1,k):
                        #  ---------------------------------
                        # print(t)
                            if needle[i+t]==haystack[j+t]:
                                    match+=1
                              # print("Match",match)
                    if match==len(needle):
                        return j
                    else:
                         match=0
            return -1

st=Solution()
print(st.strStr("missisissippi","issipi"))
