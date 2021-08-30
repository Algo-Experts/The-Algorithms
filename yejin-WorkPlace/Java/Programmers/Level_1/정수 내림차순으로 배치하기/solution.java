import java.util.Arrays;

class Solution {
    public long solution(long n) {
        long answer = 0; // 값 저장될 변수
        String str = Long.toString(n); // String 형변환
        char[] charArr = str.toCharArray(); // char 배열에 쪼개서 저장
        Arrays.sort(charArr); // 오름차순
        str = ""; // 재활용
        
        // 일반적인 for문을 사용하지만 거꾸로 돌려 str에 저장
        for (int i = charArr.length -1; i >= 0; i--) { 
            str += charArr[i];
        }
        
        answer = Long.parseLong(str); // 형변환
        return answer;
    }
}