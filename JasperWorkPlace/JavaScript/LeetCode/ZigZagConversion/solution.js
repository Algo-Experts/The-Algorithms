/*
문제 설명

Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"

0 P   A   H   N
1 A P L S I I G
2 Y   I   R

input      "P A Y P A L I S H I R I N G"
row Heights 0 1 2 1 0 1 2 1 0 1 2 1 0 1
            
Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:

0 P     I    N
1 A   L S  I G
2 Y A   H R
3 P     I

input      "P A Y P A L I S H I R I N G"
row Heights 0 1 2 3 2 1 0 1 2 3 2 1 0 1

*/

/**
 * @param {string} s
 * @param {number} numRows
 * @return {string}
 */

// 문제 풀이 순서

var convert = function (s, numRows) {
  // param numRows 로 들어오는 숫자로 s 의 문자열을 재배치 할 배열
  var rowArray = [];
  // rowArray 로 들어가는 위치 상수
  var rowHeight = 0;
  // s 가 3일 때  0 , 1 , 2 가 모두 채워졌을때, 다시 1 , 0 으로 내려 가고, 다시 1 , 2 로 올라가게 하기 위한 목적의 bool 상수
  var slope = true;
  //   증가 상수
  var i = 0;

  //   만약 s 가 공백이거나 numRows 가 1 이면, 그대로 공백이나 문자그대로를 return 한다.
  if (s === "") return s;
  if (numRows === 1) return s;

  // 문자열 s 의 길이만큼 반복문을 사용
  while (i < s.length) {
    //  만약 rowArray 의 배열의 index rowHeight에 문자열이 존재하지 않을 경우,
    if (!rowArray[rowHeight]) {
      //  값을 넣어주는데, 배열의 형태로 해당하는 같은 row 에 존재하는 문자열을 넣어준다.
      rowArray[rowHeight] = [s[i]];
    } else {
      //  만약 문자열이 존재 한다면, 그 문자열에 이어서 배열 값을 더해 준다.
      let cur = rowArray[rowHeight];
      cur += s[i];
      rowArray[rowHeight] = cur;
    }

    //  0 , 1 , 2 로 올라가는 경우 rowHeight 를 더해주며, 아닐 경우 rowHeight 를 빼준다.
    if (slope) {
      rowHeight++;
    } else {
      rowHeight--;
    }
    if (rowHeight === numRows - 1 || rowHeight === 0) {
      slope = !slope;
    }

    // While 문의 반복을 위해서 상수 더해주기
    i++;
  }

  return rowArray.join("");
};

// console.log(convert("PAYPALISHIRING", 4));
