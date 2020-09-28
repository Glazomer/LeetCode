class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = set()
        c = Counter(nums)
        nums = [[k] * (v if v < 3 else 3) for k, v in c.most_common()]
        nums = [n for subl in nums for n in subl]
        nums.sort()

        _l = 0
        _r = len(nums) - 1
        for i in range(len(nums)):
            t = -nums[i]  # target
            l = _l
            r = _r
            while l < r:
                if l == i or nums[l] + nums[r] < t:
                    l += 1
                elif r == i or nums[l] + nums[r] > t:
                    r -= 1
                else:
                    result.add(tuple(sorted([nums[l], nums[r], nums[i]])))
                    l += 1
                    r -= 1

        return result
