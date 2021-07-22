/**
 * @param {string} s
 * @return {number}
 *
 * 문제 설명
 *
 * 설명이 길기 때문에 얘시로 퉁침....
 * 
 * Example 1) 
 * Input: s = "42"
    Output: 42
    Explanation: The underlined characters are what is read in, the caret is the current reader position.
    Step 1: "42" (no characters read because there is no leading whitespace)
            ^
    Step 2: "42" (no characters read because there is neither a '-' nor '+')
            ^
    Step 3: "42" ("42" is read in)
              ^
    The parsed integer is 42.
    Since 42 is in the range [-231, 231 - 1], the final result is 42.

  * Example 2)
    Input: s = "words and 987"
    Output: 0
    Explanation:
    Step 1: "words and 987" (no characters read because there is no leading whitespace)
            ^
    Step 2: "words and 987" (no characters read because there is neither a '-' nor '+')
            ^
    Step 3: "words and 987" (reading stops immediately because there is a non-digit 'w')
            ^
    The parsed integer is 0 because no digits were read.
    Since 0 is in the range [-231, 231 - 1], the final result is 0.

  * Example 3)
    Input: s = "-91283472332"
    Output: -2147483648
    Explanation:
    Step 1: "-91283472332" (no characters read because there is no leading whitespace)
            ^
    Step 2: "-91283472332" ('-' is read, so the result should be negative)
              ^
    Step 3: "-91283472332" ("91283472332" is read in)
                        ^
    The parsed integer is -91283472332.
    Since -91283472332 is less than the lower bound of the range [-231, 231 - 1], the final result is clamped to -231 = -2147483648.
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
