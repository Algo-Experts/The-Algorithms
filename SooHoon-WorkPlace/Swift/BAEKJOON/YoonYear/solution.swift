//
//  solution.swift
//  BaekJoonSolution
//
//  Created by SooHoon on 2021/08/27.
//

import Foundation

var input = readLine()
var result  = 0

//if let input = input {
//    let inputs = input.components(separatedBy: " ")
////    print(inputs)
//}

if (Int(input!)!%4) == 0 {
    if (Int(input!)!%100) != 0 || (Int(input!)!%400) == 0 {
        print(1)
    }else {
        print(0)
    }
}else {
    print(0)
}

