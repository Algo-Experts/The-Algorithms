class Solution {
    public long solution(int price, int money, int count) {
        long answer = 0;
		long tot = 0;
		
		for (int i = 1; i <= count; i++) {
			tot += price * i;
		}
		
		answer = tot > money ? tot - money : 0;

        return answer;
    }
}