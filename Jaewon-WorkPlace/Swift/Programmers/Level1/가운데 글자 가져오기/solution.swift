//
//  main.swift
//  solution
//
//  Created by Jaewon Park on 2021/08/31.
//

import Foundation


func solution(_ s:String) -> String {
    let offset:Int = s.count / 2
    
    if s.count % 2 != 0 {
        return "\(s[s.index(s.startIndex, offsetBy: offset)])"
    }

    return "\(s[s.index(s.startIndex, offsetBy: offset-1)])\(s[s.index(s.startIndex, offsetBy: offset)])"
}

