//
//  Solution.swift
//  
//
//  Created by ido on 2021/08/01.
//

import Foundation

//임의의 양의 정수 n에 대해, n이 어떤 양의 정수 x의 제곱인지 아닌지 판단하려 합니다.
//n이 양의 정수 x의 제곱이라면 x+1의 제곱을 리턴하고, n이 양의 정수 x의 제곱이 아니라면 -1을 리턴하는 함수를 완성하세요.

func solution15(_ n:Int64) -> Int64 {
    
    let squareRoot = Int64(sqrt(Double(n))) //sqrt = 제곱근구하는 메소드
    let trueResult = squareRoot + 1
    return squareRoot * squareRoot == n ? trueResult * trueResult : Int64(-1)
    
}

// 프로그래머스에서 Foundation이 import되어 있지 않아 sqrt() 사용할때 에러나서 뻘짓을 좀 했습니다. import를 확인하자!
