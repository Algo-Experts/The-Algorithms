//
//  solution.swift
//  
//
//  Created by ido on 2021/07/15.
//

import Foundation

//array의 각 element 중 divisor로 나누어 떨어지는 값을 오름차순으로 정렬한 배열을 반환하는 함수, solution을 작성해주세요.
//divisor로 나누어 떨어지는 element가 하나도 없다면 배열에 -1을 담아 반환하세요.

func solution(_ arr:[Int], _ divisor:Int) -> [Int] {
    
    let result = arr.filter{ $0 % divisor == 0}.sorted()
    // 1. filter를 통해 나누어 떨어지는 것들만 배열에 남긴다.
    // 2. sorted로 오름차순 정렬
    
    guard result != [] else{
        return [-1] // 결과가 빈값이면 [-1] 리턴
    }
    
    return  result
}
