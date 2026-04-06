class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1

        while left < right:
            while left < right and not self.is_alphanumeric(s[left]):
                left += 1
            while right > left and not self.is_alphanumeric(s[right]):
                right -= 1
            
            if s[left].lower() != s[right].lower():
                return False
            
            left += 1
            right -= 1
        return True
    
    #manual helper function using ASCII ranges

    def is_alphanumeric(self, char: str) -> bool:
        val = ord(char)
        return (ord('A') <= val <= ord('Z') or
               ord('a') <= val <= ord('z') or
               ord('0') <= val <= ord('9') )