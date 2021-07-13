class Solution {
    public int[] solution(int[] lottos, int[] win_nums) {
        int[] ranks={6,6,5,4,3,2,1}; // 순위 메기기
        
        int count=0;
        int correct=0;
        int max_result,min_result;
        
        for(int i=0;i<6;i++){ //0의 갯수 구하기, 당첨번호 일치여부 확인
            if(lottos[i]==0){
                count++;
                continue;
            } 
            for(int j=0;j<6;j++)
                if(lottos[i]==win_nums[j]) correct++;    
        }
        
        int[] answer = {ranks[count+correct],ranks[correct]};
        return answer;
    }
}