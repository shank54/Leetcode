class Solution(object):
    def isPalindrome(self, s):
        s = ''.join(e for e in s if e.isalnum()).lower()
        a = s[::-1]
        if a==s:
            return True
        else:
            return False