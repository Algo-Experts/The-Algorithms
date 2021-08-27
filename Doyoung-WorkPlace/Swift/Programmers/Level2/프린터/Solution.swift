//
//  Solution.swift
//  
//
//  Created by Doyoung on 2021/08/27.
//

import Foundation

//1. 인쇄 대기목록의 가장 앞에 있는 문서(J)를 대기목록에서 꺼냅니다.
//2. 나머지 인쇄 대기목록에서 J보다 중요도가 높은 문서가 한 개라도 존재하면 J를 대기목록의 가장 마지막에 넣습니다.
//3. 그렇지 않으면 J를 인쇄합니다.
//예를 들어, 4개의 문서(A, B, C, D)가 순서대로 인쇄 대기목록에 있고 중요도가 2 1 3 2 라면 C D A B 순으로 인쇄하게 됩니다.
//조건2: 6개의 문서(A, B, C, D, E, F)가 인쇄 대기목록에 있고 중요도가 1 1 9 1 1 1 이므로 C D E F A B 순으로 인쇄합니다.
func solution(_ priorities:[Int], _ location:Int) -> Int {
    
    //return priorities.sorted(by: >).firstIndex(of: priorities[location])! + 1
    
    //sorted 문제 중복되는 수 카운팅 불가
    // Fifo방식으로 최대값일때 카운트 +1 하고 배열에서 제거 아니면 배열 제일 뒤로 보내는 방식으로 무한 반복으로 구해기로 했습니다.
    var result = 0
    var indexLocation = location
    var countingArray = priorities
    
    while true {
        if countingArray.first == countingArray.max() {
            result += 1
            print(result)
            countingArray.removeFirst()
            if indexLocation == 0 {
                break
            }
            indexLocation -= 1
        } else {
            countingArray.append(countingArray.first!)
            countingArray.removeFirst()
            if indexLocation == 0 {
                indexLocation = countingArray.count
            }
            indexLocation -= 1
        }
    }
    
    return result
}
