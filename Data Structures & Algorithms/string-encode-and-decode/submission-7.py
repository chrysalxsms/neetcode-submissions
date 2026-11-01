class Solution:

    def encode(self, strs: List[str]) -> str:
        # start with a nr representing the length of the string
        # followed by a separator (e.g. '#')
        # then the string
        enc = ""
        for s in strs:
            enc += str(len(s)) + "#" + s
            # print(enc)
        return enc

    def decode(self, s: str) -> List[str]:
        dec = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            i = j + 1
            j = i + length
            dec.append(s[i:j])
            i = j
        return dec