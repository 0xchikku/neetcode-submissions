// time - O(2^n × n), space O(k x n)
class Solution {
    List<List<Integer>> output = new ArrayList<>();
    List<Integer> combination = new ArrayList<>();

    public List<List<Integer>> combinationSum2(int[] candidates, int target) {
        Arrays.sort(candidates);
        backtrack(0, target, candidates);
        return output;
    }

    public void backtrack(int index, int remaining, int[] candidates) {
        if (remaining == 0) {
            output.add(new ArrayList<>(combination));
            return;
        }

        for (int i = index; i < candidates.length; i++) {
            int value = candidates[i];
            if (value > remaining) {
                break;
            }
            if (i > index && candidates[i - 1] == candidates[i]) {
                continue;
            }
            combination.add(value);
            backtrack(i + 1, remaining - value, candidates);
            combination.remove(combination.size() - 1);
        }
    }
}