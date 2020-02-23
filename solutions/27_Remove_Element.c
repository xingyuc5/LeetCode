

int removeElement(int* nums, int numsSize, int val) {
    // Keep track of index of the updated array
    int counter = 0;

    for (int i = 0; i < numsSize; i++) {
        // Copy element to index of final array only if it is not equal to val
        if (nums[i] != val) {
            nums[counter] = nums[i];
            counter++;
        }
    }
    return counter;
}