//
//  AddChosenTwo.swift
//  AlgorithmNote
//
//  Created by ido on 2021/07/11.
//

import Foundation

//정수 배열 numbers가 주어집니다. numbers에서 서로 다른 인덱스에 있는 두 개의 수를 뽑아 더해서 만들 수 있는 모든 수를 배열에 오름차순으로 담아 return 하도록 solution 함수를 완성해주세요.

func solution(_ numbers:[Int]) -> [Int] {
    var array = [Int]()

    var x = 0
    var y = x+1
    
    while x < numbers.endIndex - 1 {
        if y < numbers.endIndex {
            let sum = numbers[x] + numbers[y]
            array.append(sum)
            y += 1
        } else {
            x += 1
            y = x + 1
        }
    }
    let sums = Set(array) //중복제거
    let value = sums.sorted() //오름차순
    return value
}
