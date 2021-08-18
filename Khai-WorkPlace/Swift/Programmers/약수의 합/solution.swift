func solution(_ n:Int) -> Int {
    var sum: Int = 0
    if n != 0 {
        for index in 1...n {
            if n % index == 0 {
                sum += index
            }
        }
    }
    return sum
}
