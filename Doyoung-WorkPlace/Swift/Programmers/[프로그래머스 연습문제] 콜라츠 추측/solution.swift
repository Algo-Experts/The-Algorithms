//
//  CollatzInference.swift
//  AlgorithmNote
//
//  Created by ido on 2021/07/02.
//

import Foundation

//1-1. 입력된 수가 짝수라면 2로 나눕니다.
//1-2. 입력된 수가 홀수라면 3을 곱하고 1을 더합니다.
//2. 결과로 나온 수에 같은 작업을 1이 될 때까지 반복합니다.

//단, 작업을 500번을 반복해도 1이 되지 않는다면 –1을 반환해 주세요.

//ex )
// 6 -> 8
// 16 -> 4
// 626331 -> -1


func solution(_ num:Int) -> Int {
    var number = num // func의 매개변수는 상수이므로 변수로 재선언
    var count = 0
    
    while number != 1 && count <= 500 {
        if number % 2 == 0 {
            number = number / 2
        } else {
            number = number * 3 + 1
        }
        count += 1
    }
    
    return number == 1 ? count : -1
}

// 어렵지 않은 문제였으나 for문을 사용했을 경우, 체점 결과 테스트13을 페스하지 못해 오래걸렸다. while문으로 이용했더니 패스했다. for문의 실패요인은 아직..🤔
