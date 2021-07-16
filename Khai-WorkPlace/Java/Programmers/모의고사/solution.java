import java.util.*;
class Solution {
    public ArrayList<Integer> solution(int[] answers) {
        ArrayList<Integer> answer =new ArrayList<Integer>();
        int[] p1={1,2,3,4,5};
        int[] p2={2,1,2,3,2,4,2,5};
        int[] p3={3,3,1,1,2,2,4,4,5,5};
        
        int count1=0;
        int count2=0;
        int count3=0;
        
        for(int i=0;i<answers.length;i++){
            if(p1[i%5]==answers[i])
                count1++;
            if(p2[i%8]==answers[i])
                count2++;
            if(p3[i%10]==answers[i])
                count3++;
        }
        
        if(count1>count2){
            if(count1>count3){
                answer.add(1);
            }else if(count1==count3){
                answer.add(1);
                answer.add(3);
            }else{
                answer.add(3);
            }
        }else if(count1==count2){
            if(count1>count3){
                answer.add(1);
                answer.add(2);
            }else if(count1==count3){
                answer.add(1);
                answer.add(2);
                answer.add(3);
            }else{
                answer.add(3);
            }
        }else{
            if(count2>count3){
                answer.add(2);
            }else if(count2==count3){
                answer.add(2);
                answer.add(3);
            }else{
                answer.add(3);
            }
        }
        
        return answer;
    }
}