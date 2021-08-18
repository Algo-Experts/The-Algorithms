//
//  Solution.swift
//  AlgorithmNote
//
//  Created by Doyoung on 2021/08/18.
//

import Foundation

//전체 학생의 수 n, 체육복을 도난당한 학생들의 번호가 담긴 배열 lost, 여벌의 체육복을 가져온 학생들의 번호가 담긴 배열 reserve가 매개변수로 주어질 때, 체육수업을 들을 수 있는 학생의 최댓값을 return 하도록 solution 함수를 작성해주세요.

func solution(_ n:Int, _ lost:[Int], _ reserve:[Int]) -> Int {
    
    var students = Array(repeating: 1, count: n)
  
    for number in lost {
        students[number-1] = 0
    }
  
    for number in reserve {
        students[number-1] += 1
    }
    
    var result = n
    
    for index in 0 ..< n {
        
        let front = students[index-1]
        let behind = students[index+1]
        
        if students[index] == 0 {
            if index > 0, front > 1 {
                students[index] = 1
                students[index-1] = 1
            } else if index < n - 1, behind > 1 {
                students[index] = 1
                students[index+1] = 1
            } else {
                result -= 1
            }
        }
    }
    
    return result
    
}
