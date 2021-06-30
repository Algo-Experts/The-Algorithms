//
//  File.swift
//  
//
//  Created by ido on 2021/06/30.
//

import Foundation

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
    let sums = Set(array)
    let value = Array(sums).sorted()
    return value
}
