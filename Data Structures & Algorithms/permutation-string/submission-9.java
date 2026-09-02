
class Solution {
    public boolean checkInclusion(String s1, String s2) {

        if (s1.length() > s2.length())
            return false;

        // SCHEMA 1:
        // Build the target frequency map
        HashMap<Character, Integer> target = new HashMap<>();

        for (int i = 0; i < s1.length(); i++) {
            char c = s1.charAt(i);
            target.put(c, target.getOrDefault(c, 0) + 1);
        }


        // SCHEMA 2:
        // Create a sliding window
        HashMap<Character, Integer> window = new HashMap<>();

        int left = 0;

        for (int right = 0; right < s2.length(); right++) {

            // Add the new right character
            char c = s2.charAt(right);
            window.put(c, window.getOrDefault(c, 0) + 1);


            // SCHEMA 3:
            // If window gets too big, shrink from left
            if (right - left + 1 > s1.length()) {

                char leftChar = s2.charAt(left);

                window.put(
                    leftChar,
                    window.get(leftChar) - 1
                );

                // IMPORTANT:
                // remove zero-count entries so HashMap.equals() works
                if (window.get(leftChar) == 0)
                    window.remove(leftChar);

                left++;
            }


            // SCHEMA 4:
            // Once window is correct size,
            // check whether frequencies match
            if (target.equals(window))
                return true;
        }

        return false;
    }
}