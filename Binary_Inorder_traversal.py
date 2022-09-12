#Given a root of a binary tree, Return the inorder traversal of its node values
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        left=root.left
        right=root.right
        print(self.inorderTraversal(left))
        print(root.value)
        print(self.inorderTraversal(right))

