//
//  Solution.swift
//  
//
//  Created by Doyoung on 2021/08/16.
//

import Foundation

// 문제 README 참조

func solution(_ scores:[[Int]]) -> String {
    
    var result = ""
    
    for index in 0 ..< scores.count {
        
        var userScores = [Int]()
        
        for score in scores {
            userScores.append(score[index])
        }
        
        var sum = userScores.reduce(0){ $0 + $1 }
        var count = userScores.count
        
        let filterMax = userScores.filter{ $0 == userScores.max() }
        let filterMin = userScores.filter{ $0 == userScores.min() }
        if userScores[index] == userScores.max() {
            if filterMax.count == 1 {
                sum -= userScores[index]
                count -= 1
            }
        }else if userScores[index] == userScores.min() {
            if filterMin.count == 1 {
                sum -= userScores[index]
                count -= 1
            }
        }
        
        
        let average: Float = Float(sum/count)
        
        switch average {
        case 90...:
            result.append("A")
        case 80..<90:
            result.append("B")
        case 70..<80:
            result.append("C")
        case 50..<70:
            result.append("D")
        default:
            result.append("F")
        }
        
    }
    
    return result
}
