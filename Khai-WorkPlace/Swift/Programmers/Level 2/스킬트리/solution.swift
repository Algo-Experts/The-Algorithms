import Foundation

func solution(_ skill:String, _ skill_trees:[String]) -> Int {
    var count = skill_trees.count
    for i in skill_trees {
        var skillMap = skill.map{$0}
        var arr = i.filter{skillMap.contains($0)}
        while !arr.isEmpty {
            if skillMap.first == arr.first {
                skillMap.removeFirst()
                arr.removeFirst()
            }else {
                count -= 1
                break
            }
        }
    }
    return count
}
