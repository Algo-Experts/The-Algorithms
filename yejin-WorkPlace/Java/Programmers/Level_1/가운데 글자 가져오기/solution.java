class Solution {
    public String solution(String str) {
        String answer = "";
		
		
		if (str.length() % 2 == 0) {
			answer = Character.toString(str.charAt((str.length() / 2) - 1)) 
				+ Character.toString(str.charAt(str.length() / 2));
		} else {
			answer = Character.toString(str.charAt(str.length() / 2));
		}
        return answer;
    }
}