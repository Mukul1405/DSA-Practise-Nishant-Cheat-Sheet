def longestSubstring(str):
    l,r=0,0
    maxLength = 1
    s = set()
    while(r<len(str)):
        if str[r] not in s:
            s.add(str[r])
        else:
            while(str[r] in s):
                s.discard(str[l])
                l+=1
        r+=1
        if r - l > maxLength:
            maxLength = r - l
        # print(r,l, maxLength, s)
    return maxLength
str = "ABDEFGABEF"
print(longestSubstring(str))


# Tc - 0(2n) and Sc - 0(n)