[2381. Shifting Letters II](https://leetcode.com/problems/shifting-letters-ii)

You are given a string `s` of lowercase English letters and a 2D integer array `shifts` where <code>shifts[i] = [start<sub>i</sub>, end<sub>i</sub>, direction<sub>i</sub>]</code>. For every `i`, **shift** the characters in `s` from the index <code>start<sub>i</sub></code> to the index <code>end<sub>i</sub></code> (**inclusive**) forward if <code>direction<sub>i</sub> = 1</code>, or shift the characters backward if <code>direction<sub>i</sub> = 0</code>.

Shifting a character **forward** means replacing it with the **next** letter in the alphabet (wrapping around so that `'z'` becomes `'a'`). Similarly, shifting a character **backward** means replacing it with the **previous** letter in the alphabet (wrapping around so that `'a'` becomes `'z'`).

Return *the final string after all such shifts to* `s` *are applied*.

<p>&nbsp;</p>

**Example 1:**

> **Input:** s = "abc", shifts = [[0,1,0],[1,2,1],[0,2,1]] <br>
> **Output:** "ace" <br>
> **Explanation:** Firstly, shift the characters from index 0 to index 1 backward. Now s = "zac". <br>
> Secondly, shift the characters from index 1 to index 2 forward. Now s = "zbd". <br>
> Finally, shift the characters from index 0 to index 2 forward. Now s = "ace".

**Example 2:**

> **Input:** s = "dztz", shifts = [[0,0,0],[1,1,1]] <br>
> **Output:** "catz" <br>
> **Explanation:** Firstly, shift the characters from index 0 to index 0 backward. Now s = "cztz". <br>
> Finally, shift the characters from index 1 to index 1 forward. Now s = "catz".

<p>&nbsp;</p>

**Constraints:**

- <code>1 <= s.length, shifts.length <= 5 * 10<sup>4</sup></code>
- `shifts[i].length == 3`
- <code>0 <= start<sub>i</sub> <= end<sub>i</sub> < s.length</code>
- <code>0 <= direction<sub>i</sub> <= 1</code>
- `s` consists of lowercase English letters.
