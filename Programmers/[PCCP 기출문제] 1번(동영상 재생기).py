def time_to_seconds(time_str):
    min, sec = map(int, time_str.split(":"))
    
    return min*60+sec

def seconds_to_time(sec):
    min = sec // 60
    sec = sec % 60
    
    return f"{min:02}:{sec:02}"

def solution(video_len, pos, op_start, op_end, commands):
    video_len_sec = time_to_seconds(video_len)
    pos_sec = time_to_seconds(pos)
    op_start_sec = time_to_seconds(op_start)
    op_end_sec = time_to_seconds(op_end)

    for command in commands:
        if op_start_sec <= pos_sec <= op_end_sec:
            pos_sec = op_end_sec
        if command == "next":
            pos_sec = min(pos_sec+10, video_len_sec)
        elif command == "prev":
            pos_sec = max(pos_sec-10, 0)
        if op_start_sec <= pos_sec <= op_end_sec:
            pos_sec = op_end_sec

    return seconds_to_time(pos_sec)
