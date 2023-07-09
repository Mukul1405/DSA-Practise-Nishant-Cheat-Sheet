class Solution:
    def isIsomorphic(self, s: str, t: str):
        hashmap1 = {}
        hashmap2 = {}

        for i in s:
            if i in hashmap1.keys():
                hashmap1[i]=hashmap1[i]+1
            else:
                hashmap1[i]=1

        for i in t:
            if i in hashmap2.keys():
                hashmap2[i]=hashmap2[i]+1
            else:
                hashmap2[i]=1
        if hashmap1 == hashmap2:
            return False

        list1 = []
        list2 = []
        for i in hashmap1.values():
            list1.append(i)
        for i in hashmap2.values():
            list2.append(i)
        hashmap1 = {}
        hashmap2 = {}
        list1.sort()
        list2.sort()
        if list1 == list2:
            return True
        else:
            return False

s=Solution()
s1 = "bbbaaaba"
t = "aaabbbba"
print(s.isIsomorphic(s1,t))