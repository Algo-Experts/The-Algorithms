/**
 * @param {number[]} height
 * @return {number}
 */

var maxArea = function (height) {
  let answer = 0;
  for (let lo = 0, hi = height.length - 1; lo < hi; ) {
    answer = Math.max(answer, Math.min(height[lo], height[hi]) * (hi - lo));

    // console.log(lo, hi);

    if (height[lo] < height[hi]) ++lo;
    else --hi;
  }
  return answer;
};
