class Solution {

    public String encode(List<String> strs) {
        String enc = "";

        for (String s : strs) {
            enc += s.length() + "#" + s;
        }

        return enc;
    }

    public List<String> decode(String str) {
        ArrayList<String> ans = new ArrayList<>();

        int i = 0;

        while (i < str.length()) {

            int j = i;

            while (str.charAt(j) != '#') {
                j++;
            }

            int len = Integer.parseInt(str.substring(i, j));

            int start = j + 1;
            int end = start + len;

            ans.add(str.substring(start, end));

            i = end;
        }

        return ans;
    }
}