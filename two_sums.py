class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        solution_dict = {}
        for i, num in enumerate(nums):
            diff = target - num
            if diff in nums:
                return nums.index(diff), i
