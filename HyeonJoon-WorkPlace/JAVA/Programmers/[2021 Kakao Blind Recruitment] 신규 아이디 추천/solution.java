class Solution {

    public String solution(String[] participant, String[] completion) {
        String answer = "";
        int[] Checker = new int[participant.length];

        // checker 값 0으로 초기화
        for (int i=0; i<Checker.length; i++){
            Checker[i] = 0; 
        }

        // 값이 같은 경우, participant와 같은 위치에 Checker 값 1 부여 (마치 시험지 체크 하듯이)
        for (int i=0; i<completion.length; i++){
            
            for(int j=0; j<participant.length; j++){
                if(completion[i].equals(participant[j])){
                    Checker[j] = 1;
                    break;
                }else {}
            }
        }

        // 0 값이 부여된 Checker를 찾아 같은 위치의 participant 값을 answer에 넣어줌
        for (int i=0; i<Checker.length; i++){
            if(Checker[i] == 0) {
                answer = participant[i];
                break;
            }
        }

        return answer;
    }
}

