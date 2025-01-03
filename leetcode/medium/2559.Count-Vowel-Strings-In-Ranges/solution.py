from typing import List


class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        VOWEL = set('aeiou')
        prefix_sum = []
        cnt = 0

        for w in words:
            if w[0] in VOWEL and w[-1] in VOWEL:
                cnt += 1
            prefix_sum.append(cnt)

        ans = []
        for l, r in queries:
            ans.append(
                prefix_sum[r] - (l if l == 0 else prefix_sum[l - 1])
            )
        return ans


sol = Solution()
print(sol.vowelStrings(['aba','bcb','ece','aa','e'], [[0,2],[1,4],[1,1]])) # [2,3,0]
print(sol.vowelStrings(['a','e','i'], [[0,2],[0,1],[2,2]])) # [3,2,1]
