- Link:- https://leetcode.com/problems/3sum/

### 3Sum

Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Notice that the solution set must not contain duplicate triplets.

```
Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]

Example 2:

Input: nums = []
Output: []

Example 3:

Input: nums = [0]
Output: []


Constraints:

    0 <= nums.length <= 3000
    -105 <= nums[i] <= 105

```

### Approach

_After sorting the array, for every element in array i will find every eligible pair such that then all three are added their sum is 0, to find the pairs i am following 2 pointer approach._
