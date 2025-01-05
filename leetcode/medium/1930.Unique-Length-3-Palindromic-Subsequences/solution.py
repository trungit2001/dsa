class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        # return sum([len(set(s[s.index(letter)+1:s.rindex(letter)])) for letter in set(s)])
        n, ans = len(s), 0
        for w in set(s):
            left = s.index(w)
            right = s.rindex(w)
            ans += len(set(s[left+1:right]))
        return ans


sol = Solution()
print(sol.countPalindromicSubsequence('aabca'))  # 3
print(sol.countPalindromicSubsequence('adc'))  # 0
print(sol.countPalindromicSubsequence('bbcbaba'))  # 4
