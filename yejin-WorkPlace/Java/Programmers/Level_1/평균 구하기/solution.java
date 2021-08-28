class Solution {
    public double solution(int[] arr) {
        int tot = 0;
		Double answer = 0.0;
		
		for (int i = 0; i < arr.length; i++) {
			tot += arr[i];
		}
		
		answer = (double) tot / arr.length;
        return answer;
    }
}