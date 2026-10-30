class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}      # dict for counts
        freq = [[] for i in range(len(nums)+1)]
        
        for num in nums:
            count[num] = 1 + count.get(num, 0) # returns 0 if num not in count
        for num, cnt in count.items(): # tupels of length 2
            freq[cnt].append(num)
        
        res = []
        for i in range(len(freq) -1, 0, -1): # we don't have to touch index 0, always empty (minimum count value is 1)
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res