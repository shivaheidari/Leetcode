def check(s):
<<<<<<< HEAD
    push_l=["(","{","["]
    pop_l=[")","}","]"]
    slist=[*s]
    print(slist)
    stack=[]
    for item in slist:
        print(item)
        if item in push_l:
            stack.append(item)
            print("appended",item)
        else:
            if stack==[]:
                return False
            index=pop_l.index(item)
            pattern=push_l[index]
            out=stack.pop()
            if out !=pattern:
                return False
            
    if stack==[]:
        return True
    else:
        return False
            

    
print(check("(]"))
=======
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
>>>>>>> master
