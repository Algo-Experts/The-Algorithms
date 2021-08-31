class Solution {
    public String solution(String s) {
        String answer = ""; // retrun 값
        String[] strArr = s.split(""); // 띄어쓰기까지 포함해서 다 배열에 저장해준다.
        int idx = 0; // 검사 기준이 되는 변수
        
        // 지금 배열에 저장된 형태는 [a, b,  , c, .....] 띄어쓰기까지 저장 되어있다.
        for (int i = 0; i < strArr.length; i++) {
            if (strArr[i].equals(" ")) { // 띄어쓰기를 만나면
                idx = 0; // 검사 기준이 되는 인덱스 초기화
            } else if (idx % 2 == 0) { // 짝수라면 대문자
                strArr[i] = strArr[i].toUpperCase();
                idx++;
            } else { // 그외 ( 홀수 ) 라면 소문자
                strArr[i] = strArr[i].toLowerCase();
                idx++;
            }
            answer += strArr[i];
        }
        return answer;
    }
}