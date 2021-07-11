fun main(args: Array<String>) {
    val (a, b) = readLine()!!.split(' ').map(String::toInt)
    var lenStar : String = ""

    for(i in 1..a){
        star += "*"
    }
    for(i in 1..b){
        println(star)
    }
}
