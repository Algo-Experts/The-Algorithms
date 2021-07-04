//
//  HidePhoneNumber.swift
//  AlgorithmNote
//
//  Created by ido on 2021/07/04.
//

//전화번호가 문자열 phone_number로 주어졌을 때, 전화번호의 뒷 4자리를 제외한 나머지 숫자를 전부 *으로 가린 문자열을 리턴하는 함수, solution을 완성해주세요.

import Foundation

func solution1(_ phoneNumber: String) -> String {
    
    let result = "\(String(repeating: "*", count: phoneNumber.count-4))\(phoneNumber.suffix(4))"
    
    return result
}


// String.prefix(<#T##maxLength: Int##Int#>) & String.suffix(<#T##maxLength: Int##Int#>)
// 앞에서 Int값만큼 가져오기 & 뒤에서 Int값만큼 가져오기
