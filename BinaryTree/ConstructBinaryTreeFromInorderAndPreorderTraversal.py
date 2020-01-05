#https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/

"""
Given preorder and inorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.

For example, given

preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]
Return the following binary tree:

    3
   / \
  9  20
    /  \
   15   7

"""

#Solution: The root node is always in the beginning of preorder list.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    rootIdx = 0
    map = {}
    
    def buildTree(self, preorder, inorder):
        def helper(inLeft, inRight):
            if inLeft > inRight:
                return None

            node = TreeNode(preorder[self.rootIdx])
            self.rootIdx += 1
            index = self.map[node.val]

            node.left = helper(inLeft, index - 1)
            node.right = helper(index + 1, inRight)

            return node

        for i, val in enumerate(inorder):
            self.map[val] = i

        return helper(0, len(preorder) - 1)
