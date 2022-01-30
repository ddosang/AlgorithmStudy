import Foundation

func solution(_ n:Int, _ lost:[Int], _ reserve:[Int]) -> Int {
    var clothes = Array(repeating: 1, count: n+1)
    
    for l in lost {
        clothes[l] -= 1
    }
    
    for r in reserve {
        clothes[r] += 1
    }
    
    for i in 1..<clothes.count {
        if clothes[i] == 2 {
            if clothes[i-1] == 0 {
                clothes[i-1] = 1
                clothes[i] = 1
            } else if i < clothes.count - 1 && clothes[i+1] == 0 {
                clothes[i] = 1
                clothes[i+1] = 1
            }
        }
    }

    return clothes.filter {
        $0 > 0
    }.count - 1
}
