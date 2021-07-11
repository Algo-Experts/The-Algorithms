/**
 * 지워도 상관없음 문제에 있길래 퍼옴
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */

/**
 * 문제 설명
 * - 정수형 배열이 nums 로 들어온다.
 * - target 으로 들어오는 정수로 만들수 있는 nums 안의 원소의 위치를 배열로 저장하여
 * - return 해주면 됩니다.
 *
 * 문제 풀이 순서
 * 1. dictionary 형태의 js 에서 제공해주는 Map 을 선언한다.
 *
 * 2. map.set(nums[i] , i ) 의 형태로 구성해 준다.
 *
 * 2-1 . nums -> [3,3] / target -> 6 과 같은 경우에는 만약 2번 풀이 순서가 3번 보다 위에 있을 경우 [0 , 0] 이
 *      return 됨 그렇기 때문에 이것을 방지하기 위해 3번 아래로 2번 순서를 내림 //
 *
 * 3. map.has( 목표하는 수에서 배열 내의 숫자를 빼준 다음에 {문제의 경우 무조건 답이 나오는 경우 이기 때문에}
 *      빼준 값이 위치를 get 으로 가지고 오고, 빼준 숫자의 위치를 i 로 가지고 온다. )
 *
 *      %% x + y = target으로 했을 경우 x 의 위치를 i(x) y의 위치를 i(y) 로 할때
 *      %% target - x = y 이므로 i(x) 를 아래 함수의 i , i(y) 를 아래 함수의 map.get(target - nums[i]) 로 두었다.
 *
 */

var twoSum = function (nums, target) {
  let map = new Map();
  for (let i = 0; i < nums.length; i++) {
    if (map.has(target - nums[i])) {
      return [map.get(target - nums[i]), i];
    }
    map.set(nums[i], i);
  }
};

console.log(twoSum([3, 3], 6));
