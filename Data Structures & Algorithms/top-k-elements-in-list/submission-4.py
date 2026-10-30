class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        res = [[] for i in range(n)]
        l = sorted(nums)
        i = 0
        while i < n:
            count = 1
            j=i+1
            while j < n and l[i] == l[j]:
                count += 1
                j += 1
            res[count-1].append(l[i])
            i = j
        freq = []
        for i in range(len(nums)-1, -1, -1):
            if res[i] != 0:
                for x in res[i]:
                    freq.append(x)
            if len(freq) == k:
                return freq