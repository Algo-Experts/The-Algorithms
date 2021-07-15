(알로리즘을 위한)
# The Swift Programming Language 

# Array
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

#### closure(다른 언어에서 주로 람다) 에 대한 이해 필요
## map(_:), filter(_:), reduce(_:) 

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
