func solution(_ arr:[Int], _ divisor:Int) -> [Int] {
    let answer = arr.filter { $0%divisor == 0 }
    
    if answer.count > 0 {
        return answer.sorted()
    } else {
        return [-1]
    }
}
