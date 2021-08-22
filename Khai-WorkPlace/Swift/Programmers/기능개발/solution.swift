import Foundation

func solution(_ progresses:[Int], _ speeds:[Int]) -> [Int] {
    var progress = progresses
    var speed = speeds
    var count = 0
    var result = [Int]()

    while progress.isEmpty == false {
        if progress.first! < 100 {
            for i in 0..<progress.count {
                progress[i] += speed[i]
            }

            if count > 0 {
                result.append(count)
                count = 0
            }

        } else {
            progress.removeFirst()
            speed.removeFirst()
            count += 1
        }
    }

    if count > 0 {
        result.append(count)
    }

    return result
}
