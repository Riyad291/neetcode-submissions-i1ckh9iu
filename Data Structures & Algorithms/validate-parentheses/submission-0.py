class Solution:
    def isValid(self, s: str) -> bool:
       
        Map = {")": "(", "]": "[", "}": "{"}
        stack = []

        for char in s:

            if char in Map:
                
                top_element = stack.pop() if stack else '#'
                
                
                if Map[char] != top_element:
                    return False
            else:
              
                stack.append(char)

        return not stack