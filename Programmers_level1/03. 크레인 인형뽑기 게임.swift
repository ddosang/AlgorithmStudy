import Foundation

func solution(_ board:[[Int]], _ moves:[Int]) -> Int {
    var answer = 0
    var board = board
    var dolls = [Int]()
    
    for move in moves {
        for i in board.indices {
            if board[i][move-1] != 0 {
                let doll = board[i][move-1]
                board[i][move-1] = 0
                
                if let last = dolls.popLast() {
                    if last == doll {
                        answer += 2
                    } else {
                        dolls.append(last)
                        dolls.append(doll)
                    }
                } else {
                    dolls.append(doll)
                }
                break
            }
        }
    }
    return answer
}
