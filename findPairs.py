class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        # O(N) O(N)
        result = 0
        c = Counter(nums)
        for n in c:
            if (n - k) in c and (n - k != n or c[n] > 1):
                result += 1
        return result
