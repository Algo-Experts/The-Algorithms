class Solution {
    public int[] solution(int[] arr) {
        int[] answer = new int[arr.length - 1]; // 제일 작은 수가 없어질거니까 초기화 자체를 한자리 수 적게 선언한다.
        int min = arr[0]; // 제일 작은 수를 비교하기 위한 기준
        int index = 0; // answer배열의 인덱스 번호가 될 변수
        
        if (arr.length <= 1) { // 만일 arr의 인덱스가 1 과 같거나 작으면 다른 arr를 리턴한다.
            int[] arr2 = { -1 };
            return arr2;
        }
        
        for (int i = 0; i < arr.length; i++) { // 제일 작은 수를 확인.
            if (arr[i] < min) {
                min = arr[i];
            }
        }
        
        for (int i = 0; i < arr.length; i++) { // 위에 선언한 answer 배열에 제일 작은 수 빼고 나머지 수만 저장하는 for문
            if (min == arr[i]) {
                continue;
            } else {
                answer[index++] = arr[i];
            }
        }
        return answer;
    }
}