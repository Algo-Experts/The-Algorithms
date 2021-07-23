//
//  solution.swift
//  
//
//  Created by ido on 2021/07/23.
//

import Foundation

//정수를 저장한 배열, arr 에서 가장 작은 수를 제거한 배열을 리턴하는 함수, solution을 완성해주세요. 단, 리턴하려는 배열이 빈 배열인 경우엔 배열에 -1을 채워 리턴하세요. 예를들어 arr이 [4,3,2,1]인 경우는 [4,3,2]를 리턴 하고, [10]면 [-1]을 리턴 합니다.

func solution(_ arr:[Int]) -> [Int] {
    
    var result = arr
    result.remove(at: result.firstIndex(of: result.min() ?? -1)!) // 최소값인 index 제거 만약 빈 배열일 경우
  
    return result.isEmpty ? [-1] : result // 결과가 비어있을때는 [-1] 아닐 경우 그대로 결과를 내보냄.
}
