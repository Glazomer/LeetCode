class Solution:
  def maxArea(self, h: List[int]) -> int:
    # Here, instead of trying to do N^2 brute force, we go smart way
    # We search for the highest peak from side were we have lowest peak.
    # If for example left peak is higher than right, we want to find same hight or more peak on right, so we have possibility to beat our result.
    # When we search the higher peak, we hope that length decreasing (r - l) if gonna be beaten by peak growth 
    # (h[l] or h[r] will be much greater than lMax or rMax respectivly)
    res = 0
    l, r = 0, len(h) - 1
    lMax = rMax = 0
    while l < r:
      lMax = max(h[l], lMax)
      rMax = max(h[r], rMax)
      res = max(min(h[l],h[r]) * (r - l), res)
      if rMax > lMax:
        l += 1
      else:
        r -= 1
        
    return res
    # To be honest, I just got that solution in the head somehow...
