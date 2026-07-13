class Solution {
    // time - O(n^(t/m)), space - O(t/m) - t is target and m is min value in candidates, n is length of candidates
    private List<List<Integer>> output = new ArrayList<>();
    private List<Integer> combination = new ArrayList<>();

    private void backtrack(int index, int[] candidates, int remaining) {
        if (remaining == 0) {
            output.add(new ArrayList<>(combination));
            return;
        }
        for (int i = index; i < candidates.length; i++) {
            int diff = remaining - candidates[i];
            if (diff < 0) {
                break;
            }
            combination.add(candidates[i]);
            backtrack(i, candidates, diff);
            combination.remove(combination.size() - 1);
        }

    }

    public List<List<Integer>> combinationSum(int[] candidates, int target) {
        Arrays.sort(candidates);
        backtrack(0, candidates, target);
        return output;
    }
}