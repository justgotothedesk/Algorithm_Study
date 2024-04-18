# 문제 설명 : 배열 arr이 주어진다. 이 때, 가로가 세로보다 크거나 같다면, 가로를 2배 줄이고 나눈 배열에서 큰 값을 남겨라. 같을 경우 아무 값이나 남기면 된다.
# 반대로, 세로가 가로보다 크다면, 세로를 2배 줄이고 나눈 배열에서 작은 값을 남겨라. 이 역시, 같을 경우 아무 값이나 남기면 된다.
# 그 과정을 k번 반복하라.

def solution(arr, k):
    for _ in range(k):
        row = len(arr)
        col = len(arr[0])
        if row == 1 and col == 1:
            break
          
        if col >= row:
            col //= 2
            temp = [[]*col for _ in range(row)]
            for i in range(row):
                for j in range(col):
                    if arr[i][j*2] >= arr[i][j*2+1]:
                        temp[i].append(arr[i][j*2])
                    else:
                        temp[i].append(arr[i][j*2+1])
        else:
            row //= 2
            temp = [[]*col for _ in range(row)]
            for i in range(row):
                for j in range(col):
                    if arr[i*2][j] <= arr[i*2+1][j]:
                        temp[i].append(arr[i*2][j])
                    else:
                        temp[i].append(arr[i*2+1][j])
        arr = temp

    answer = arr
    
    return answer
