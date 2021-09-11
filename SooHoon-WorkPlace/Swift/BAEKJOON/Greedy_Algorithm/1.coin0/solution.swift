//
//  main.swift
//  solution
//
//  Created by SooHoon on 2021/09/05.
//

import Foundation

var input = readLine()
var N :Int = 0
var K :Int = 0

var coinK: Int = 1
var arrayKind: Array<Int> = []
// 결과 값 선언
var result :Int = 0

if let input = input {
    var inputs = input.components(separatedBy: " ")
    
    N = Int(inputs[0])!
    K = Int(inputs[1])!
}

for kind in 1...N {
    // 코인 종류 출력
    print(coinK)
    // 배열에 넣기
    arrayKind.append(coinK)
    
    // 다음 코인 종류 만들기
    if kind % 2 == 0 {
        coinK *= 2
    } else {
        coinK *= 5
    }
}

print("count: \(arrayKind.count)")
for i in 1...arrayKind.count {
//    print("i: ",i)
//    print("arrayKind: \(arrayKind[arrayKind.count - i])")
//    print("result: \(result)")
    if (K / arrayKind[arrayKind.count - i]) > 0 || (K % arrayKind[arrayKind.count - i] > 0){
        result += (K / arrayKind[arrayKind.count - i])
        K = K % arrayKind[arrayKind.count - i]
    }else {
        
    }
}
print("결과 : ", result)

