int removeDuplicates(int* nums, int numsSize) {
    // Special case
    if (numsSize == 0) {
        return 0;
    } else if (numsSize == 1) {
        return 1;
    }

    // Normal case
    int len = 1;

    // Iterate through the array, the first number is unique by far
    for (int i = 1; i < numsSize; i++) {
        // If current number is different from last unique number
        if (nums[i] != nums[len - 1]) {
            // Increase unique numbers count and update new discovered unique
            // number
            nums[len] = nums[i];
            len++;
        }
    }
    return len;
}