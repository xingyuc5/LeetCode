
class Solution {
    public int removeElement(int[] nums, int val) {
        int counter = 0;

        for (int num : nums) {
            // Copy element to index of final array only if it is not equal to val
            if (num != val) {
                nums[counter] = num;
                counter++;
            }
        }
        return counter;
    }
}