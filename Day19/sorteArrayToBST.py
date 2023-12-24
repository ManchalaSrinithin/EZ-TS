# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        low=0
        high=len(nums)-1
        def binarysearchTree(low,high):
            if low>high:
                return None
                mid=(low+high)//2
                root=TreeNode(nums[mid])
                root.left=binarysearchTree(low,mid-1)
                root.right=binarysearchTree(mid+1,high)
                return root
        return binarysearchTree(low,high)