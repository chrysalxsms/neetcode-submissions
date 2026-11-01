class Solution:

    def encode(self, strs: List[str]) -> str:
        # start with a nr representing the length of the string
        # followed by a separator (e.g. '#')
        # then the string
        enc = ""
        for s in strs:
            enc += str(len(s)) + 'é' + s
            # print(enc)
        return enc

    def decode(self, s: str) -> List[str]:
        dec = []
        i = 0
        while i < len(s):
            lnth = ""
            # print("i: ", i)
            while s[i] != 'é':
                lnth += s[i]
                i += 1
            if s[i] == 'é':
                # print("found é")
                n = int(lnth)
                dec.append(s[i+1:i+n+1])
                # print(dec)
                i += n+1
        return dec