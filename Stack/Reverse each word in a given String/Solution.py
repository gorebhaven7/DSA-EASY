class Solution:
    def reverseWords(self, s):
        # code here
        self.stack = []
        output = ""
        for e in s:
            if e != '.':
                self.stack.append(e)
            else:
                while(len(self.stack) != 0):
                    output += self.stack.pop()
                output += "."
        
        while(len(self.stack) != 0):
            output += self.stack.pop()        
        
        return output

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        s = input().strip()
        ob = Solution()
        ans = ob.reverseWords(s)
        print(ans)
# } Driver Code Ends