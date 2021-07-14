/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @return {number}
 */

/**
 * 문제 설명
 *
 *  nums1 과 nums2 가 배열의 형태로 들어오면, ex) [1,2] [3,4] -> 빈 배열이 들어 올수 있고, 0 만 있는 배열이 들어 올 수도 있다.
 *
 *  베열을 정렬하여 ex) [1,2,3,4]
 *
 *  가운데의 수의 평균을 return 한다  ex) 2.5
 *
 *
 * 문제 풀이 순서
 * 1. nums1 과 nums2 의 배열을 정렬 되게끔 만들며, 합친다. ( js 는 파이썬과 같이 다양한 함수들을 제공 받지 못해 일단 알아서 해줌 )
 *
 * 2. 배열의 길이를 2로 나누어 홀수 인지 짝수인지 구별 후 배열 가운데의 수를 리턴 한다.
 *
 * (홀수이면 가운데 수를 그냥 return 하면 되고 짝수이면 가운데의 2수를 더해서 그 평균을 return 한다.)
 *
 */
var findMedianSortedArrays = function (nums1, nums2) {
  let a = 0;
  let b = 0;

  let new_array = [];
  // 문제 풀이 순서 1
  while (a < nums1.length && b < nums2.length) {
    if (nums1[a] < nums2[b]) {
      new_array.push(nums1[a]);
      a++;
    } else {
      new_array.push(nums2[b]);
      b++;
    }
  }

  while (a < nums1.length) {
    new_array.push(nums1[a]);
    a++;
  }

  while (b < nums2.length) {
    new_array.push(nums2[b]);
    b++;
  }
  // 문제 풀이 순서 2
  let start_point = 0;
  let end_point = new_array.length - 1;

  if (new_array.length % 2 === 1) {
    let median = Math.floor((start_point + end_point) / 2);

    return new_array[median];
  }

  if (new_array.length % 2 === 0) {
    let median = Math.floor((start_point + end_point) / 2);

    return (new_array[median] + new_array[median + 1]) / 2;
  }
};

console.log(findMedianSortedArrays([1, 4], [2, 3]));
