class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        chars_s = list(s)
        charcount = len(chars_s)
        chars_t = []

        for char in t:
            if len(chars_s) == 0:
                return False

            if char in chars_s:
                chars_t.append(char)
                chars_s.remove(char)

        if len(chars_t) == charcount and len(chars_s) == 0:
            return True
        else:
            return False
        