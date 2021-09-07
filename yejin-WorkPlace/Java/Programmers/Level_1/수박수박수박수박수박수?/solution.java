class Solution {
    public String solution(int num) {
        String answer = "";
		
		for (int i = 1; i <= num; i++) {
			answer += i % 2 == 0 ? "박" : "수";
		}
        return answer;
    }
}