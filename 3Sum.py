class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = set()  # Will save only unique arrays
        # we need to find a + b + c == 0, that is same as a + b == -c, so we will use that to check for -c
        c = Counter(nums)
        nums = []  # Counted all elements and cleaned array
        for k, v in c.most_common():  # Getting number and amount of that number in array
            # Removing more than two occurrences of same number (so will not exceed time limit)
            nums.extend([k, k] if v > 1 else [k])

        for i, n1 in enumerate(nums):  # enumerate returns index, value of list
            c[n1] -= 1  # Removing used numbers from counted nums
            for n2 in nums[i+1:]:
                n3 = -(n1 + n2)
                c[n2] -= 1  # removing used number
                if n3 in c and c[n3] > 0:
                    # sorting and using tuples, so we will have unique result
                    numbs = tuple(sorted([n1, n2, n3]))
                    result.add(numbs)
                # adding back used number, becuase we will use it in further itarations
                c[n2] += 1

        return result  # Python is smart... He will automatically convert set() of tuple() to list() of list()
