from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_cnt = Counter(list(s))
        t_cnt = Counter(list(t))
        if s_cnt == t_cnt:
            return True
        return False