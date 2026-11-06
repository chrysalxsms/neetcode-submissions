class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s) <= 1:
            return True
        s = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
        print(s)
        n = len(s)
        l = s[:n//2]
        print(l)
        if n % 2 == 0:
            r = s[n//2:][::-1]
            print(r)
        else:
            r = s[n//2+1:][::-1]
            print(r)
        if l != r:
            return False
        return True