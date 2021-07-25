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


# Optional
: 옵셔널은 nil값이 존재할 수 있는 타입들을 지칭합니다. ex) Optional<String>, Optional<Int> ...

예를 보면 옵셔널 타입이 뭔지 이해하 실 수 있습니다.
> String 타입을 Int 타입으로 케스팅을 해보겠습니다.
```swift
let strNumber = "123"

let intCasting = Int(strNumber)
print(type(of: intCasting) // -> Optional<Int>
```
위 같이 String 값을 Int 타입으로 케스팅 한 다음, 타입을 출력하면 Int가 아니라 "Optional<Int>" 가 나옵니다. 🤔

```swift
let strNomal = "abc"

let intCasting = Int(strNomal)
print(intCasting) // -> nil
```
만약 숫자형 문자가 아닌 영어나 다른 언어를 int로 케스팅하는 경우 nil 이 출력됩니다.

즉, 옵셔널타입이란 값이 존재하지 않을 수도 있는 경우의 타입을 말합니다.

nil값이 필요한 옵셔널 타입의 프로퍼티(변수, 상수)를 생성하고 싶을 시 타입뒤에 ? 를 추가해주시면 됩니다.
ex) var str: String?,var num: Int? ...


> 옵셔널타입은 항시 nil 값에 대해서 처리를 해줘야 합니다. 방법으로는 "Forced Unwrapping" 과 "Optional Binding" 이 존재합니다.

## Forced Unwrapping
> ! 를 통해서 옵셔널 값을 처리할 수 있습니다.

```swift
et strNumber = "123"

let intCasting = Int(strNumber)!
print(type(of: intCasting) // -> Int
```
! 를 추가했더니 전과 다르게 Int 타입을 출렸했습니다.

❗️하지만 Forced Unwrapping 런타임 오류에 취약합니다. 그래서 nil값이 존재하지 않는다고 확신한 경우에만 사용해야 합니다.
```swift
let strNomal = "abc"

let intCasting = Int(strNomal)
print(intCasting!) // 언래핑시 Error --> Fatal error: Unexpectedly found nil while unwrapping an Optioanl value. 
```


## Optional Binding

> 옵셔널 바인딩은 조건문(if, while, guard)을 통하여 nil 값을 처리하는 방식입니다.

ex) if로
```swift
let strNomal = "abc"

let intCasting = Int(strNomal)

if let binding = intCasting {
    print("\(binding)")
} else {
    print("binding is nil") // nil 처리
}

// -> binding is nil

```

ex) guard문(my love)
```swift
let strNomal = "abc"

let intCasting = Int(strNomal)

guard let binding = intCasting else {
    
    return
}

print(binding) // -> 아무값 안나옴. nil 에 대해 출력을 원하면 else 블록안에다 추가하면 되요!
```

## guard문 을 사랑하는 이유🤔🤔

### guard문이 if문과 다른점
- ~이름이 멋있다.~
- else를 먼저 catch 함으로 빠른 종료가 가능하다.
- 메소드 내에서만 사용가능하다.
-  **옵셔널 바인딩한 상수의 Scope가 다르다**❗️
> if 문의 경우
```swift
func optionalBindingIf() {
    if let binding = intCasting {
        print("\(binding)")
    } else {
        print("binding is nil") // nil 처리
    }
    let message = binding // Error-> Cannot fint 'binding' in scope : if문 밖에서는 바인딩한 상수에 접근 할 수 없음! ☹️
}
```
>guard문의 경우
```swift
func optionalBindingGuard() {
    guard let binding = intCasting else {
        return
    }
    let message = binding // 바인딩한 값을 guard 구문 밖에서 사용가능합니다! 👍
}
```
