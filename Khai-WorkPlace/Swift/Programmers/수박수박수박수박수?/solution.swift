func solution(_ n:Int) -> String {
    var watermelon=""
    
    for i in 1...n{
        if i%2==0{
            watermelon.append("박")
        }else{
            watermelon.append("수")
        }
    }
    
    return watermelon
}
