class Solution {
    public long[] solution(int x, int n) {
        long tot = x;
		long[] answer = new long[n];
        
        for (long i = 0; i < n; i++) {
			answer[(int)i] = tot;
			tot += x;
		}
        
        return answer;
    }
}