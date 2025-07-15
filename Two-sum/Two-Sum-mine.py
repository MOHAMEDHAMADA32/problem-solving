class Solution:
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            y = target - nums[i]
            if y in nums and nums.index(y) != i:
                return [i, nums.index(y)]


sol = Solution()

#  Test Cases by chatgpt
test_cases = [
    # Format: (nums, target, expected output [indices])
    ([2, 7, 11, 15], 9, [0, 1]),
    ([3, 2, 4], 6, [1, 2]),
    ([3, 3], 6, [0, 1]),
    ([1, 5, 3, 4], 6, [1, 2]),
    ([0, 4, 3, 0], 0, [0, 3]),
]


for i, (nums, target, expected) in enumerate(test_cases):
    result = sol.twoSum(nums, target)
    print(f"Test Case {i+1}: {'Passed' if sorted(result) == sorted(expected) else 'Failed'} — Output: {result}, Expected: {expected}")

