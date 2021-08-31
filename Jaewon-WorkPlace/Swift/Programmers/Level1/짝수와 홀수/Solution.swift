//
//  File.swift
//  
//
//  Created by Jaewon Park on 2021/08/30.
//

import Foundation

// [ 문제설명 ]
// 정수 num이 짝수일 경우 "Even"을 반환하고 홀수인 경우 "Odd"를 반환하는 함수
//
// [ 제한사항 ]
// num은 int 범위의 정수입니다.
// 0은 짝수입니다.
//
// [ 입출력예 ]
// 3 "Odd"
// 4 "Even"

func solution(_ num:Int) -> String {
    return num % 2 == 0 ? "Even" : "Odd"
}
