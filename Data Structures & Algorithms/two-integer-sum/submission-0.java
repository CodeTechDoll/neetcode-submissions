class Solution {
    public int[] twoSum(int[] nums, int target) {
        Hashtable<Integer, Integer> set = new Hashtable();
        int cur = -1;
        int tar = -1;
        for(int i = 0; i < nums.length; i++) {
            cur = nums[i];
            tar = target - cur;
            if (set.containsKey(tar) && set.get(tar) != i) {
                return new int[]{set.get(tar), i};
            } else {
                set.put(cur, i);
            }
        }
        
        return new int[]{cur,tar};
    }
}
