import java.util.*;

public class Solution {
    public int solution(int n) {
        int answer = 0; // 총 합의 변수 선언

        while (n != 0) { // 자연수 n이 0 과 같지 않을때까지 반복문
            answer += n % 10; // 자연수의 끝자리 수를 가져오기 위한 나머지 값을 answer에 더한다.
            n /= 10; // 구한 끝자리 수는 answer에 저장되었으니 그 다음 수 구하기 위해 나눠준다.
        }

        return answer;
    }
}