//
//  Solution.swift
//  
//
//  Created by Doyoung on 2021/10/04.
//

import Foundation

//두 개의 단어 begin, target과 단어의 집합 words가 있습니다. 아래와 같은 규칙을 이용하여 begin에서 target으로 변환하는 가장 짧은 변환 과정을 찾으려고 합니다.
//1. 한 번에 한 개의 알파벳만 바꿀 수 있습니다.
//2. words에 있는 단어로만 변환할 수 있습니다.

// 변환할 수 없는 경우에는 0를 return 합니다.

//Input 〉    "hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]
//Expected 〉    4

//Input 〉    "hit", "cog", ["hot", "dot", "dog", "lot", "log"]
//Expected 〉    0

func solution(_ begin:String, _ target:String, _ words:[String]) -> Int {
    
    var result = [String]()
    var visited = [Bool](repeating: false, count: words.count)
    
    func dfs(start: String) -> Int{
        result.append(start)
        guard !checkLetter(start, target) else {

            return result.count
        }
        
        for index in words.indices {
            if !visited[index] && checkLetter(start, words[index]) {
                print("\(start) & \(words[index])")
                visited[index] = true
                return dfs(start: words[index])
            }
        }
        return 0
    }
    
    if !words.contains(target) {
        return 0
    }
    return dfs(start: begin)
}

func checkLetter(_ first : String, _ second : String) -> Bool {
    var counting = 0
    let firstWordLetters = first.map{ String($0) }
    let secondWordLetters = second.map{ String($0) }
    for index in firstWordLetters.indices {
        if firstWordLetters[index] != secondWordLetters[index] {
            counting += 1
        }
    }
    return counting == 1 ? true : false
}
