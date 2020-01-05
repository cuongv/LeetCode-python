#https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/

"""
Given inorder and postorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.

For example, given

inorder = [9,3,15,20,7]
postorder = [9,15,7,20,3]
Return the following binary tree:

    3
   / \
  9  20
    /  \
   15   7   

#Solution: The root node is always in the end of postorder list.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
"""

class Solution(object):
    def buildTree(self, inorder, postorder):
        def helper(inLeft, inRight):
            if inLeft > inRight:
                return None
            node = TreeNode(postorder.pop())
            index = map[node.val]
            node.right = helper(index + 1, inRight)
            node.left = helper(inLeft, index - 1)
            return node

        map = {}
        for i, val in enumerate(inorder):
            map[val] = i
        return helper(0, len(postorder) - 1)
       
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
###################################################################

    """
    #My naive solution :(
    def buildTree(self, inorder, postorder):
        if not inorder:
            return None
        if len(inorder) == 1:
            return TreeNode(inorder[0])
        
        root = TreeNode(postorder[-1])
        
        leftNodes = []
        rightNodes = []
        postLeftNodes = []
        postRightNodes = []
        
        isLeft = True 
        
        mapIdx = {}
        for i, val in enumerate(inorder):
            if val == root.val:
                isLeft = False
            elif isLeft:
                leftNodes.append(val)    
            else:
                rightNodes.append(val)
                
            mapIdx[val] = i
                
        for val in postorder:
            if val == root.val:
                continue
            if mapIdx[val] < mapIdx[root.val]:
                postLeftNodes.append(val)
            else:
                postRightNodes.append(val)
                
        root.left = self.buildTree(leftNodes, postLeftNodes) 
        root.right = self.buildTree(rightNodes, postRightNodes) 
        
        return root
        """
