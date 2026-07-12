class Solution {
    private List<Integer> subset = new ArrayList<>();
    private List<List<Integer>> output = new ArrayList<>();

    public List<List<Integer>> subsets(int[] nums) {
        backtrack(nums, 0);
        return output;
    }

    private void backtrack(int[] nums, int index) {
        if (index == nums.length) {
            output.add(new ArrayList<>(subset));
            return;
        }

        subset.add(nums[index]);
        backtrack(nums, index + 1);
        subset.remove(subset.size() - 1);
        backtrack(nums, index + 1);
    }
}