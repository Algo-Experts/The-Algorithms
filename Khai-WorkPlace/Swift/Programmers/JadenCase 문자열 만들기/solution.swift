func solution(_ s:String) -> String {
    let words = s.components(separatedBy: " ")
    var counts = Array(repeating: [String](), count: words.count)
    var answer = Array(repeating: String(), count: words.count)
    for i in 0..<words.count {
        counts[i] = words[i].map{String($0).lowercased()}
        if counts[i] != [] {
        counts[i][0] = counts[i][0].uppercased()
        }
        answer[i] = counts[i].joined(separator: "")
    }
 
    return answer.joined(separator: " ")
}
