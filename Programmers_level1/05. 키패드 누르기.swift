import Foundation

func distance(start: Int, end: Int) -> Int {
    let start_x = (start - 1) % 3
    let start_y = (start - 1) / 3
    let end_x = (end - 1) % 3
    let end_y = (end - 1) / 3
    
    let distance = abs(start_x - end_x) + abs(start_y - end_y)

    return distance
}

func solution(_ numbers:[Int], _ hand:String) -> String {
    var answer = ""
    var left_loca = 10
    var right_loca = 12
    
    for num in numbers {
        let num = (num == 0) ? 11 : num
        
        if num % 3 == 1 {
            answer += "L"
            left_loca = num
        } else if num % 3 == 0 {
            answer += "R"
            right_loca = num
        } else {
            
            let dist_left = distance(start: left_loca, end: num)
            let dist_right = distance(start: right_loca, end: num)
            print(dist_left, dist_right)
            
            if dist_left < dist_right {
                answer += "L"
                left_loca = num
            } else if dist_left > dist_right {
                answer += "R"
                right_loca = num
            } else {
                if hand == "left" {
                    answer += "L"
                    left_loca = num
                } else {
                    answer += "R"
                    right_loca = num
                }
            }
        }
        
    }
    return answer
}
