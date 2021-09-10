import Foundation

func solution(_ brown:Int, _ yellow:Int) -> [Int] {
    let half = Int(sqrt(Double(yellow)))
  
    for width in half...yellow {
        for height in 1...width {
            guard yellow == width * height else { continue }
            if brown == ((width + 2) * 2) + (height * 2) {
                return [width + 2, height + 2]
            }
        }
    }
    return []
}
