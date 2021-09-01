func solution(_ a:Int, _ b:Int) -> String {
    let days = ["SUN","MON","TUE","WED","THU","FRI","SAT"]
    let months = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    var dayOfWeek = 5
    
    for i in 0..<a-1 {
        dayOfWeek += months[i]
    }
    
    dayOfWeek += b-1
    
    return days[dayOfWeek%7]
}
