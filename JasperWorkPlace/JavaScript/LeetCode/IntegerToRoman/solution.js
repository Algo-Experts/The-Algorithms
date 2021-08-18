/**
 * @param {number} num
 * @return {string}
 */
var intToRoman = function (num) {
  let map = {
    1000: "M",
    900: "CM",
    500: "D",
    400: "CD",
    100: "C",
    90: "XC",
    50: "L",
    40: "XL",
    10: "X",
    9: "IX",
    5: "V",
    4: "IV",
    1: "I",
  };

  // O(1)
  let sorted = Object.keys(map).sort((a, b) => {
    // 내림 차순 정렬
    return b - a;
  });

  console.log(sorted);
  let result = "";

  // O(n)
  for (let val of sorted) {
    if (val > num) {
      // val 이 num 보다 클때, 무시하고 넘어가게끔 만들어준다.
      /* console.log("val 입니다.", val);
      console.log("num 입니다.", num); */
      continue;
    }
    while (num >= val) {
      result += map[val];
      num -= val;
    }
  }
  return result;
};

console.log(intToRoman(123));
