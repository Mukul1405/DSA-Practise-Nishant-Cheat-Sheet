import queue

class Solution:
    def findAnagrams(self, s: str, p: str):
        hashmapString = {}
        hashmap = {}

        for i in p:
            if i not in hashmap.keys():
                hashmap[i] = 1
            else:
                hashmap[i]=hashmap[i]+1

        j = len(p)
        for i in range(j):
            if s[i] in hashmapString.keys():
                hashmapString[s[i]]=hashmapString[s[i]]+1
            else:
                hashmapString[s[i]]=1
        i=0
        j=j-1
        outputList = []
        print("1st hashmap is",hashmapString)
        while(j<len(s)):
            if hashmap == hashmapString:
               outputList.append(i)
            print("element poped is ",s[i],hashmapString[s[i]])
            if hashmapString[s[i]]>1:
                hashmapString[s[i]] = hashmapString[s[i]]-1
            else:
                hashmapString.pop(s[i])
            i+=1
            j+=1
            if j >= len(s):
                return outputList
            print("current hashmap is ",hashmapString)
            print("s[j] is ",s[j])
            if s[j] in hashmapString.keys():
                hashmapString[s[j]]=hashmapString[s[j]]+1
            else:
                hashmapString[s[j]]=1
            print(i, j, hashmapString, outputList)
        return outputList


s = Solution()
print(s.findAnagrams("aaaaaaaaaa","aaaaaaaaaaaaa"))