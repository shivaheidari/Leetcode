def romanToInt(s: str):
        val_dict={"I":1 ,"V":5,"X":10,"L":50,"C":100,"D":500, "M":1000}
        s_list=list(s)
        # print("list://",s_list)
        summation=0
        for i in range(0,len(s_list)):
            if i<len(s_list)-1:
                val=val_dict[s_list[i]]
                val_n=val_dict[s_list[i+1]]
                if val<val_n:
                 val=-(val)
            else: val=val_dict[s_list[i]]
            summation+=val
        return summation

print(romanToInt("VI"))