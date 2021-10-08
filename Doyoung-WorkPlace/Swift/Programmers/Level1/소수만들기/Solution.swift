//
//  Solution.swift
//  
//
//  Created by Doyoung on 2021/10/08.
//

import Foundation

//주어진 숫자 중 3개의 수를 더했을 때 소수가 되는 경우의 개수를 구하려고 합니다. 숫자들이 들어있는 배열 nums가 매개변수로 주어질 때, nums에 있는 숫자들 중 서로 다른 3개를 골라 더했을 때 소수가 되는 경우의 개수를 return 하도록 solution 함수를 완성해주세요.
func solution(_ nums:[Int]) -> Int {
    var sums = [Int]()
    for first in 0..<nums.count - 2 {
        for second in first+1..<nums.count {
            for third in second+1..<nums.count {
                sums.append(nums[first] + nums[second] + nums[third])
            }
        }
    }

    return sums.filter{ $0.isPrimeNumber() }.count
}

extension Int {
    func isPrimeNumber() -> Bool {
        for index in 2..<self {
            if self%index == 0 {
                return false
            }
        }
        return true
    }
}
