/**
 * @param {string} s
 * @return {number}
 *
 * 문제 설명
 *
 * param s 로 진입하는
 */
var myAtoi = function (s) {
  const num = parseInt(s.replace(/-\D(e|E)?[.]?\D/g, "")),
    min = Math.pow(-2, 31),
    max = Math.pow(2, 31);

  if (s.match(/^[ ]*[\+]?-?[0-9]+/))
    // valid string
    return Number(num) >= max
      ? max - 1
      : Number(num) <= min
      ? min
      : !isNaN(num)
      ? num
      : 0;

  return 0; // not valid string
};
