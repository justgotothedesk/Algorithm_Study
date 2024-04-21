# 인덱스의 차이가 가장 작은 것이 우선 순위이므로, 현재 오름차순으로 주어진 sequence 배열의 특성에 따라서 뒤에서부터 탐색을 해준다.
# 탐색에서 총 합이 k보다 클 경우에 마지막 값을 빼주면서 k와 같아질 때까지 반복 수행한다.
# 그리고 문제 두 번째 조건에서 인덱스의 차이가 동일하다면 인덱스 그 자체의 값이 작은 것을 선택하라고 했으므로, 그 경우는 ([2, 2, 2, 2], 4)와 같이 값이 동일한 경우일 때이다.
# 이 때를 신경써서 동일한 값이 반복되는 구간까지 sequence의 뒷부분을 빼주어서 인덱스가 최소가 되게 해준다.

def solution(sequence, k):
    total = 0
    
    for i in range(len(sequence)-1, -1, -1):
        total += sequence[i]
        if total > k:
            total -= sequence.pop()
        elif total == k:
            while sequence[i-1] == sequence[-1] and i >= 1:
                i -= 1
                sequence.pop()
                
            return [i, len(sequence)-1]
