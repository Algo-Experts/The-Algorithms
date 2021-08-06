func solution(_ strings:[String], _ n:Int) -> [String] {
    var result:[String] = []
    
    result = strings.sorted{
        Array($0)[n] == Array($1)[n] ? $0 < $1 : Array($0)[n] < Array($1)[n]
    }
    
    // 비교하는 문자가 같을 경우 전체 비교 정렬 아닐시 문자값으로만 비교 정렬
    
    return result
}
