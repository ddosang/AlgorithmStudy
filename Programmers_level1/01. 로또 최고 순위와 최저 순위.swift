import Foundation

func calculateOrder(count: Int) -> Int {
    return (count <= 1) ? 6 : 7-count
}

func solution(_ lottos:[Int], _ win_nums:[Int]) -> [Int] {
    var answer = [Int]()
    var matchCount = 0
    var zeroCount = 0
    
    var highOrder = 0
    var lowOrder = 0
    
    for lotto in lottos {
        for num in win_nums {
            if lotto == num {
                matchCount += 1
                break
            }
        }
    }
    
    for lotto in lottos {
        if lotto == 0 {
            zeroCount += 1
        }
    }
    
    highOrder = calculateOrder(count: matchCount+zeroCount)
    lowOrder = calculateOrder(count: matchCount)
    
    answer.append(highOrder)
    answer.append(lowOrder)
    
    
    return answer
}
