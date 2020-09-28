class Solution:
  def threeSum(self, nums: List[int]) -> List[List[int]]:
    result = set()
    c = Counter(nums)
    nums = []
    for k, v in c.most_common():
      nums.extend([k, k] if v > 1 else [k])
      
    for i, n1 in enumerate(nums):
      c[n1] -= 1
      for n2 in nums[i+1:]:
        n3 = -(n1 + n2)
        c[n2] -= 1
        if n3 in c and c[n3] > 0:
          numbs = tuple(sorted([n1, n2, n3]))
          result.add(numbs)
        c[n2] += 1
    print(nums)
    return result