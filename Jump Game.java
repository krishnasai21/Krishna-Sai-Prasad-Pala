class Solution {
  public boolean canJump(int[] nums) {
    int n = nums.length;

    // max position one could reach 
    // starting from index <= i
    int maxPos = nums[0];

    for (int i = 1; i < n; ++i) {
      // if one could't reach this point
      if (maxPos < i) {
        return false;
      }
      maxPos = Math.max(maxPos, nums[i] + i);
    }
    return true;
  }
}