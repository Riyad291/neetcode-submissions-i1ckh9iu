class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def validate(node, low, high):
            # 1. Base Case: If we reach the end, it's valid so far!
            if not node:
                return True
            
            # 2. The Check: Does the node break the rules?
            # Must be > everything on the left AND < everything on the right
            if node.val <= low or node.val >= high:
                return False
            
            # 3. The Recursive Step: Check both sides
            left_is_valid = validate(node.left, low, node.val)
            right_is_valid = validate(node.right, node.val, high)
            
            # If BOTH sides are true, the whole tree is true
            return left_is_valid and right_is_valid

        # Start with no limits (infinity)
        return validate(root, float('-inf'), float('inf'))