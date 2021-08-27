//
//  StringIntAndEnglish.swift
//  AlgorithmNote
//
//  Created by ido on 2021/07/09.
//

import Foundation

func solution(_ s:String) -> Int {
    
    var pram = s
    
    if pram.contains("zero") {
        pram = pram.replacingOccurrences(of: "zero", with: "0")
    }// 0을 세팅 안해서 통과를 못하고 있었음..(속도문제아님)
    
    if pram.contains("one") {
        pram = pram.replacingOccurrences(of: "one", with: "1")
    }
    
    if pram.contains("two") {
        pram = pram.replacingOccurrences(of: "two", with: "2")
    }
    
    if pram.contains("three") {
        pram = pram.replacingOccurrences(of: "three", with: "3")
    }
    
    if pram.contains("four") {
        pram = pram.replacingOccurrences(of: "four", with: "4")
    }
    
    if pram.contains("five") {
        pram = pram.replacingOccurrences(of: "five", with: "5")
    }
    
    if pram.contains("six") {
        pram = pram.replacingOccurrences(of: "six", with: "6")
    }
    
    if pram.contains("seven") {
        pram = pram.replacingOccurrences(of: "seven", with: "7")
    }
    
    if pram.contains("eight") {
        pram = pram.replacingOccurrences(of: "eight", with: "8")
    }
    
    if pram.contains("nine") {
        pram = pram.replacingOccurrences(of: "nine", with: "9")
    }
    
    let result = Int(pram) ?? 0;
    
    return result
    
}

// Using Enumerated
// Thanks Jasper
func bestSolution(_ s:String) -> Int {
    var result = s
    
    let stringNum = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    
    for (num, str) in stringNum.enumerated() {
        if result.contains(str)  {
            result = result.replacingOccurrences(of: str, with: String(num))
        }
    }
    
    return Int(result)!
}
