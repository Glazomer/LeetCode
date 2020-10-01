class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = set()
        nums.sort()

        num = nums[0] if nums else 0
        inRow = 1
        last = 0
        for n in nums:
            if not (num == n and inRow > 3):
                nums[last] = n
                last += 1
                inRow = inRow + 1 if num == n else 1
                num = n

        nums = nums[:last]

        for i in range(len(nums)):
            t = -nums[i]  # target
            l = 0
            r = len(nums) - 1
            while l < r:
                if l == i or nums[l] + nums[r] < t:
                    l += 1
                elif r == i or nums[l] + nums[r] > t:
                    r -= 1
                else:
                    result.add(tuple(sorted([nums[l], nums[r], -t])))
                    l += 1
                    r -= 1

        return result
