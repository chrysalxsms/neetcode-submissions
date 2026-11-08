class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()     # lets us skip duplicates easily
                        # ensures that moving l or r pointer will
                        # increase or decrease the sum 
                        # in a predictable way
        print(nums)
        # for each fixed number a, we place two pointers
        for i in range(len(nums)):
            a = nums[i]
            if a > 0:
                break
            if i > 0 and a == nums[i-1]:
                continue
            l = i + 1
            r = len(nums) - 1
            while l < r:
                threeSum = a + nums[l] + nums[r]
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    res.append([a, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while nums[l] == nums[l-1] and l < r:
                        l += 1
        return res