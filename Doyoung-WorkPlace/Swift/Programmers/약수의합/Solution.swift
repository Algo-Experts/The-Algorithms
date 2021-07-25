//
//  Solution.swift
//  
//
//  Created by ido on 2021/07/25.
//

import Foundation

//정수 n을 입력받아 n의 약수를 모두 더한 값을 리턴하는 함수, solution을 완성해주세요.

func solution(_ n:Int) -> Int {
    
    return n == 0 ? 0 : Array(1...n).filter{n % $0 == 0}.reduce(0){ $0 + $1}
    // 0일 경우, 0 리턴,,,아닐경우 1부터 n까지 나누어 떨어지는 것으로 배열 filtering -> reduce로 합 구하기
}
