# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        stack = [root]
        ans = 0

        while stack:
            node = stack.pop()
            if not node:
                continue
            if (node.val >= p.val and node.val <= q.val) or node.val <= p.val and node.val >= q.val:
                return node
            elif node.val > p.val:
                stack.append(node.left)
            else:
                stack.append(node.right)

        return None