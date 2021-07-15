//
//  solution.swift
//  
//
//  Created by ido on 2021/07/15.
//

import Foundation

func solution(_ s:String) -> String {
    return String(s.sorted{$0 > $1})
}
