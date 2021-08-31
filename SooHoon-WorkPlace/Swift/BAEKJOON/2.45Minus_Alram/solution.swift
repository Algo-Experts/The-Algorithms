//
//  solution.swift
//  BaekJoonSolution
//
//  Created by SooHoon on 2021/08/27.
//

import Foundation

var input = readLine()

if let input = input {
    var inputs = input.components(separatedBy: " ")
    
    var H = inputs[0]
    var M = inputs[1]
    
    var solutionH = 0
    var solutionM = 0
    
    switch (Int(M)!) {
    case 0...44 :
        solutionM = Int(M)! + 15
        solutionH = Int(H)! - 1
        break

    case 45...59 :
        solutionM = 15 - (60 - Int(M)!)
        solutionH = Int(H)!
        break

    default: break
    }
    print("\(solutionH) \(solutionM)")
}



//
//  solution.swift
//  BaekJoonSolution
//
//  Created by SooHoon on 2021/08/27.
//

import Foundation

var H = readLine()
var M = readLine()
var solutionH = 0
var solutionM = 0

switch (Int(M!)!) {
case 0...44 :
    solutionM = Int(M!)! + 15
    solutionH = Int(H!)! - 1
    break

case 45...59 :
    solutionM = 15 - (60 - Int(M!)!)
    solutionH = Int(H!)!
    break

default: break
}
print("\(solutionH) \(solutionM)")



//
//  solution.swift
//  BaekJoonSolution
//
//  Created by SooHoon on 2021/08/27.
//

import Foundation

//var H = readLine(); var M = readLine()

var input = readLine()

//if let input = input {
//    var H = input.components(separatedBy: " ")
//    var M = input.components(separatedBy: " ")
//    var solutionH = 0
//    var solutionM = 0
////    var array =
//    switch (Int(M!)!) {
//    case 0...44 :
//        solutionM = Int(M!)! + 15
//        solutionH = Int(H!)! - 1
//        break
//
//    case 45...59 :
//        solutionM = 15 - (60 - Int(M!)!)
//        solutionH = Int(H!)!
//        break
//
//    default: break
//    }
//    print("\(solutionH) \(solutionM)")
//}

var H = readLine()
var M = readLine()
var solutionH = 0
var solutionM = 0

switch (Int(M!)!) {
case 0...44 :
    solutionM = Int(M!)! + 15
    solutionH = Int(H!)! - 1
    break

case 45...59 :
    solutionM = 15 - (60 - Int(M!)!)
    solutionH = Int(H!)!
    break

default: break
}
print("\(solutionH) \(solutionM)")


