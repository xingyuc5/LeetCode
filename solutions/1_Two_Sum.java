class Solution {
    public int[] twoSum(int[] nums, int target) {

        int[] results = new int[2];

        // Key: target - number
        // Value: index of number
        HashMap map = new HashMap<Integer, Integer>();

        for (int i = 0; i < nums.length; i++) {
            int temp = target - nums[i];

            if (!map.containsKey(temp)) {
                map.put(nums[i], i);
            } else {
                results[0] = (int) map.get(temp);
                results[1] = (int) i;
                return results;
            }
        }
        return results;
    }
}