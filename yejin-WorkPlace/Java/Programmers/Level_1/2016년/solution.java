class Solution {
    public String solution(int month, int day) {
        int[] monthDay = {31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};
		String[] dayArr = {"FRI", "SAT", "SUN", "MON", "TUE", "WED", "THU"};
		
		String answer = "";
		
		int diff = day - 1;
		
		for (int i = 1; i < month; i++) {
			diff += monthDay[i - 1];
		}
        return answer = dayArr[diff % 7];
    }
}