class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        # O(N log N) O(1)
        result = 0
        nums.sort()
        l = r = 0
        while l < len(nums) and r < len(nums):
            if (r < len(nums) - 1 and nums[r] == nums[r+1]) or \
                    nums[r] - nums[l] < k or\
                    l == r:
                r += 1
            elif (l < len(nums) - 1 and nums[l] == nums[l+1] and l + 1 != r) or \
                    nums[r] - nums[l] > k:
                l += 1
            else:
                result += 1
                l += 1
                r += 1
        return result
