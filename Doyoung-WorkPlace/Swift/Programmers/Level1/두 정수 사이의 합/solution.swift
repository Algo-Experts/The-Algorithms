//
//  solution.swift
//  
//
//  Created by ido on 2021/07/16.
//

import Foundation

func solution(_ a:Int, _ b:Int) -> Int64 {
   return Int64((a<b ? a...b : b...a).reduce(0){ $0 + $1 }) // reduce 사용
}

// 처음에는 습관처럼 Array를 만들어서 했었으나 테스트4에서 시간 초과가 나와 어처피 Int 범위를 배열로 인지할거 같아 Array 캐스팅 한 걸 지웠더니 통과했습니다.

// 처음 소스 : Int64(Array(a<b ? a...b : b...a).reduce(0){ $0 + $1 })
