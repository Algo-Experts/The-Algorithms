/**
 * Definition for singly-linked list.
 *
 * // 문제에서 주어지는 것 ..
 *
 * function ListNode(val, next) {
 *
 *     this.val = (val === undefined ? 0 : val)
 *
 *     this.next = (next===undefined ? null : next)
 *
 * }
 */
/**
 * @param {ListNode} l1
 * @param {ListNode} l2
 * @return {ListNode}
 */

// undefined 됬을 경우

/**
 * 문제 설명 : l1 [2, 4 , 3] l2 [5,6,4] 로 param 이 input 되었을때,
 *
 *  [7,0,8] 이 return 된다. ( 342 + 465 = 807 이 되기 때문에 )
 *
 * 문제 풀이
 * 1. l1, l2 를 받아오는 변수 , num1 , num2, 올림값(carry) , 결과 값을 저장할 solution -> ListNode, 현재 자리수를 current 라 선언
 * 2. p1, p2 가 있을때 까지 반복문
 * 3. num1 과 num2 의 현재 노드를 return 해 주거나 p1 혹은 p2 가 없다면 0을 리턴
 * 4. 같은 노드 끼리의 합이 9보다 클 경우 carry 1 증가 되고, current( 현재 노드에 num1 + num2 + carry( 처음 노드 이기 떄문에 초기값 0 당연히 10이 overflow 되니 - 10 ))
 *  현재 노드에서 다음 노드로 진행 하기 위해 current.next  , 다음 노드로 전달될 carry = 1
 * 5. 4번 방법과 반대로 진행 but , carry = 0
 *
 * 6. 조건문 빠져나와서 p1 과 p2 모두 다음 노드로 이동
 *
 * 7. while 문이 끝나고 p1 과 p2 의 마지막 노드를 다 돈 후에도 carry 가 존재 한다면, 다음 노드에 carry 를 올려줌
 *
 */
function ListNode(val, next) {
  //  현재 노드
  this.val = val === undefined ? 0 : val;
  //  다음 노드
  this.next = next === undefined ? null : next;
}

var addTwoNumbers = function (l1, l2) {
  let p1 = l1,
    p2 = l2,
    num1 = 0,
    num2 = 0,
    carry = 0,
    solution = new ListNode(0),
    current = solution;
  // 2번 풀이 과정
  while (p1 || p2) {
    num1 = p1 ? p1.val : 0;
    num2 = p2 ? p2.val : 0;
    //  3번 풀이 과정
    if (num1 + num2 + carry > 9) {
      // 올림 수가 발생할 경우
      current.next = new ListNode(num1 + num2 + carry - 10);
      current = current.next;
      carry = 1;
      //   4번 풀이 과정
    } else {
      // 울림수 발생 안할 경우
      current.next = new ListNode(num1 + num2 + carry);
      current = current.next;
      carry = 0;
    }
    //  6번 풀이과정
    if (p1) p1 = p1.next;
    if (p2) p2 = p2.next;
  }

  // 7번 풀이과정
  if (carry) current.next = new ListNode(carry);
  return solution.next;
};
