/**
 * Definition of Interval:
 * public class Interval {
 *     public int start, end;
 *     public Interval(int start, int end) {
 *         this.start = start;
 *         this.end = end;
 *     }
 * }
 */

class Solution {
    public boolean canAttendMeetings(List<Interval> intervals) {
        
        for(int j=0; j<intervals.size();j++){
            for(int i=0; i<intervals.size();i++){
                if(i!=j && ((intervals.get(i).start>=intervals.get(j).start && intervals.get(j).end>intervals.get(i).start) || (intervals.get(i).end>intervals.get(j).start && intervals.get(j).end>=intervals.get(i).end))) 
                return false;
            }
        }
        return true;
    }
}
