import java.util.Arrays;

class Solution {
    public long solution(long n) {
    
        // long 을 String으로 형변환
        String str = String.valueOf(n);
        
        // return 배열 선언. 개수는 String의 개수만큼
        int[] answer = new int[str.length()];
        
        // String으로 변환된 값을 각각 하나씩 짤라서 배열에 저장
        String[] strArr = str.toString().split("");
        // 내림차순
        Arrays.sort(strArr,Collections.reverseOrder());
        
        // for문을 돌며 return 배열에 저장
        for (int i = 0; i < strArr.length; i++) {
            answer[i] = Integer.parseInt(strArr[i]);
        }
        return answer;
    }
}