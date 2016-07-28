__author__ = 'Yaicky'

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        rlt, stack = [], [[root, -1]]

        while stack:
            node, status = stack[-1]
            stack[-1][1] += 1
            if status == -1 and node.left:
                stack.append([node.left, -1])
            elif status == 0 and node.right:
                stack.append([node.right, -1])
            elif status == 1:
                rlt.append(stack.pop()[0].val)
        return rlt
