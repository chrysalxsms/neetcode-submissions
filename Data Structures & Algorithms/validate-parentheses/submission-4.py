class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 0:
            return True
        if len(s) % 2 != 0:
            return False
        stack = []
        pairs = {')':'(','}':'{',']':'['}
        for i in s:
            if i in {'(','{','['}:
                stack.append(i)
            elif i in {')', '}', ']'}:
                if stack and pairs[i] == stack[-1]:
                    stack.pop()
                else:
                    return False
        if not stack:
            return True
        return False