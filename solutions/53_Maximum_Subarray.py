class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        # Initialize
        result = nums[0]
        sum = 0

        for num in nums:

            # If previous sum < 0, we dont want to add it to current subarray
            # but restart a new subarray from current number
            if sum > 0:
                sum += num
            else:
                sum = num

            # Update result
            result = max(result, sum)
        return result
