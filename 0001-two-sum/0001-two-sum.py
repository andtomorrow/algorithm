class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
          for j in range(1, len(nums)):
            if j == i:
              continue
            else:
              if nums[i] + nums[j] == target:
                return [i, j]
