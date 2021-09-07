class Solution {
    public String solution(String[] seoul) {
        String answer = "";
        
        for (int i = 0; i < seoul.length; i++) {
            if (seoul[i].equals("Kim")) {
                answer = "김서방은 " + i + "에 있다";
            }
        }
        return answer;
    }
}


// 다른사람 코드
class Solution {
    public String solution(String[] seoul) {
        String answer = "";
        
        int index = Arrays.asList(seoul).indexOf("Kim");
                
        answer = "김서방은 " + index + "에 있다";
        
        return answer;
    }
}