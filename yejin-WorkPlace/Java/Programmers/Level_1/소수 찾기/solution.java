class Solution {
    public int solution(int num) {
        int answer = 0;
        int[] arr1 = new int[num + 1];
        
        // 입력받은 숫자 중 1을 제외한 숫자를 배열에 저장한다.
        for (int i = 2; i <= num; i++) {
            arr1[i] = i;
        }
        
        for(int i = 2; i <= num; i++) {
            if(arr1[i] == 0) {
                continue;
            }
            
            // 에라토스테네..?의 방법으로 배수들을 삭제하기 위해 이중반복문을 돌린다. ( ex. 2는 소수. 그 외 2의 배수는 소수가 아님. )
            for(int j = 2 * i; j <= num; j += i) {
                arr1[j] = 0;
            }
        }
        
        for(int i = 0; i < arr1.length; i++) {
            if(arr1[i] != 0) {
                answer++;
            }
        }
        return answer;
    }
}