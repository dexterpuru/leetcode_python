- Link:- https://leetcode.com/problems/longest-substring-without-repeating-characters/

### Longest Substring Without Repeating Characters

Given a string s, find the length of the longest substring without repeating characters.

```
Example:

Input:
s = "abcabcbb"

Output:
3

Explanation:
The answer is "abc", with the length of 3.
```

### Approach

- Following Sliding Window approach
- Using Dictionary to keep count of all letters.
- While doing Sliding Window only increase right to right+1, and the moment we find a repeated letter, we will check the length of substring and move left to left+1 until every element in dictionary has only 1 occurance.
