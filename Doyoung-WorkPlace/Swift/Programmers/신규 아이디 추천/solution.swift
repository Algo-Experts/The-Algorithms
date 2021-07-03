//
//  RecommandNewId.swift
//  AlgorithmNote
//
//  Created by ido on 2021/07/03.
//

import Foundation

//1. new_id의 모든 대문자를 대응되는 소문자로 치환합니다.[O]
//2. new_id에서 알파벳 소문자, 숫자, 빼기(-), 밑줄(_), 마침표(.)를 제외한 모든 문자를 제거합니다.
//3. new_id에서 마침표(.)가 2번 이상 연속된 부분을 하나의 마침표(.)로 치환합니다.
//4. new_id에서 마침표(.)가 처음이나 끝에 위치한다면 제거합니다.[O]
//5. new_id가 빈 문자열이라면, new_id에 "a"를 대입합니다.
//6. new_id의 길이가 16자 이상이면, new_id의 첫 15개의 문자를 제외한 나머지 문자들을 모두 제거합니다.
//     만약 제거 후 마침표(.)가 new_id의 끝에 위치한다면 끝에 위치한 마침표(.) 문자를 제거합니다.
//7. new_id의 길이가 2자 이하라면, new_id의 마지막 문자를 new_id의 길이가 3이 될 때까지 반복해서 끝에 붙입니다.

func solution(_ new_id:String) -> String {
    
    var userId = new_id.lowercased() // 1단계
    
    for character in userId {
        switch character {
        case "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0","-", "_", "."://😅😅
            break
        default:
            userId = userId.replacingOccurrences(of: String(character), with: "")// String값에서 of 값을 with 값으로 전환
        }
    }

    
    while userId.contains("..") {
        userId = userId.replacingOccurrences(of: "..", with: ".")// of 값을 with 값으로 전환
    } // 3단계
    while userId.last == "." || userId.first == "." {
        userId = userId.trimmingCharacters(in: ["."])
    } // 4단계
   
    if userId.isEmpty {
        userId = "a"
    } // 5단계
    
    guard userId.count >= 16 else {
        if userId.count <= 2 {
            while userId.count != 3 {
                userId = "\(userId)\(userId.last!)"// ! : Optional Forced Unwrapping
            } // 7단계
        }
        return userId
    }
    userId.removeLast(userId.count - 15)
    
    if userId.last == "."{
        userId.removeLast()
    } // 6단계
    
    return userId
}


// 7단계(사용된 swift 문법)
// "\(??)" : String Interpolation, 문자열에 변수를 삽입 ex) let age = 28     print("I'm \(age)") => "I'm 28"

//  guard 구문 : if 구문과 같이 조건문으로 순서가 if문과 반대라고 생각하면 된다.
//  guard (Bool 타입 값) else {
//  예외사항
//  return
//  } --> 예외사항으로 빠지지 않았으면 다음코드 실행
//
//  guard 문을 사용한 이유는 특별한 이유가 없다 if문을 사용해도 문제는 없지만 guard 문의 장점은 특정 조건에 부합하지 않다는 판단이 되면 빠른 종료를 할 수 있고 가독성이 좋다는 점이다(swift 문서에 의하면)

// !: Optional 값을 강제로 언랩핑(추출?)하는 방법이다. 그렇기에 만약 변수가 nil(다른 언어에서 nul?) 값이 었다면 런타임 에러가 발생한다. 그렇기에 가능한 사용을 지양해야 합니다. --> if나 while문을 이용한 Optional 바인딩을 통해 언랩핑 해줍니다. (저는 주로 guard문이나 if문 사용)


// 후기 : String에 대한 이해도가 있으면 쉽게 풀 수 있었던 문제였습니다. 하지만 굳이 swift로 알고리즘을 풀 생각이 아니라면, 굳이 알필요가 없다 생각합니다.(매우 주관적인)

//Best 풀이
//2단계에서 고차함수 filter 및 isNumber, isLetter 사용시 코드량을 단축할 수 있습니다.
// => userId.filter{$0.isNumber || $0.isLetter || $0 == "-" || $0 == "_" || $0 == "."}
