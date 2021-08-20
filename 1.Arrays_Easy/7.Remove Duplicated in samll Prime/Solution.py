class Solution:
    def removeDuplicates(self, arr):
        # code here 
        d = [0]*100
        ans = []
        for e in arr:
            if d[e] == 0:
                ans.append(e)
                d[e] = 1
        
        return ans

#{ 
#  Driver Code Starts
if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        res = Solution().removeDuplicates(arr)
        for i in range(len(res)):
            print(res[i], end=" ")
        print('')


# } Driver Code Ends