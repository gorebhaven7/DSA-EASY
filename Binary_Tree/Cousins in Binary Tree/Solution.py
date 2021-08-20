# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def check(self,root,x,y,l,depth,prev):
        
        if root is None:
            return
        
        if root.val == x or root.val == y:
            li = []
            li.append(prev.val)
            li.append(depth)
            l.append(li)
            
        self.check(root.left,x,y,l,depth+1,root)
        self.check(root.right,x,y,l,depth+1,root)
    
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        
        ans = []
        self.check(root,x,y,ans,0,root)
        if ans[0][0] != ans[1][0] and ans[0][1] == ans[1][1]:
            return True
        else:
            return False
        