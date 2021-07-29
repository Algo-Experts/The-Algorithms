def solution(dartResult):
    divided = []       # 문자열의 3회 결과를 전부 나눈다. 1S2D*3T -> [1S, 2D*, 3T]
    check_point = 0    # 문자열을 잘라낼 체크포인트
    for i in range(1, len(dartResult)):  # 문자열에 대해서
        if i == len(dartResult) - 1:     # 마지막까지 돌았으면
            divided.append(dartResult[check_point:])
        if dartResult[i].isdigit():      # 중간에 정수가 있으면, 그 전까지를 1회의 결과로 판별
            if dartResult[i] == "0" and dartResult[i - 1] == "1":    # 10점의 경우에만 예외처리
                continue
            else:
                divided.append(dartResult[check_point:i])    # 아니면 이전 체크포인트부터 i까지 1회의 결과로
                check_point = i

    total_point = []    # 전체 포인트 계산
    for d in divided:   # 1회 결과에 대해 조건문으로 점수 줌
        if "10" in d:
            point = 10
        else:
            point = int(d[0])
        if "S" in d:
            total_point.append(point)
        elif "D" in d:
            total_point.append(point**2)
        elif "T" in d:
            total_point.append(point**3)
        if "#" in d:
            total_point[-1] *= -1
        elif "*" in d:   # *이 있을경우 맨 뒤에서 2회 점수 *2
            for p in range(len(total_point)-2, len(total_point)):
                if p >= 0:
                    total_point[p] *= 2

    return sum(total_point)


print(solution("1S2D*3T"))