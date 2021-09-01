func solution(_ a:Int, _ b:Int) -> Int64 {

    let minValue = a < b ? a : b
    let maxValue = a > b ? a : b

    var value: Int64 = 0
    for i in minValue...maxValue {
        value += i
    }

    return value
}
