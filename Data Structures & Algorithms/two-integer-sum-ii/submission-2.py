from collections import defaultdict
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        d = defaultdict(int)
        for i in range(len(numbers)):
            diff = target - numbers[i]
            if diff in d:
                return [d[diff], i+1]
            d[numbers[i]] = i+1
