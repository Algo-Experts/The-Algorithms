/**
 * @param {string} s
 * @return {number}
 */
/**
 *
 *  문제 설명
 * - String s = "abcabcbb" 로 param 들어옴
 *
 * - 이때 가장 길게 다른 수로 연속되어진 것은 "abc" 이므로
 *
 * - 그 길이인 3을 리턴 해준다.
 *
 * 문제 풀이
 * 1. Objects pass 를 선언하여  s 의 모든 값을 지나쳤는지 확인한다. // -> 중복 허용 x
 * 2. check_un_duplicate_arr 를 통해 지속적으로 중복되지 않은 값을 체크하는 값을 넣는 array 를 선언
 *      -> abcc 일 경우 [3,0] 으로 들어가게끔
 * 3. count 를 통해 check_un_duplicate_arr 의 원소 int 값 선언 /  원소 이동 값 i 선언
 * 4. String s 값을 입력 받아 그 길이 만큼 반복문 돌리며
 *    dict pass 의  index 의 값이 null 이면 아무 string 값("p") 를 주어 체크했다는 것을 알림
 * 5. 체크 시에 count 값과 i 값은 자동 증감
 * 6. 1번의 특징을 이용해 만약 같은 알파벳이 나올 경우 4번의 아무 string 값이 주어져 있어
 *    check_un_duplicate_arr 에 여기 까지가 최대로 중복 되어지지 않았으므로 쌓여진 count 를 push
 *    해주며 남은 수의 갯수로 i 를 갱신 , object pass 를 갱신한다. 물론 count 또한 갱신
 * 7. 반복문 종료시 강제로 count를 넣는다 --> s= ""라는 식으로 들어올수도 있음
 *
 * 8. check_un_duplicate_arr 의 최댓값이 곧 return 값
 *
 */

var lengthOfLongestSubstring = function (s) {
  //   1번 순서
  let pass = {};
  //  2번 순서
  let check_un_duplicate_arr = [];
  // 3번 순서
  let count = 0;

  let i = 0;

  //   4번 순서
  while (i < s.length) {
    if (!pass[s[i]]) {
      pass[s[i]] = "p";
      //   5번 순서
      count++;
      i++;
      //   6번 순서
    } else {
      check_un_duplicate_arr.push(count);
      pass = {};

      i = i + 1 - count;

      count = 0;
    }
  }
  //   7번 순서
  check_un_duplicate_arr.push(count);
  //   8번 순서 ( JS 최댓값 도출 법  Math.max(...values: number[]): number)
  return Math.max(...check_un_duplicate_arr);
};

// console.log(lengthOfLongestSubstring("abcdabcdabb"));
