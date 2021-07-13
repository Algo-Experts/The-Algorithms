import java.util.*;

class Solution {
    public int solution(int[] nums) {
        int a=nums.length/2;
        
        ArrayList<Integer> b=new ArrayList<>();
        
        for(int i=0;i<nums.length;i++)
            if(!b.contains(nums[i]))
                b.add(nums[i]);
        
        if(b.size()>=a)
            return a;
        else return b.size();
    }
}