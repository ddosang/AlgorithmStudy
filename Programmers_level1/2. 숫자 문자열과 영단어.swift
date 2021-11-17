import Foundation

func solution(_ s:String) -> Int {
    var answer: String = ""
    var local: String = ""
    
    let dict = [
        "zero": "0",
        "one" : "1",
        "two" : "2",
        "three" : "3",
        "four" : "4",
        "five" : "5",
        "six" : "6",
        "seven" : "7",
        "eight" : "8",
        "nine" : "9"
    ]
    
    for c in s {
        if c.isNumber {
            answer += String(c)
        } else {
            local += String(c)
            if let word = dict[local] {
                answer += word
                local = ""
            }
        }
    }
    
    return Int(answer)!
}
