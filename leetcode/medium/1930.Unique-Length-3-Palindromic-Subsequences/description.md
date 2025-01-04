[1930. Unique Length 3 Palindromic Subsequences](https://leetcode.com/problems/unique-length-3-palindromic-subsequences)

Given a string `s`, return *the number of **unique palindromes of length three** that are a **subsequence** of* `s`.

Note that even if there are multiple ways to obtain the same subsequence, it is still only counted **once**.

A **palindromes** is a string that reads the same forwards and backwards.

A **subsequence** of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.

- For example, `"ace"` is a subsequence of <code>"<u>a</u>b<u>c</u>d<u>e</u>"</code>.

<p>&nbsp;</p>

**Example 1:**

> **Input:** s = "aabca" <br>
> **Output:** 3 <br>
> **Explanation:** The 3 palindromic subsequences of length 3 are:
> - "aba" (subsequence of "<u>a</u><u>a</u>bc<u>a</u>")
> - "aaa" (subsequence of "<u>a</u><u>a</u>bc<u>a</u>")
> - "aca" (subsequence of "<u>a</u>ab<u>c</u><u>a</u>")

**Example 2:**

> **Input:** s = "adc" <br>
> **Output:** 0 <br>
> **Explanation:** There are no palindromic subsequences of length 3 in "adc".

**Example 3:**

> **Input:** s = "bbcbaba" <br>
> **Output:** 4 <br>
> **Explanation:** The 4 palindromic subsequences of length 3 are: <br>
> - "bbb" (subsequence of "<u>bb</u>c<u>b</u>aba")
> - "bcb" (subsequence of "<u>b</u>b<u>cb</u>aba")
> - "bab" (subsequence of "<u>b</u>bcb<u>ab</u>a")
> - "aba" (subsequence of "bbcb<u>aba</u>")

<p>&nbsp;</p>

**Constraints:**

- <code>3 <= s.length <= 10<sup>5</sup></code>
- `s` consists of only lowercase English letters.
