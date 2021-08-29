//
//  solution.swift
//  
//
//  Created by ido on 2021/07/15.
//

import Foundation

//문자열로 구성된 리스트 strings와, 정수 n이 주어졌을 때, 각 문자열의 인덱스 n번째 글자를 기준으로 오름차순 정렬하려 합니다. 예를 들어 strings가 ["sun", "bed", "car"]이고 n이 1이면 각 단어의 인덱스 1의 문자 "u", "e", "a"로 strings를 정렬합니다.
//인덱스 1의 문자가 같은 문자열이 여럿 일 경우, 사전순으로 앞선 문자열이 앞쪽에 위치합니다.

func solution(_ strings:[String], _ n:Int) -> [String] {
    
    return strings.sorted(by: {
        guard Array($0)[n] != Array($1)[n] else { //String 요소를 배열로 변경후 비교
            return $0 < $1 // 같을경우는 오름차순
        }
        return Array($0)[n] < Array($1)[n] // 다를 경우는 n 글자를 기준으로 오름차순
    })
    
}


// 삼항 연산자를 사용할 경우 코드가 간략해집니다.
// return strings.sorted(by: { Array($0)[n] !=  Array($1)[n] ? Array($0)[n] < Array($0)[n] : $0 < $1})
