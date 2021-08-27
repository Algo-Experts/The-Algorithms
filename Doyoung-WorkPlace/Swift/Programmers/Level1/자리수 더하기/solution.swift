//
//  solution.swift
//  
//
//  Created by ido on 2021/07/19.
//

import Foundation

//자연수 N이 주어지면, N의 각 자릿수의 합을 구해서 return 하는 solution 함수를 만들어 주세요. 😅

func solution(_ n:Int) -> Int
{
    return Array(String(n)).map{ String($0)}.map{ Int($0)!}.reduce(0, +)
    // 한자리 스트링 배열로 케스팅 -> 인트로 케스팅 후 맵핑-> -> reduce로 배열 총합 구하기!
}
