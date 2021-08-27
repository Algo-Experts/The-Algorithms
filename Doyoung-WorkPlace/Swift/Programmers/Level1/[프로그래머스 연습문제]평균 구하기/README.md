1. 문제 출처 : https://programmers.co.kr/learn/courses/30/lessons/12944

swift 특징:
1. type inference: https://docs.swift.org/swift-book/ReferenceManual/Types.html (마지막문단에 정확한 설명이 있습니다. 영문주의❗️)

swift 문법:
##Closure (가동석 문제로 추후 재업로드 예정)
1. closure는 C의 Block 이나 다른 언어의 Lamda와 유사합니다. func(함수) 역시 클로저의 한 형태입니다.
2. 클로저의 3가지 특징
- 이름이 있으면서 어떤 값도 획득하지 않는 전역함수의 형태
- 이름이 있으면서 다른 함수 내부의 값을 획득할 수 있는 중첩된 함수의 형태
- 이름이 없고 주변 문맥에 따라 값을 획득할 수 있는 축약 문법으로 작성한 형태

3. closure 는 일반적인 경우에 깔끔한 문법을 가짐(저는 너무 싫어요..)
- parameter(매개변수) 와 반환 값을 type inference로 생략가능해짐
- 단일 표현식일 경우, 암시적으로 이를 반환 값으로 취급
- 축약된 전달인자 이름을 사용($0, $1, $2 ...)
- 후앵 클로저 문법 사용

4. 클로저 표현
{ (매개변수들)  -> 반환 타입 in
    실행코드
}

정확한 정보는:
(애플공식문서 - 추천👍)https://docs.swift.org/swift-book/LanguageGuide/Closures.html
(번역1 - 민소네)http://minsone.github.io/mac/ios/swift-closure-summary
(번역2 - 야곰)https://blog.yagom.net/555/


Best 풀이에 사용된 reduce 고차함수에서 사용되는 closure를 보겠습니다.

reduce 고차함수는 
func reduce<Result>(_ initialResult: Result, _ nextPartialResult: (Result, Element) throws -> Result) rethrows -> Result 과 같이 짜여진 함수입니다.

문제를 풀기 위하여 우리에게 필요한것은 배열의 합이니
reduce(시작, 시작 + 다음) 와 같아집니다.

2번째 parameter에다가 식을 넣어야 함으로 closure를 사용합니다

arr.reduce(0, { (x: Int, y: Int) -> Int in
    return x + y
})

swift는 type inference로  인해 parameter 와 리턴값의 타입을 생략해서 클로저를 생성할 수 있습니다.
arr.reduce(0, { x, y  in
    return x + y
})

클로저가 단일 표현식일 경우 이를 반환 값으로 취급되어 다음과 같이 생략 가능해집니다.
arr.reduce(0, { x, y  in
   x + y
})

클로저에서는 축약된 전달인자를 사용하여 코드를 줄이기도 합니다.
arr.reduce(0, {$0 + $1})



