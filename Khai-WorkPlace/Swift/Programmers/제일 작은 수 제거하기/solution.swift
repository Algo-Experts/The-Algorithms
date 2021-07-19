func solution(_ arr:[Int]) -> [Int] {
    var arr2=arr
    if let first=arr.firstIndex(of: arr.min()!){
        arr2.remove(at: first)
    }
    if arr2.count==0{
        arr2.append(-1)
    }
    return arr2
}
