class Solution {
    public long[] solution(int x, int n) {
        long[] answer = new long[n];

        for(long i=0; i<n; i++){
            answer[(int)i] = x*(i+1);
        }
        return answer;
    }
}

// 다른 사람의 풀이 1

// import java.util.*;
// class Solution {
//     public static long[] solution(int x, int n) {
//         long[] answer = new long[n];
//         answer[0] = x;

//         for (int i = 1; i < n; i++) {
//             answer[i] = answer[i - 1] + x;
//         }

//         return answer;

//     }
// }

// 다른 사람의 풀이 2

// class Solution {
//   public long[] solution(int x, int n) {
//       long[] answer = new long[n];
//       long sum = 0;
//       for(int i = 0;i<answer.length;i++){
//           sum += x;
//           answer[i] = sum;
//       }


//       return answer;
//   }
// }