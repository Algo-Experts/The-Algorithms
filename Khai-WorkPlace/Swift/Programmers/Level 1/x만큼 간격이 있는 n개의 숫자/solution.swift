func solution(_ x:Int, _ n:Int) -> [Int64] {
    var sum:[Int]=[]
    
    for i in 0..<n{
        sum.append((i+1)*x)
    }
    return sum.map{Int64($0)} //Int64로 변환
}
