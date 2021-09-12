//
//  Solution.swift
//  
//
//  Created by Doyoung on 2021/09/12.
//

import Foundation

func solutionSecretMap(_ n:Int, _ arr1:[Int], _ arr2:[Int]) -> [String] {
    var answer: [String] = []
    
    //1. 2진수 배열 만들기 (고급 연잔자 사용)
    var binaryNums: [String] {
        var array = [String]()
        for index in arr1.indices {
            var number = String(arr1[index] | arr2[index], radix: 2)
            
            while number.count < n {
                number = "0" + number
            }
            array.append(number)
        }
        return array
    }
    
    //2. 문자열 치환
    answer = binaryNums.map {
            $0.replacingOccurrences(of: "1", with: "#")
        }.map{
            $0.replacingOccurrences(of: "0", with: " ")
        }
    return answer
}
