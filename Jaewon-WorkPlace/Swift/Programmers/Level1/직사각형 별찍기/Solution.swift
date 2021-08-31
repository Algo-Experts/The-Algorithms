//
//  File.swift
//  
//
//  Created by Jaewon Park on 2021/08/30.
//

import Foundation

// [ 문제설명 ]
// 이 문제에는 표준 입력으로 두 개의 정수 n과 m이 주어집니다.
// 별(*) 문자를 이용해 가로의 길이가 n, 세로의 길이가 m인 직사각형 형태를 출력해보세요.
//
// [ 제한사항 ]
// - n과 m은 각각 1000 이하인 자연수입니다.
//
// [ 입출력예 ]
// 5 3
// *****
// *****
// *****

import Foundation

let n = readLine()!.components(separatedBy: [" "]).map { Int($0)! }
let (a, b) = (n[0], n[1])
var result:String = ""
for i in 1...b {
    for i in 1...a {
        result += "*"
    }
    result += "\n"
}
print(result)
