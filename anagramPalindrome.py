
def anagramPalindrome(string):
    hashmap = {}
    for i in string:
        if i in hashmap.keys():
            hashmap[i] = hashmap[i]+1
        else:
            hashmap[i]=1

    for i in hashmap.values():
        if i%2 != 0:
            return False
    return True

string = "geeksgeeks"
print(anagramPalindrome(string))