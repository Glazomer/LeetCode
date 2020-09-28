class Solution:
  def threeSum(self, nums: List[int]) -> List[List[int]]:
    result = set()
    c = Counter(nums)
    nums = [[key] * (val if val < 3 else 3) for key, val in c.most_common()]
    nums = [item for sublist in nums for item in sublist]
    for i in range(len(nums)):
      n1 = nums[i]
      c[n1] -= 1
      for j in range(i+1,len(nums)):
        n2 = nums[j]
        n3 = -(n1 + n2)
        c[n2] -= 1
        if n3 in c and c[n3] > 0:
          numbs = [str(n1), str(n2), str(n3)]
          numbs.sort()
          result.add(','.join(numbs))
        c[n2] += 1
    print(nums)
    return [map(lambda n: int(n), s.split(',')) for s in result]