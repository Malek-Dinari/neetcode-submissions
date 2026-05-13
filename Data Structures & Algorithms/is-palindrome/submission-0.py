class Solution:
    def isPalindrome(self, s: str) -> bool:
        # 1. Clean the string: remove non-alphanumeric and make lowercase
        clean_s = "".join(char.lower() for char in s if char.isalnum())
        
        # 2. Compare the string with its reverse using slicing
        return clean_s == clean_s[::-1]