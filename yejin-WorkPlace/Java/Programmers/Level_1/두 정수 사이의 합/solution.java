class Solution {
    public long solution(int num1, int num2) {
        long answer = 0;
		
		
		if (num1 > num2) {
			for (int i = num2; i <= num1; i++) {
				answer += i;
			}
		} else {
			for (int i = num1; i <= num2; i++) {
				answer += i;
			}
		}
        return answer;
    }
}