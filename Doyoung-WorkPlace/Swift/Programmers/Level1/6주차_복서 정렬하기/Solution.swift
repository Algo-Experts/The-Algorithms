//
//  File.swift
//  
//
//  Created by Doyoung on 2021/09/13.
//

import Foundation

/*
복서 선수들의 몸무게 weights와, 복서 선수들의 전적을 나타내는 head2head가 매개변수로 주어집니다. 복서 선수들의 번호를 다음과 같은 순서로 정렬한 후 return 하도록 solution 함수를 완성해주세요.

 - 전체 승률이 높은 복서의 번호가 앞쪽으로 갑니다. 아직 다른 복서랑 붙어본 적이 없는 복서의 승률은 0%로 취급합니다.

 - 승률이 동일한 복서의 번호들 중에서는 자신보다 몸무게가 무거운 복서를 이긴 횟수가 많은 복서의 번호가 앞쪽으로 갑니다.

 - 자신보다 무거운 복서를 이긴 횟수까지 동일한 복서의 번호들 중에서는 자기 몸무게가 무거운 복서의 번호가 앞쪽으로 갑니다.

 - 자기 몸무게까지 동일한 복서의 번호들 중에서는 작은 번호가 앞쪽으로 갑니다.

 ex) =>   [50,82,75,120]    ["NLWL","WNLL","LWNW","WWLN"]    [3,4,1,2]
          [145,92,86]    ["NLW","WNL","LWN"]    [2,3,1]
          [60,70,60]    ["NNN","NNN","NNN"]    [2,1,3]
 */

func solutionSithWeeks(_ weights:[Int], _ head2head:[String]) -> [Int] {

    //#1. 승률 array 생성
    var winRates = [Double]()
    
    head2head.forEach {
        let win = Array($0).filter{ $0 == "W"}.count
        let lose = Array($0).filter{ $0 == "L"}.count
        let rate = Double(win) / Double(win + lose) * 100
        winRates.append(rate.isNaN ? 0.0 : rate)
    }
    
    //#2. 자기보다 무거운 상대 이긴횟수 array생성
    var winHeaviers = [Int]()
    
    for index in weights.indices {
        var count = 0
        
        let winOrLose = Array(head2head[index])
        for secondIndex in winOrLose.indices {
            if winOrLose[secondIndex] == "W", weights[secondIndex] > weights[index] {
                count += 1
            }
        }
        
        winHeaviers.append(count)
    }
    
    //#3. Boxer array 생성
    var boxers: [Boxer] {
        var boxers = [Boxer]()
        for index in weights.indices {
            boxers.append(Boxer(id: index+1, weight: weights[index], winRate: winRates[index], winHeavier: winHeaviers[index]))
        }
        return boxers
    }
    
    //#4. result 계산
    let result = boxers.sorted {
        if $0.winRate == $1.winRate {
            guard $0.winHeavier == $1.winHeavier else {
                return $0.winHeavier > $1.winHeavier
            }
            guard $0.weight == $1.weight else {
                return $0.weight > $1.weight
            }
            return $0.id < $1.id
        } else {
            return $0.winRate > $1.winRate
        }
    }
    
    return result.map { $0.id }
}

// Model
struct Boxer {
    var id: Int
    var weight: Int
    var winRate: Double
    var winHeavier: Int
}
