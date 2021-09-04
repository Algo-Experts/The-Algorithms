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
