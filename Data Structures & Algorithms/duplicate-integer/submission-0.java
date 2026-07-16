// time - O(n), space - O(n)
class Solution {
    Set<Integer> seen = new HashSet<>();
    public boolean hasDuplicate(int[] nums) {
        for (int num: nums) {
            if (seen.contains(num)) {
                return true;
            }
            seen.add(num);
        }
        return false;
    }
}