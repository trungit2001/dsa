[1422. Maximum Score After Splitting a String](https://leetcode.com/problems/maximum-score-after-splitting-a-string)

Given a string `s` of zeros and one, *return the maximum score after splitting the string into two **non-empty** substrings* (i.e **left** substring and **right** substring).

The score after splitting a string is the number of **zeros** in the **left** substring plus 
the number of **ones** in the **right** substring.

<p>&nbsp;</p>

**Example 1:**

> **Input:** s = "011101" <br>
> **Output:** 5 <br>
> **Explanation:** <br>
> All possible ways of splitting s into two non-empty substrings are: <br>
> left = "0" and right = "11101", score = 1 + 4 = 5 <br>
> left = "01" and right = "1101", score = 1 + 3 = 4 <br>
> left = "011" and right = "101", score = 1 + 2 = 3 <br>
> left = "0111" and right = "01", score = 1 + 1 = 2 <br>
> left = "01110" and right = "1", score = 2 + 1 = 3 <br>

**Example 2:**

> **Input:** s = "00111" <br>
> **Output:** 5 <br>
> **Explanation:** When left = "00" and right = "111", we get the maximum score = 2 + 3 = 5

**Example 3:**

> **Input:** s = "1111" <br>
> **Output:** 3 <br>

<p>&nbsp;</p>

**Constraints:**

- `2 <= s.length <= 500`
- The string `s` consists of characters `'0'` and `'1'` only.
