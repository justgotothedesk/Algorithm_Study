# 문제의 조건에 맞게 공격을 받을 때와 그렇지 않을 때를 구분해서 순차적으로 정리하면 어렵지 않다.

def solution(bandage, health, attacks):
    maxv = health
    maxt = attacks[-1][0]
    clock = 0
    time, demage = None, None
    continuous = 0
    debug = []
    
    while clock < maxt: # 해당 조건이 없으면 무한 루프가 발생함
        if time == None and demage == None and attacks:
            time, demage = attacks.pop(0)
        clock += 1

        # 공격 받을 때
        if clock == time:
            health -= demage
            if health <= 0:
                return -1
            
            continuous = 0
            time, demage = None, None

        # 공격 받지 않을 때
        else:   
            continuous += 1
            if health+bandage[1] >= maxv:
                health = maxv
            else:
                health += bandage[1]
                
            if continuous == bandage[0]:
                continuous = 0
                if health+bandage[2] >= maxv:
                    health = maxv
                else:
                    health += bandage[2]
    
    return health
