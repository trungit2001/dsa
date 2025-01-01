class Solution:
    def maxScore(self, s: str) -> int:
        # return max([s[:idx].count('0') + s[idx:].count('1') for idx in range(1, len(s))])
        _max = 0
        for idx in range(1, len(s)):
            _max = max(_max, s[:idx].count('0') + s[idx:].count('1'))
        return _max


sol = Solution()
print(sol.maxScore('011101')) # 5
print(sol.maxScore('00111')) # 5
print(sol.maxScore('1111')) # 3
