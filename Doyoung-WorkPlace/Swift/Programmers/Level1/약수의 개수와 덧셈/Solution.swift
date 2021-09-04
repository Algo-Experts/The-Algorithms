//
//  Solution.swift
//
//  Created by Doyoung on 2021/09/04.
//

import Foundation

//두 정수 left와 right가 매개변수로 주어집니다. left부터 right까지의 모든 수들 중에서, 약수의 개수가 짝수인 수는 더하고, 약수의 개수가 홀수인 수는 뺀 수를 return 하도록 solution 함수를 완성해주세요.

func solution(_ left:Int, _ right:Int) -> Int {
    
    var result = 0
    
    for number in left...right {
        let divisorCount = Array(1...number).filter{ number % $0 == 0}.count
        if divisorCount % 2 == 0 {
            result += number
        } else {
            result -= number
        }
    }
    return result
}


