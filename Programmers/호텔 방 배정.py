import sys
sys.setrecursionlimit(10000)

def recursive(idx, room):
    if idx not in room.keys():
        room[idx] = idx+1
        
        return idx
    
    empty = recursive(room[idx], room)
    room[idx] = empty+1
    
    return empty

def solution(k, room_number):
    room = {}
    
    for i in room_number:
        recursive(i, room)
    
    return list(room.keys())
