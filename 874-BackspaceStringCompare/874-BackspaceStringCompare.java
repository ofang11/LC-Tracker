// Last updated: 8/2/2025, 4:53:24 PM
class Solution {
    public String helper(String str) {
        char[] strArr = str.toCharArray();
        String res = "";

        for(Character c : strArr) {
            if (c.equals('#')) {
                if (res.length() == 0) {
                    continue;
                } else {
                    res = res.substring(0, res.length() - 1);
                }
            } else {
                res += c;
            }
        }
        return res;
    }

    public boolean backspaceCompare(String s, String t) {
        String pS = helper(s);
        String pT = helper(t);

        return pS.equals(pT);
    }
}