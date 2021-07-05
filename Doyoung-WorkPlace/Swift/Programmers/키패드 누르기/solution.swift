//
//  KeyPad.swift
//  AlgorithmNote
//
//  Created by ido on 2021/07/05.
//

import Foundation

// 본 문제는 이미지를 보며 풀어야 편합니다!

// 1. 엄지손가락은 상하좌우 4가지 방향으로만 이동할 수 있으며 키패드 이동 한 칸은 거리로 1에 해당합니다.
// 2. 왼쪽 열의 3개의 숫자 1, 4, 7을 입력할 때는 왼손 엄지손가락을 사용합니다.
// 3. 오른쪽 열의 3개의 숫자 3, 6, 9를 입력할 때는 오른손 엄지손가락을 사용합니다.
// 4. 가운데 열의 4개의 숫자 2, 5, 8, 0을 입력할 때는 두 엄지손가락의 현재 키패드의 위치에서 더 가까운 엄지손가락을 사용합니다.
// 4-1. 만약 두 엄지손가락의 거리가 같다면, 오른손잡이는 오른손 엄지손가락, 왼손잡이는 왼손 엄지손가락을 사용합니다.

func solution(_ numbers:[Int], _ hand:String) -> String {
    
    var result = ""
    var left = 10 //거리를 측정하기위해 10으로 설정
    var right = 12 //거리를 측정하기위해 12로 설정
    
    
    // 키패드 규칙을 가운데 위치한 수들의 가까운 수들의 공통점은 뺀 값의 절대값을 3으로 나누면 공통된 수가 나옵니다.(개같았다...)
    
    func distance(from number: Int) -> String {
        
        let leftDestance = abs((number-left)/3) + abs((number-left)%3)
        let rightDestance = abs((number-right)/3) + abs((number-right)%3)
        
        if leftDestance < rightDestance {
            left = number
            return "L"
        } else if leftDestance > rightDestance{
            right = number
            return "R"
        } else {
            if hand == "left" {
                left = number
                return "L"
            } else {
                right = number
                return "R"
            }
        }
    }//거리구하는 메소드
    
    for num in numbers {
        switch num {
        case 1:
            result.append("L")
            left = 1
        case 4:
            result.append("L")
            left = 4
        case 7:
            result.append("L")
            left = 7
        case 3:
            result.append("R")
            right = 3
        case 6:
            result.append("R")
            right = 6
        case 9:
            result.append("R")
            right = 9
        case 0:
            let shiftNum = 11 // 거리를 측정하기 위해 0을 11로
            result.append(distance(from: shiftNum))
        default:
            result.append(distance(from: num))
        }
    }
    
    return result
}
