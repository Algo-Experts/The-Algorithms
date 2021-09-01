func solution(_ s:String) -> String {
    let len: Int = s.count
    let start = s.index(s.startIndex, offsetBy: (len-1)/2)
    let end = s.index(s.startIndex, offsetBy: len/2)
    return String(s[start...end])
}
