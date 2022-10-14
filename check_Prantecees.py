def check(s):
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