func solution(_ n:Int) -> Int {
    var answer = 0
    var array = [Bool](repeating: true, count: n + 1)
    for i in 2 .. < n + 1 {
        if array[i] {
            answer += 1
            for j in 2..<Int(n / i) + 1 {
                array[i * j] = false
            }
        }
    }
    return answer
}
