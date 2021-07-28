func solution(_ s:String) -> String {
    let splited = s.split(separator: " ")
    var number: [Int] = []

    for i in splited {
        guard let number = Int(i) else { return " " }
        number.append(number)
    }

    return "\(number.min()!) \(number.max()!)"
}
