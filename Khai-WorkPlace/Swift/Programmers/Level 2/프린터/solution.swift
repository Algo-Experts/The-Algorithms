import Foundation

func solution(_ priorities:[Int], _ location:Int) -> Int {
    
    var queue: [(Int, Int)] = []
    var sortedQueue = priorities.sorted(by : >)
    var result = 0
    
    priorities.enumerated().forEach { (index, property) in
        queue.append((index, property))
    }
    
    while !queue.isEmpty {
        if queue.first!.1 == sortedQueue.first! {
            if queue.first!.0  == location {
                return result + 1
            }
            
            result += 1
            queue.removeFirst()
            sortedQueue.removeFirst()
        } else {
            queue.append(queue.removeFirst())
        }
    }
    
    return result
}
