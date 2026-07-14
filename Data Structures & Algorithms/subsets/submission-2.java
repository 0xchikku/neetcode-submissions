// time - O(n x 2^n), space - O(n x 2^n)
class Solution {
    List<List<Integer>> output = new ArrayList<>();
    List<Integer> subset = new ArrayList<>();

    public List<List<Integer>> subsets(int[] nums) {
        backtrack(0, nums);
        return output;
    }

    public void backtrack(int index, int[] nums) {
        if (index == nums.length) {
            output.add(new ArrayList<>(subset));
            return;
        }

        subset.add(nums[index]);
        backtrack(index+1, nums);
        subset.remove(subset.size() - 1);
        backtrack(index+1, nums);
    }
}