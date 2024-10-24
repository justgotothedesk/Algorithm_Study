def solution(mats, park):
    answer = -1
    
    for mat in mats:
        for i in range(len(park)):
            for j in range(len(park[0])):
                count = 0
                
                for row in range(mat):
                    for col in range(mat):
                        if (row+i >= len(park)) or (col+j >= len(park[0])):
                            continue
                        if park[i+row][j+col] == "-1":
                            count += 1
                
                if count == mat**2:
                    answer = max(answer, mat)
                
    return answer
