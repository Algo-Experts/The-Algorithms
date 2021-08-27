//
//  Solution.swift
//  
//
//  Created by Doyoung on 2021/08/21.
//

import Foundation

func solution(_ absolutes:[Int], _ signs:[Bool]) -> Int {

    var result = 0
    for calc in 0 ..< signs.count {
        if signs[calc] {
            result += absolutes[calc]
        } else {
            result -= absolutes[calc]
        }
    }
    return result

}

//신기한 풀이: zip활용
func solutionTwo(_ absolutes:[Int], _ signs:[Bool]) -> Int {
    zip(absolutes, signs)
        .map { $1 ? $0 : -$0 }
        .reduce(0, +)
}
