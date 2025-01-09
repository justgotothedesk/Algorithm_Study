# 2018 KAKAO BLIND RECRUITMENT
# 문자열은 대소문자를 신경쓰지 않으므로 소문자로 모두 바꿔준다.
# 알파벳 두 글자씩 끊어서 비교를 하므로, 두 글자씩 끊었을 때에 알파벳인지 아닌지를 판단한다.
# 두 집합이 모두 영어가 없는 경우에 나눌 수 없으므로, 문제에서 주어진대로 65536을 반환한다.
# 두 집합을 이중 for문으로 탐색하면서, 동일한 값이 있으면 교집합+1과 합집합-1을 해준다.
# 교집합/합집합의 값을 반환한다.

def solution(str1, str2):
    A = []
    B = []
    str1 = str1.lower()
    str2 = str2.lower()
    
    for i in range(len(str1)-1):
        if str1[i].isalpha() and str1[i+1].isalpha():
            A.append(str1[i]+str1[i+1])
    for i in range(len(str2)-1):
        if str2[i].isalpha() and str2[i+1].isalpha():
            B.append(str2[i]+str2[i+1])
            
    if not len(A) and not len(B):
        return 65536
    
    hap = len(A)+len(B)
    kyo = 0
    
    for a in A:
        for b in B:
            if a == b:
                kyo += 1
                B.remove(a)
                hap -= 1
                break
    
    return int(kyo/hap*65536)
