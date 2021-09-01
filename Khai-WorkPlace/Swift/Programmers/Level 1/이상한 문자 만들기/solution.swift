func solution(_ s:String) -> String {
    var count = 0
    var result = ""

    for i in s {
        if i == " " {
            count = -1
            result += String(i)
        } else if count % 2 == 0 {
            result += i.uppercased()
        } else {ㄴ
            result += i.lowercased()
        }
        count += 1
    }

    return result
}
