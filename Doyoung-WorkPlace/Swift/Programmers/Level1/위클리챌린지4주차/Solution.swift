//
//  Solution.swift
//  AlgorithmNote
//
//  Created by Doyoung on 2021/08/28.
//

import Foundation

//직업군 언어 점수를 정리한 문자열 배열 table, 개발자가 사용하는 언어를 담은 문자열 배열 languages, 언어 선호도를 담은 정수 배열 preference가 매개변수로 주어집니다. 개발자가 사용하는 언어의 언어 선호도 x 직업군 언어 점수의 총합이 가장 높은 직업군을 return 하도록 solution 함수를 완성해주세요. 총합이 같은 직업군이 여러 개일 경우, 이름이 사전 순으로 가장 빠른 직업군을 return 해주세요.

func solution(_ table:[String], _ languages:[String], _ preference:[Int]) -> String {
    
    let newTable = table.map{ $0.components(separatedBy: " ") }.sorted { $0[0] < $1[0] }
    print(newTable)
    var scores = Array(repeating: 0, count: table.count)
    
    for index in 1...table.count {
        for language in languages {
            if newTable[index-1].contains(language) {
                switch newTable[index-1].firstIndex(of: language)! {
                case 1:
                    scores[index-1] += 5 * preference[languages.firstIndex(of: language)!]
                case 2:
                    scores[index-1] += 4 * preference[languages.firstIndex(of: language)!]
                case 3:
                    scores[index-1] += 3 * preference[languages.firstIndex(of: language)!]
                case 4:
                    scores[index-1] += 2 * preference[languages.firstIndex(of: language)!]
                case 5:
                    scores[index-1] += 1 * preference[languages.firstIndex(of: language)!]
                    
                default:
                    print("Out of range")
                }
            }
        }
    }
    return newTable[scores.firstIndex(of: scores.max()!)!][0]
}
