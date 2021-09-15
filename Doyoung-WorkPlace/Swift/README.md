(알로리즘을 위한)
# The Swift Programming Language 

# Array 다루기
> 빈 배열 생성
```swift
var array1 : [Any] = []
var array2 = [Any]()
var array3 : Array<Any> = []
```

> 크기가 정해진 배열 생성
```swift
var array4 = [String](repeating: "A", count: 4) // ["A", "A", "A"]

```

>여러 타입이 들어갈 수 있는 배열
Any 타입으로 만들기
```swift
var arrayAny: [Any] = [1,2,"A","B"] 

```

## map(_:), filter(_:), reduce(_:) 
#### closure(다른 언어에서 주로 람다) 에 대한 이해 필요

>map(_:)
배열 요소들을 조건에 따라 새롭게 구성하는 메소드입니다
ex)
```swift
let cast = ["Do", "Young", "Lee"]
let lowercaseNames = cast.map { $0.lowercased() } // ["do", "young", "lee"] 
let letterCounts = cast.map { $0.count } // [2, 5, 3]
```

>filter(_:)
배열 요소 중 조건에 따라 거르는 메소드입니다.
```swift
let num = [1, 2, 3, 4, 5, 6, 7]
let evenNum = num.filter{ $0 % 2 == 0 } // [2, 4, 6]

```

>reduce(_:)
배열의 요소들을 하나의 값으로 만드는 메소드입니다.
```swift
let numbers = [1, 2, 3, 4]
let numbersSum = num.reduce(0) { $0 + $1 } // numberSum == 10

```

## enumerated
Returns a sequence of pairs (n, x), where n represents a consecutive integer starting at zero and x represents an element of the sequence.

> 0부터 시작하는 연속적인 정수를 n, 시퀀스의 요소를 x로 정하면, (n,x)의 시퀀스를 리턴합니다.
```swift
for (n, c) in "Swift".enumerated() {
    print("\(n): '\(c)'")
}
// Prints "0: 'S'"
// Prints "1: 'w'"
// Prints "2: 'i'"
// Prints "3: 'f'"
// Prints "4: 't'"
```
