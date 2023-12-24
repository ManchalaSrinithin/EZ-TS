# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result=[]
        def order(root):
            if root is not None:
                result.append(root.val)
                order(root.left)
                order(root.right)
        order(root)
        return result
        