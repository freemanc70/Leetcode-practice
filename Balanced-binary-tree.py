class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class solution(object):
    """
    type root: a tree node
    rtype: boolean
    """
    def isBalanced(self, root):
        
        return (self.getHeight(root) >=0)
    
    def getHeight(self, root):
        
        if root is None:
            return 0
        
        left_height, right_height = self.getHeight(root.left), self.getHeight(root.right)
        if abs(left_height - right_height) > 1:
            return -1
        return max(left_height, right_height) +1
        
        
        
if __name__ == "__main__":
    root = TreeNode(0)
    root.left = TreeNode(1)
    root.right = TreeNode(3)
    root.left.left = TreeNode(2)
    root.left.left.left = TreeNode(1)
    result = solution().isBalanced(root)
    print result
