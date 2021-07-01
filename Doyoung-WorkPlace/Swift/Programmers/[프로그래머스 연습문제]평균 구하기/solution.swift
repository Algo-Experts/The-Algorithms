//
//  solution.swift
//  
//
//  Created by ido on 2021/07/01.
//

import Foundation

//Doy의 풀이
func solution(_ arr:[Int]) -> Double {
    
    // Return 타입이 Double
    
    var sum: Double = 0 // 타입을 선언하지 않으면, var sum = 0 을 type inference로 int 값으로 인지함
    
    let count = Double(arr.count)
    
    for num in 0..<arr.count {  // swift 범위 연산자 ex) 10미만 = '..<10', 10이하 = '...10'
        sum += Double(arr[num])
    }
    
    let result = sum / count
    
    return result
}


//Best 풀이: Higher-order function 사용(reduce)
func bestSolution(_ arr:[Int]) -> Double {
    
    return Double(arr.reduce(0, { $0 + $1}))/(Double)(arr.count)
    // Closuer이해 필요(README 참조)
    
    // -> Double(arr.reduce(0,+))/Double(arr.count) 이렇게 한번 더 줄여짐..
    // 연산자는 중위 연산자로 왼쪽 값이 $0, 오른쪽 값이 $1임을 추론 가능하므로 위 같이 생략가능.(이렇게 까지 간소화 할 필요는 없다 생각)
    
}
