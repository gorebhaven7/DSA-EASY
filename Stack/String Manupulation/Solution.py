class Solution:
    def removeAdj(self,v,n):
        # Your code goes here
        stack = []
        for e in v:
            if len(stack) == 0:
                stack.append(e)
            else:
                top = stack[-1]
                if top == e:
                    stack.pop()
                else:
                    stack.append(e)
        
        return len(stack)
    

#{ 
#  Driver Code Starts


if __name__=='__main__':
    tcs=int(input())

    for _ in range(tcs):
        n=int(input())
        v=[x for x in input().split()]
        ob = Solution()
        print(ob.removeAdj(v,n))
# } Driver Code Ends