def check(s):
    symbol={"(":0, ")":0, "{":0, "}":0, "[":0, "]":0}
    slist=[*s]
    for item in slist:
        symbol[item]+=1
    if symbol["("]!=symbol[")"]:
        return False
    if symbol["["]!=symbol["]"]:
        return False
    if symbol["{"]!=symbol["}"]:
        return False
    return True
print(check("())"))

# wont work for this "([)]" soulution is stack
#solution Push and Pop and the stack should be empty till the end 