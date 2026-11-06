class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 1: 
            return n
        i = 0
        j = 1
        cnt = 1
        counts = set()
        nums.sort()
        # print("nums: ", nums)
        while i < n and j < n:
            #if j == n:
            #    i += 1
            #   j = i + 1
            cur = nums[i]
            nex = nums[j]
            # print("current vs next: ", cur, nex)
            if nex == cur + 1:
                cnt += 1
                # print("count: ", cnt)
                i = j
                j = i+1
            elif cur == nex:
                i = j
                j = i+1
            else:
                counts.add(cnt)
                # print("counts: ", counts)
                cnt = 1
                i += 1
                j += 1
        counts.add(cnt)
        return max(counts)