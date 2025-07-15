#leetcode most accurate answer
class Solution(object):
    def twoSum(self, nums, target):
       
        sec = dict()
        for ind,num in enumerate(nums):
            if target-num not in sec:
                sec[num]=ind
                continue
            return [ind, sec[target-num]]
        
    #test case written by cahtgpt    
def test_two_sum():
    sol = Solution()
    
    test_cases = [
        # Format: (nums, target, expected indices - order doesn't matter)
        ([2, 7, 11, 15], 9, [0, 1]),
        ([3, 2, 4], 6, [1, 2]),
        ([3, 3], 6, [0, 1]),
        ([1, 2, 3, 4], 5, [2, 1]),  # 3 + 2 = 5
        ([0, 4, 3, 0], 0, [0, 3]),
        ([1, 5, 1], 2, [0, 2]),
        ([1, 5, 3, 8], 13, [3, 1]),  # 8 + 5
        ([5, 75, 25], 100, [2, 1]),
        ([1, 2], 3, [1, 0]),
    ]

    passed = 0
    for i, (nums, target, expected) in enumerate(test_cases):
        result = sol.twoSum(nums, target)
        if sorted(result) == sorted(expected):
            print(f"✅ Test {i+1} passed. Output: {result}")
            passed += 1
        else:
            print(f"❌ Test {i+1} failed. Output: {result}, Expected: {expected}")

    print(f"\n{passed}/{len(test_cases)} tests passed.")

test_two_sum()