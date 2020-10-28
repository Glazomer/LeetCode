class Solution:
  def trap(self, h: List[int]) -> int:
    res = passed = maxV = last = 0
    for i, v in enumerate(h):
      if v > maxV:
        res += passed
        passed = 0
        last = i
        maxV = v
      else:
        passed += maxV - v
        
    passed = maxV = 0
    for i, v in enumerate(h[::-1]):
      if i >= len(h) - last:
        break
      elif v >= maxV:
        res += passed
        passed = 0
        maxV = v
      else:
        passed += maxV - v
    
    return res
