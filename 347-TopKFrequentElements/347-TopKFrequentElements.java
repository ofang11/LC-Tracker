// Last updated: 8/2/2025, 4:53:42 PM
class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        Map<Integer, Integer> counts = new HashMap<>();
        for (int num : nums) {
            counts.put(num, counts.getOrDefault(num, 0) + 1);
        }

        List<int[]> sortedCounts = new ArrayList<>();
        for (int key : counts.keySet()) {
            sortedCounts.add(new int[] {counts.get(key), key});
        }
        sortedCounts.sort((a, b) -> Integer.compare(b[0], a[0]));

        int[] res = new int[k];

        for (int i = 0; i < k; i++) {
            res[i] = sortedCounts.get(i)[1];
        }
        return res;
    }
}