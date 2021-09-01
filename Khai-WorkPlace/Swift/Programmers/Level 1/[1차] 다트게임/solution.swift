func solution(_ dartResult:String) -> Int {
    var temp = ""
    var result: [String] = []
    var scores: [Int] = []

    for word in dartResult {
        if (Int(String(word)) == nil) {
            if word == "*" || word == "#" {
                result[result.count-1] += String(word)
            } else {
                temp += String(word)
                result.append(temp)
                temp = ""
            }
        } else { // 숫자인경우
            temp += String(word)
        }
    }

    for i in 0..<result.count {
        var number = ""
        for j in result[i] {
            if Int(String(j)) == nil {
                switch j {
                    case "S":
                        scores.append(Int(number)! * 1)
                    case "D":
                        scores.append(Int(number)! * Int(number)!)
                    case "T":
                        scores.append(Int(number)! * Int(number)! * Int(number)!)
                    case "*":
                        scores[scores.count-1] *= 2
                        if i > 0 {
                            scores[scores.count-2] *= 2
                        }
                    case "#":
                        scores[scores.count-1] *= -1
                    default:
                        break
                }
                number = ""

            } else {
                number += String(j)
            }
        }
    }

    return scores.reduce(0) { $0 + $1 }
}
