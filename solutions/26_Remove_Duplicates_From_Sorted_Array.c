int removeDuplicates(int* nums, int numsSize) {
    if (numsSize == 0) {
        return 0;
    } else if (numsSize == 1) {
        return 1;
    }

    int len = 1;
    for (int i = 1; i < numsSize; i++) {
        if (nums[i] != nums[len - 1]) {
            nums[len] = nums[i];
            len++;
        }
    }
    return len;
}