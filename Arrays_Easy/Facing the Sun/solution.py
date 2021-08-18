class Solution:
    
    def countBuildings(self,h, n):
        # code here
        maxx,count = 0,0
        for e in h:
            if e > maxx:
                count += 1
                maxx = e
        
        return count

#{ 
#  Driver Code Starts
#Initial Template for Python 3





if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        h = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.countBuildings(h, n)
        print(ans)
        tc -= 1

# } Driver Code Ends