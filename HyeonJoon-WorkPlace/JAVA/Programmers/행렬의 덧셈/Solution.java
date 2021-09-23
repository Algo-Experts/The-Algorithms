class Solution {
    public String solution(String phone_number) {
        String answer = "";
        String tmp = "";

        
        tmp = phone_number.substring(phone_number.length()-4, phone_number.length());
        for(int i=0; i<phone_number.length()-4; i++){
            answer += "*";
        }

        answer += tmp;
        return answer;
    }
   
}


// 다른사람의 풀이1

// class Solution {
//   public String solution(String phone_number) {
//      char[] ch = phone_number.toCharArray();
//      for(int i = 0; i < ch.length - 4; i ++){
//          ch[i] = '*';
//      }
//      return String.valueOf(ch);
//   }
// }

// 다른사람의 풀이2

// class Solution {
//   public String solution(String phone_number) {
//     return phone_number.replaceAll(".(?=.{4})", "*");
//   }
// }