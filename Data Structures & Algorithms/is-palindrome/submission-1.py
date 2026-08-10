class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower()
        s = ''.join(char for char in s if char.isalnum())
        my_list= list(s)
        my_list.reverse()
        if my_list==list(s):
            return True
        else:
            return False