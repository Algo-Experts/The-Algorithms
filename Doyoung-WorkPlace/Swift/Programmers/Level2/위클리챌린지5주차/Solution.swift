//
//  Solution.swift
//
//
//  Created by Doyoung on 2021/09/04.
//

import Foundation

//사전에 알파벳 모음 'A', 'E', 'I', 'O', 'U'만을 사용하여 만들 수 있는, 길이 5 이하의 모든 단어가 수록되어 있습니다. 사전에서 첫 번째 단어는 "A"이고, 그다음은 "AA"이며, 마지막 단어는 "UUUUU"입니다.
//단어 하나 word가 매개변수로 주어질 때, 이 단어가 사전에서 몇 번째 단어인지 return 하도록 solution 함수를 완성해주세요.
//제한사항
//word의 길이는 1 이상 5 이하입니다.
//word는 알파벳 대문자 'A', 'E', 'I', 'O', 'U'로만 이루어져 있습니다.

func solution5(_ word:String) -> Int {
    var result = 0
    makeDic(index: "", step: 0)
    for index in dictionary.indices {
        guard dictionary[index] != word else {
            result = index + 1
            return result
        }
    }
    return result
}

var dictionary = [String]()

func makeDic(index: String, step: Int) {
    if step == 6 {
        return
    }
    if index != "" {
        dictionary.append(index)
    }
    for char in ["A", "E", "I", "O", "U"] {
        makeDic(index: index+char, step: step+1)
    }
}
