def isLongPressedName(name: str, typed: str):
    i,j = 0,0
    while(i<len(name) and j<len(typed)):
        print(name[i],typed[j])
        if name[i] == typed[j]:
            i+=1        
            j+=1
        else:
            i-=1
            # print(i)
            if i<0 or j<0:
                return False
            if name[i]!= typed[j]:
                return False
            else:
                i+=1
                j+=1
    if i != len(name) and j == len(typed):
        return False
    while(j<len(typed)):
        if name[i-1] == typed[j]:
            j+=1
        else:
            return False

    return True

name = "alexad"
typed = "alexaaaa"
print(isLongPressedName(name,typed))
