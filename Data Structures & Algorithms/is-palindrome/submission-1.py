class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s) <= 1:
            return True
        s = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
        n = len(s)
        l = s[:n//2]
        if n % 2 == 0:
            r = s[n//2:][::-1]
        else:
            r = s[n//2+1:][::-1]
        if l != r:
            return False
        return True