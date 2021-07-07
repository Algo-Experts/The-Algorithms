//
//  FailureRate.swift
//  AlgorithmNote
//
//  Created by ido on 2021/07/07.
//

import Foundation

//실패율은 다음과 같이 정의한다.
//스테이지에 도달했으나 아직 클리어하지 못한 플레이어의 수 / 스테이지에 도달한 플레이어 수
//전체 스테이지의 개수 N, 게임을 이용하는 사용자가 현재 멈춰있는 스테이지의 번호가 담긴 배열 stages가 매개변수로 주어질 때, 실패율이 높은 스테이지부터 내림차순으로 스테이지의 번호가 담겨있는 배열을 return 하도록 solution 함수를 완성하라.
func solution(_ N:Int, _ stages:[Int]) -> [Int] {
    
    var failureRates: [Int: Float] = [:] // [스테이지: 실패율], Dictionary 필요
    var tried = stages.count // 시도한 사람 수
    
    for stage in 1...N {
        let ofStage = stages.filter { $0 == stage }// 스테이지 설정
        
        let failureRate:Float = Float(ofStage.count)/Float(tried)//실패율 구하기
        
        failureRates[stage] = failureRate // 스테이지별 실패율 생성
        
        tried -= ofStage.count // 단계별로 실패한 사람 수 빼기
    }
    
    let result = failureRates.sorted(by: <).sorted(by: {$0.value > $1.value}).map{$0.key} // 단계별 내림차순 정렬, 실패율 내림차순 정렬, key(단계)로 mapping
    
    return result
}
