/**
 * @param {string} s
 * @return {string}
 */
// 문제 설명
// 왼쪽 부터, 오른쪽 부터 읽어도 같은 단어가 되는 단어를 찾아라!!
//  예를 들어 s = "cbbd" 가 pararm 으로 들어 왔을 경우, bb 를 리턴
//  예를 들어2 s  = "babad" 가 param 으로 들어 왔을 경우, bab 나 aba 를 리턴 한다.
//  예를 들어3 s  = "ac" s = "a" 가 param 으로 들어 왔을 경우, 둘다 a 를 리턴 하면 된다.

// 풀이 순서
//  1. start 와 end 변수 , len 변수를 만들어 만들어진 s 문자열의 시작점 ( start ) , 끝점 ( end ) 을 구하고 구한 시작점과 끝점을 이용해서 len 을 구한다.
//  2. s 문자열중 반복되는 문자열의 start 와 end , len 을 구하기 위해 함수 isPalindrome 선언
//
//

var longestPalindrome = function (s) {
  let start = 0;
  let end = 0;
  let len = 0;

  // 가장 긴 연속된 숫자의 길이를 구하는 함수
  // 문자열이 s ,  만들어질수 있는 단어를 구하는데, 단어의 왼쪽 순서를 left , 오른쪽 순서를 right 이라 한다.

  function isPalindromeLength(s, left, right) {
    if (left > right) return 0;

    while (left >= 0 && right < s.length && s[left] == s[right]) {
      left--;
      right++;
    }

    return right - left - 1;
  }

  for (var i = 0; i < s.length; i++) {
    //  문자열의 시작 부분과 끝부분을 교차하며 검사
    let p1 = isPalindromeLength(s, i, i);
    let p2 = isPalindromeLength(s, i, i + 1);
    len = Math.max(p1, p2);
    // 가장 긴 반복열의 길이를 출력 한다.
    if (len > end - start) {
      // 반복열이 시작 되는 위치를 start 변수에 넣는다.
      start = Math.ceil(i - (len - 1) / 2);

      // 반복열이 끝나는 위치를 end 변수에 넣는다.
      end = i + len / 2;
    }
  }

  // 문자열 s 를 slice 하여 return 한다.
  return s.slice(start, end + 1);
};
