//
//  CountOfPY.swift
//  AlgorithmNote
//
//  Created by ido on 2021/07/17.
//

import Foundation

func solution(_ s:String) -> Bool {
    let p = Array(s.lowercased()).filter{ $0 == "p"}
    let y = Array(s.lowercased()).filter{ $0 == "y"}
    
    guard p.count == y.count else { return false }
    
    return true
}
