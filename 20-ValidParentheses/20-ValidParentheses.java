// Last updated: 8/2/2025, 4:54:18 PM
class Solution {
    public boolean isValid(String s) {
        char[] chars = s.toCharArray();
        Stack<Character> res = new Stack<>();
        Map<Character, Character> map = new HashMap<>();
        map.put(')', '(');
        map.put(']', '[');
        map.put('}', '{');
        for (Character c : chars) {
            if (map.containsKey(c)) {
                if (res.isEmpty()) {
                    return false;
                }
                if (res.peek().equals(map.get(c))) {
                    res.pop();
                } else {
                    return false;
                }
            } else {
                res.push(c);
            }
        }
        return res.size() == 0;
    }
}
