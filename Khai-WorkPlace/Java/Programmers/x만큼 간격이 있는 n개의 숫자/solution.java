//함수 solution은 정수 x와 자연수 n을 입력 받아, x부터 시작해 x씩 증가하는 숫자를 n개 지니는 리스트를 리턴해야 합니다.

class Solution {
    public long[] solution(int x, int n) {
        long[] answer = new long[n];
        long temp = x;
                     
        for(int i = 0; i < n; i++){
            answer[i] = temp * (i+1);
        }
            
        return answer;
    }
}