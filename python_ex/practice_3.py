# 임의의 정수 n에 대해, n이 어떤 정수 x의 제곱인지 아닌지 판단하려 합니다.
# n이 정수 x의 제곱이라면 x+1의 제곱을 리턴하고, n이 정수 x의 제곱이 아니라면 -1을 리턴하는 함수를 완성하세요.


def solution(n):
    num = pow(n, 0.5)
    if num == int(num):
        return pow(num+1, 2)
    return -1
