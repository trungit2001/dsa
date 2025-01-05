from typing import List


class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        n = len(s)
        diff = [0] * n
        for start, end, direct in shifts:
            if direct:
                diff[start] += 1
                if end + 1 < n:
                    diff[end + 1] -= 1
            else:
                diff[start] -= 1
                if end + 1 < n:
                    diff[end + 1] += 1
        ans = list(s)
        nos = 0
        for i in range(n):
            nos = (nos + diff[i]) % 26
            nos = nos + 26 if nos < 0 else nos
            ans[i] = chr((ord(ans[i]) - 97 + nos) % 26 + 97)
        return ''.join(ans)


sol = Solution()
print(sol.shiftingLetters('abc', [[0,1,0],[1,2,1],[0,2,1]]))  # 'ace'
print(sol.shiftingLetters('dztz', [[0,0,0],[1,1,1]]))  # 'catz'
