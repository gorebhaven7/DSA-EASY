# Your task is to complete this function

class Solution:
    # function should return an integer denoting the required answer
    def evalTree(self, root):
        # Code here
        if root is None:
            return
        
        if root.left is None and root.right is None:
            return int(root.data)
        
        left_ans = self.evalTree(root.left)
        right_ans = self.evalTree(root.right)
        
        if root.data == '+' :
            return left_ans + right_ans
        elif root.data == '-' :
            return left_ans - right_ans
        elif root.data == '*' :
            return left_ans * right_ans
        else:
            return int(left_ans/right_ans)

#{ 
#  Driver Code Starts
class node:
    def __init__(self, value):
        self.left = None
        self.data = value
        self.right = None

def isExp(s):
    if s=="+" or s=="-" or s=="*" or s=="/":
        return True
    return False

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = input().strip().split()
        q = []
        p = 0
        root = node(arr[p])
        q.append(root)
        p = 1
        while q!=[]:
            f = q.pop(0)
            if isExp(f.data):
                l = node(arr[p])
                p+=1
                r = node(arr[p])
                p+=1
                f.left = l
                f.right = r
                q.append(l)
                q.append(r)
            
        # inorder(root)
        # print ''
        print(Solution().evalTree(root))


# } Driver Code Ends