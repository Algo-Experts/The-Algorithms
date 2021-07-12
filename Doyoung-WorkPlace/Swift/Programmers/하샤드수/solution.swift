//
//  File.swift
//  
//
//  Created by ido on 2021/07/12.
//

import Foundation

//양의 정수 x가 하샤드 수이려면 x의 자릿수의 합으로 x가 나누어져야 합니다. 예를 들어 18의 자릿수 합은 1+8=9이고, 18은 9로 나누어 떨어지므로 18은 하샤드 수입니다. 자연수 x를 입력받아 x가 하샤드 수인지 아닌지 검사하는 함수, solution을 완성해주세요.

func solution(_ x:Int) -> Bool {
    let sum = String(x).map{Int(String($0))!}.reduce(0, +) // 자리수 합 구하기, string으로 케스팅한 후에, map으로 ing 배열로 생성, reduce로 배열 합 구하기.
    
    return x % sum == 0
    
}
