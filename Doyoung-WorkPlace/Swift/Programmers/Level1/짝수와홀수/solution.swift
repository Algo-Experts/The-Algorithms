//
//  solution.swift
//  
//
//  Created by ido on 2021/07/13.
//

import Foundation

func solution(_ num:Int) -> String {
    
    guard num%2 == 0 else {
        return "Odd"
    }
    return "Even"
}
