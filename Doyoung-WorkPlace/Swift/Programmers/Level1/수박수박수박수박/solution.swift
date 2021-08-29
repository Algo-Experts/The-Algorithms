//
//  Watermelon.swift
//  AlgorithmNote
//
//  Created by ido on 2021/07/10.
//

import Foundation

func solution(_ n:Int) -> String {
    
//    길이가 n이고, "수박수박수박수...."와 같은 패턴을 유지하는 문자열을 리턴하는 함수, solution을 완성하세요. 예를들어 n이 4이면 "수박수박"을 리턴하고 3이라면 "수박수"를 리턴하면 됩니다.
    
    let watermelon = String(repeating: "수박", count: n/2)
    
    guard n%2 == 0 else {
        return "\(watermelon)수"
    }
    
    return watermelon
    
}

//1. 완벽한 수박 프로퍼티 생성
//2. 2로 나누어 떨어지지 않을 경우 뒤에 "수"를 추가해서 guard 문으로 빠른 종료 아닐지, 그대로 리턴
