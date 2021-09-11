func solution(_ n:Int64) -> Int64 {
    let str = String(n)
    let answer = String(str.sorted(by: >))
    
    return Int64(answer)!
}
