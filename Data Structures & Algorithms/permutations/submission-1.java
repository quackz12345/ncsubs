class Solution {
    public List<List<Integer>> permute(int[] nums) {
        ArrayList<List<Integer>> perms = new ArrayList<List<Integer>>();
        ArrayList<Integer> list = new ArrayList<>(nums.length);
        for (int i = 0; i < nums.length; i++) {
            list.add(-11);
        }
        permuter(nums, list, perms);
        return perms;
    }
    public void permuter(int[] nums, ArrayList<Integer> curr, ArrayList<List<Integer>> perms) {
        if (curr.indexOf(-11) < 0)
                perms.add(curr);
        for (int n : nums) {
            if (curr.indexOf(n) < 0) {
                ArrayList<Integer> burr = new ArrayList<>(curr);
                burr.set(burr.indexOf(-11), n);
                permuter(nums, burr, perms);
            }
        }
    }
}
