# 예를 들어, 입력된 수가 6이라면 6→3→10→5→16→8→4→2→1 이 되어 총 8번 만에 1이 됩니다.
# 위 작업을 몇 번이나 반복해야하는지 반환하는 함수, solution을 완성해 주세요.
# 단, 작업을 500번을 반복해도 1이 되지 않는다면 –1을 반환해 주세요.


def solution(num):
    if num == 1:
        return 0

    for i in range(500):
        num = num/2 if num % 2 == 0 else num*3+1

        if num == 1:
            return i+1

    return -1
