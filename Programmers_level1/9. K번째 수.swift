import Foundation

func solution(_ array:[Int], _ commands:[[Int]]) -> [Int] {

    var answer: [Int] = []

    for i in commands.indices {
        answer.append(array[(commands[i][0] - 1)..<commands[i][1]].sorted()[commands[i][2]-1])
    }
    
    return answer
}
