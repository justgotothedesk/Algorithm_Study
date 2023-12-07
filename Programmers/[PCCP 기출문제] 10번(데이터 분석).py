# str 값에 따라서 값을 선택하고 정렬해야하기 때문에 str 값을 index 번호로 번환하는 함수 ext_index 함수를 만들어준다.
# val_ext보다 작은 값만을 남겨주고 람다 함수를 사용하여 정렬을 해준다.

def ext_index(ext):    
    if ext == "code":
        return 0
    elif ext == "date":
        return 1
    elif ext == "maximum":
        return 2
    else:
        return 3
    
def solution(data, ext, val_ext, sort_by):
    answer = []
    
    for i in data:
        index = ext_index(ext)
        if i[index] < val_ext:
            answer.append(i)
            
    answer.sort(key = lambda x:x[ext_index(sort_by)])
    
    return answer
