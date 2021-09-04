//
//  main.swift
//  solution
//
//  Created by SooHoon on 2021/09/05.
//

import Foundation

var input = readLine()
var num = Int(input!)!

var emp = ""
var a = "*"

// stride 함수를 이용하면 범위 연산이 편리하다. 즉, 오름차순이 아니라 내림차순으로 순서로 연산을 진행할 수 있다.
// from 5 to 1  >>>> 5..>1 과 같다고 생각함.

for i in 1...num{
    
    emp = ""
    for _ in stride(from: num , to: i, by: -1) { // 5..>1
        emp.append(" ")
    }

    print(emp + a) // 왼쪽 정렬
    a.append("*")

    
}
//
//  main.swift
//  solution
//
//  Created by SooHoon on 2021/09/05.
//

import Foundation

var input = readLine()
var num: Int = Int(input!)!


// Solution 1
/* for문 밖에서 print 할 변수를 선언해주고 1씩 뺴준다.
   이렇게 되면 강한참조가 되어서 초기 선언했던 num 변수가 초기화 되지 않는다. 즉, instance의 값이 영구적으로 변한다.
   이렇게 풀면 for 문의 i는 의미 없는 숫자가 된다. _ 로 사용하지 않는 변수로 바꿔준다.
 */
for _ in 0...Int(input!)! {
   print(num)
    num -= 1
}

//Solution 2
/*
 for 문 안에서 readLine 을 int로 변환한 변수를 선언해준다.
 이렇게 되면 반복문이 실행 될 때마다 num 변수값이 초기화 되기 때문에
 매번 i를 뺴줘도 된다.
 */
 
for i in 0...Int(input!)! {
    var num: Int = Int(input!)!
   print(num)
    num -= i
    print("i : \(i)")
    print("result \(num)")
}


