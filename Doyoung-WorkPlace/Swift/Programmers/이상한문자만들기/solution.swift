//
//  solution.swift
//  
//
//  Created by ido on 2021/07/21.
//

import Foundation
//TODO: 문자열 s는 한 개 이상의 단어로 구성되어 있습니다. 각 단어는 하나 이상의 공백문자로 구분되어 있습니다. 각 단어의 짝수번째 알파벳은 대문자로, 홀수번째 알파벳은 소문자로 바꾼 문자열을 리턴하는 함수, solution을 완성하세요.
//제한 사항
//문자열 전체의 짝/홀수 인덱스가 아니라, 단어(공백을 기준)별로 짝/홀수 인덱스를 판단해야합니다.
//첫 번째 글자는 0번째 인덱스로 보아 짝수번째 알파벳으로 처리해야 합니다.


func solution(_ s:String) -> String {
    
    let array = s.components(separatedBy: " ").map{ result -> String in // sepatated로 공백기준으로 짤라서 배열 만들기
        var freak = String()
        for (index, element) in result.enumerated() {
            freak.append(index % 2 == 0 ? element.uppercased() : element.lowercased())
        }
        return freak //map으로 enumerated로 짝수는 대문자 홀수는 소문자로
    }
    
    return array.joined(separator: " ") //join을 통해 배열의 요소들간 " "을 추가하여 하나의 문자열로
}


// 생각보다 오래걸렸습니다. 아래와 같이 배열을 string 값으로 합치는 과정에서 당연히 제일 앞과 뒤에 공백을 지워야한다 생각해서 trim을 사용했지만 " try " 이런 경우는 공백이 유지되야했습니다. 결론은 문제를 잘 파악하자🥲
//
//  for freak in array {
//        result.append("\(freak) ")
//    }
//
//    return result.trimmingCharacters(in: [" "])
