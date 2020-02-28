int maxSubArray(int* nums, int numsSize) {
    int results = nums[0], sum = 0;

    for (int i = 0; i < numsSize; i++) {
        if (sum < 0) {
            sum = nums[i];
        } else {
            sum += nums[i];
        }
        results = results < sum ? sum : results;
    }
    return results;
}