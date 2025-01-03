from typing import List


class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        totals = sum(nums)
        cnt = prefix_sum = 0
        for num in nums[:-1]:
            prefix_sum += num
            cnt += (prefix_sum >= totals - prefix_sum)
        return cnt


sol = Solution()
print(sol.waysToSplitArray([10,4,-8,7]))  # 2
print(sol.waysToSplitArray([2,3,1,0]))  # 2
