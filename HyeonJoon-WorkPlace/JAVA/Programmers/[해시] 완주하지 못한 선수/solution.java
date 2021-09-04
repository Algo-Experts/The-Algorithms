import java.util.Arrays;
import java.util.List;
import java.util.stream.Collectors;

// 마라톤 경기에 참여한 선수의 수는 1명 이상 100,000명 이하입니다.
// completion의 길이는 participant의 길이보다 1 작습니다.
// 참가자의 이름은 1개 이상 20개 이하의 알파벳 소문자로 이루어져 있습니다.
// 참가자 중에는 동명이인이 있을 수 있습니다.

class Solution {

    public static String solution(String[] participant, String[] completion) {
        String answer = "";

        // 참가자와 완주자 명단을 오름차순으로 정렬하고 List 형태로 저장.
        List<String> listParticipant = (List<String>) Arrays.asList(participant).stream().sorted().collect(Collectors.toList());
        List<String> listCompletion = (List<String>) Arrays.asList(completion).stream().sorted().collect(Collectors.toList());

        // 정렬된 명단 중 제일 마지막 index
        int difIndex = listParticipant.size()-1;

        // 정렬된 리스트를 비교하며, 값이 다른 부분에서 index값을 기록하고 빠져나간다. 없을 시 difIndex는 변하지 않음
        for(int index = 0; index < listCompletion.size(); index++){
            if(!listCompletion.get(index).equals(listParticipant.get(index))){
                difIndex = index;
                break;
            }
        }

        answer = listParticipant.get(difIndex);

        return answer;
    }
}
