#User function Template for python3

class Solution:
    def countElements(self,N,A):
        # print(max(A))
        if N==0 or N==1:
            return 0
        #code here
        hashmap = {}
        sum = 0
        for i in A:
            if i in hashmap.keys():
                hashmap[i]=hashmap[i]+1
                sum+=1
            else:
                hashmap[i] = 0
        
        
        minn = min(A)
        maxx = max(A)
        return maxx-minn-N+1+sum

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        N=int(input())
        A=list(map(int,input().strip().split()))
        ob=Solution()
        print(ob.countElements(N,A))
# } Driver Code Ends