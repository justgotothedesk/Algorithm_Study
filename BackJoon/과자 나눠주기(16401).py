def main():
    M, N = map(int, input().split())
    sticks = list(map(int, input().split()))

    start = 1
    end = max(sticks)
    while start <= end:
        mid = (start + end) // 2
        count = 0
        for stick in sticks:
            count += (stick // mid)
        if count < M:
            end = mid - 1
        else:
            start = mid + 1
    print(end)

if __name__ == "__main__":
    main()
