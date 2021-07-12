//
//  sumOfProcession.swift
//  AlgorithmNote
//
//  Created by ido on 2021/07/12.
//

import Foundation

//행렬의 덧셈은 행과 열의 크기가 같은 두 행렬의 같은 행, 같은 열의 값을 서로 더한 결과가 됩니다. 2개의 행렬 arr1과 arr2를 입력받아, 행렬 덧셈의 결과를 반환하는 함수, solution을 완성해주세요.

func solution(_ arr1:[[Int]], _ arr2:[[Int]]) -> [[Int]] {
    
    var result: [[Int]] = [] // 빈배열 생성
    
    for outter in 0..<arr1.count {
        result.append([]) //배열에 빈배열 추가
        for inner in 0..<arr1[outter].count {
            result[outter].append(arr1[outter][inner] + arr2[outter][inner])
        }
        
    }
    return result
}
