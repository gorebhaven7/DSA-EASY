# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def path(self,root,l,ans):
        
        if root is None:
            return
        else:
            l.append(str(root.val))
        
        if root.left is None and root.right is None:
            s = "->"
            s = s.join(l)
            ans.append(s)
            l.pop()
            return
            
        self.path(root.left,l,ans)
        self.path(root.right,l,ans)
        l.pop()
    
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        l = []
        ans = []
        self.path(root,l,ans)
        return ans