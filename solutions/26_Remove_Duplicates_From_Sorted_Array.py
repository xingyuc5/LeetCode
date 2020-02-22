class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return len(nums)

        nums_distinct = 0
        for num in nums:
            if num != nums[nums_distinct]:
                nums_distinct += 1
                nums[nums_distinct] = num
        return nums_distinct+1
