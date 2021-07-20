/**
 * @param {number} x
 * @return {number}
 *
 *
 */
/*
정수 x 가 들어 왔을때, 반대로 뒤집어서 숫자 표현
ex)  x = 123 , 321
    x = -123 , -321
    x= 120 -> 21

    Array.from(String(x), Number


    -231 <= x <= 231 - 1

    제약 조건 좀 잘 보자 .................

*/

var reverse = function (x) {
  var answer = "";

  var num1;

  let max = Math.pow(2, 31) - 1;
  let min = -Math.pow(2, 31);
  //   let min = Math.pow(-2 , 31)

  if (x > 0 && x <= max) {
    var a = Array.from(String(x), Number).reverse();

    for (i = 0; i < a.length; i++) {
      answer += a[i];
    }

    num1 = parseInt(answer);

    if (num1 > min && num1 <= max) {
      return num1;
    } else {
      return 0;
    }
  } else if (x >= min && x < 0) {
    var b = Array.from(String(x), Number).reverse();

    for (i = 0; i < b.length; i++) {
      answer += b[i];
    }

    num1 = parseInt(answer) * -1;

    if (num1 > min && num1 <= max) {
      return num1;
    } else {
      return 0;
    }
  } else {
    return 0;
  }
};

console.log(reverse(1534236469));
