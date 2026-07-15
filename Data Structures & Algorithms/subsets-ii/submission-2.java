// time - O(n * 2^n), space - O(n * 2^n)
class Solution {
    List<List<Integer>> output = new ArrayList<>();
    List<Integer> subset = new ArrayList<>();

    public List<List<Integer>> subsetsWithDup(int[] nums) {
            Arrays.sort(nums);
            backtrack(0, nums);
            return output;
    }

    public void backtrack(int index, int[] nums) {
        output.add(new ArrayList<>(subset));
        for (int i = index; i < nums.length; i++) {
            if (i > index && nums[i-1] == nums[i])
                continue;
            subset.add(nums[i]);
            backtrack(i+1, nums);
            subset.remove(subset.size() - 1);
        }
    }
}