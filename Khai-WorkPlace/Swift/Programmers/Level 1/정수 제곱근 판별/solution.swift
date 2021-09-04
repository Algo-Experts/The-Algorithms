func solution(_ n:Int64) -> Int64 {
    var answer = 1
    while answer*answer <= n {
        if answer*answer == n {
            return Int64((answer+1)*(answer+1))
        }
        answer += 1
    }
    return -1
}
