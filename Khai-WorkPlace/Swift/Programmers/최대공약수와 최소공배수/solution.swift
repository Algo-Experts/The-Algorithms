func solution(_ n:Int, _ m:Int) -> [Int] {
    var GCD = 0
    var LCM = 0
    var small = n < m ? n : m
    var big = n > m ? n : m
    

    for num in 1...small {
        if n % num == 0 && m % num == 0 {
            GCD = num
        }
    }

    for num in big...(n * m) {
        if num % n == 0 && num % m == 0 {
            LCM = num
            break
        }
    }
    return [GCD, LCM]
}
