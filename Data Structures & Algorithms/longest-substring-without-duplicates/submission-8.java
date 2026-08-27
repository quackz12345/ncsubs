class Solution {
    public int lengthOfLongestSubstring(String s) {
        int curr = 0, left = 0, ans = 0;
        HashSet<Character> d = new HashSet<>();
        for(int right = 0; right<s.length(); right++){
            if(d.contains(s.charAt(right))){
                
                while(s.charAt(left)!=s.charAt(right)){
                    d.remove(s.charAt(left));
                    left++;
                    
                }
                left++;
                
            }else{
                d.add(s.charAt(right));
            }
            ans = Math.max(ans, right-left+1);
        }
        return ans;
    }
}
