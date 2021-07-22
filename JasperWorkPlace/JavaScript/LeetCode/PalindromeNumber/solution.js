/**
 * @param {number} x
 * @return {boolean}
 */
/**
 * 문제 설명
 *
 * 1. 반복되어 지는 수인지 체크하고 bool 값  return 해준다.
 *
 *
 */

var isPalindrome = function (x) {
  let rev = x.toString().split("").reverse().join("");
  return rev == x ? true : false;
};

// console.log(isPalinrome(-101))
