//
//  File.swift
//  
//
//  Created by Doyoung on 2021/09/24.
//

import Foundation

//주어진 항공권을 모두 이용하여 여행경로를 짜려고 합니다. 항상 "ICN" 공항에서 출발합니다.
//항공권 정보가 담긴 2차원 배열 tickets가 매개변수로 주어질 때, 방문하는 공항 경로를 배열에 담아 return 하도록 solution 함수를 작성해주세요.
//만일 가능한 경로가 2개 이상일 경우 알파벳 순서가 앞서는 경로를 return 합니다.

//ex) 입력값 〉    [["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]  기댓값 〉    ["ICN", "JFK", "HND", "IAD"]
//ex) 입력값 〉    [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL", "SFO"]] 기댓값 〉    ["ICN", "ATL", "ICN", "SFO", "ATL", "SFO"]

func solution(_ tickets:[[String]]) -> [String] {
    
    let tickets = tickets.sorted{ $0[1] < $1[1]} //도착지 기준으로 정렬(문제 조건)
    var result = [String]()
    var visited = [Bool](repeating: false, count: tickets.count) // 노드 방문 여부

    // DFS 재귀함수 이용
    func dfs(start: String) {
        if result.count == tickets.count {
            result.append(start)
            return
        }
        for index in tickets.indices {
            if tickets[index][0] == start && !visited[index] {
                result.append(start)
                visited[index] = true
                dfs(start: tickets[index][1])
                
                if result.count == tickets.count + 1 {
                    return
                }
                result.removeLast() //재탐색
                visited[index] = false
            }
        }
    }
    dfs(start: "ICN") // 시작 노드는 "ICN"이라 문제에서 명시
    return result
}
