class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = set()
        nums.sort()

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            for j in range(i+1, len(nums)):
                l, r = j+1, len(nums)-1
                while l < r:
                    cur = nums[i]+nums[j]+nums[l]+nums[r]
                    if cur == target:
                        ans.add((nums[i], nums[j], nums[l], nums[r]))
                        l += 1
                    if cur > target:
                        r -= 1
                    if cur < target:
                        l += 1
        return ans
