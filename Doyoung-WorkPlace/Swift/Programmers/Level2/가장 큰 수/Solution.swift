//
//  File.swift
//  
//
//  Created by Doyoung on 2021/08/29.
//

import Foundation

//0 또는 양의 정수가 주어졌을 때, 정수를 이어 붙여 만들 수 있는 가장 큰 수를 알아내 주세요.
//예를 들어, 주어진 정수가 [6, 10, 2]라면 [6102, 6210, 1062, 1026, 2610, 2106]를 만들 수 있고, 이중 가장 큰 수는 6210입니다.
//0 또는 양의 정수가 담긴 배열 numbers가 매개변수로 주어질 때, 순서를 재배치하여 만들 수 있는 가장 큰 수를 문자열로 바꾸어 return 하도록 solution 함수를 작성해주세요.

func solution(_ numbers:[Int]) -> String {
    
    let stringNumbers = numbers.map{ String($0) }
    let result = stringNumbers.sorted{ $0 + $1 > $1 + $0} //String 연산으로 큰 수가 먼저 나오게 sorted
    
    return result.max() == "0" ? "0" : result.joined()

}

// 테스트 11 실패를 해결하는데 많은 시간을 날렸습니다😭😭 (about: 0) ---> [0, 0, 0] 의 경우
