class Solution {
    public boolean solution(String str) {
        boolean answer = true;
        
        if (str.length() == 4 || str.length() == 6) { // 길이 체크
            for (int i = 0; i < str.length(); i++) {
                if (!Character.isDigit(str.charAt(i))) {
                // isDigit 은 지정한 문자가 숫자인지 확인해주는 메소드.
                    answer = false;
                }
            }
        } else {
            answer = false;
        }
        return answer;
    }
}