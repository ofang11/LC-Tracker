// Last updated: 8/2/2025, 4:53:53 PM
class Solution {
    public boolean containsDuplicate(int[] nums) {
        Map<Integer, Integer> numMap = new HashMap<Integer, Integer>();
        for (int i = 0; i < nums.length; i++) {
            if (numMap.containsKey(nums[i])) {
                return true;
            } else {
                numMap.put(nums[i], 1);
            }
        }
        return false;
    }
}