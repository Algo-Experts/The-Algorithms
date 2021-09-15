//
//  File.swift
//  
//
//  Created by Doyoung on 2021/09/15.
//

import Foundation

//작업의 개수(progresses, speeds배열의 길이)는 100개 이하입니다.
//배포는 하루에 한 번만 할 수 있으며, 하루의 끝에 이루어진다고 가정합니다. 예를 들어 진도율이 95%인 작업의 개발 속도가 하루에 4%라면 배포는 2일 뒤에 이루어집니다.

/*
 입력값 [93, 30, 55], [1, 30, 5] -> 기댓값 [2, 1]
 입력값 [95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1] -> 기댓값 [1, 3, 2]
 */

func solution(_ progresses:[Int], _ speeds:[Int]) -> [Int] {
    
    var remaining = [Int]()
    var result = [Int]()
    
    for index in progresses.indices {
        remaining.append(Int(ceil(Float(100-progresses[index])/Float(speeds[index]))))
    }
    while !remaining.isEmpty {
        let index = remaining.removeFirst()
        var count = 1
        while remaining.count != 0 {
            if remaining.first! > index {
                break
            }
            remaining.removeFirst()
            count += 1
        }
        result.append(count)
    }
    
    return result
}
