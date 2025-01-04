[2270. Number of Ways to Split Array](https://leetcode.com/problems/number-of-ways-to-split-array/)

You are given a **0-indexed** integer array `nums` of length `n`.

`nums` contains a **valid split** at index `i` if the following are true:

- The sum of the first `i + 1` elements is **greater than or equal to** the sum of the last `n - i - 1` elements.

- There is **at least one** element to the right of `i`. That is, `0 <= i < n - 1`.

Return *the number of **valid splits** in* `nums`.

<p>&nbsp;</p>

**Example 1:**

> **Input:** nums = [10,4,-8,7] <br>
> **Output:** 2 <br>
> **Explanation:** <br>
> There are three ways of splitting nums into two non-empty parts: <br>
> - Split nums at index 0. Then, the first part is [10], and its sum is 10. The second part is [4,-8,7], and its sum is 3. Since 10 >= 3, i = 0 is a valid split.
> - Split nums at index 1. Then, the first part is [10,4], and its sum is 14. The second part is [-8,7], and its sum is -1. Since 14 >= -1, i = 1 is a valid split.
> - Split nums at index 2. Then, the first part is [10,4,-8], and its sum is 6. The second part is [7], and its sum is 7. Since 6 < 7, i = 2 is not a valid split.
> Thus, the number of valid splits in nums is 2.

**Example 2:**

> **Input:** nums = [2,3,1,0] <br>
> **Output:** 2 <br>
> **Explanation:** <br>
> There are two valid splits in nums: <br>
> - Split nums at index 1. Then, the first part is [2,3], and its sum is 5. The second part is [1,0], and its sum is 1. Since 5 >= 1, i = 1 is a valid split.
> - Split nums at index 2. Then, the first part is [2,3,1], and its sum is 6. The second part is [0], and its sum is 0. Since 6 >= 0, i = 2 is a valid split.

<p>&nbsp;</p>

**Constraints:**

- <code>2 <= nums.length <= 10<sup>5</sup></code>
- <code>-10<sup>5</sup> <= nums[i] <= 10<sup>5</sup></code>
