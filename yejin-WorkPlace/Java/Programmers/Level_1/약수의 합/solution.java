class Solution {
    public int solution(int num) {
        int answer = 0;
		
		for (int i = 1; i <= num; i++) {
			int result = num / i;
			if (result * i == num) {
				answer += result;
			}
		}
        return answer;
    }
}