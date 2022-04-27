"""
https://programmers.co.kr/learn/courses/30/lessons/43165
"""
def solution(numbers, target):
    def dfs(numbers, target, count, sign):
        if numbers:
            return dfs(numbers[1:], target + sign * numbers[0], count, 1) + dfs(numbers[1:], target + sign * numbers[0],
                                                                                count, -1)
        else:
            if target == 0:
                return count + 1
            else:
                return count

    return (dfs(numbers, target, 0, 1) + dfs(numbers, target, 0, -1)) / 2


def solution2(numbers, target):
    if not numbers:
        if target == 0:
            return 1
        else:
            return 0

    return solution(numbers[1:], target + numbers[0]) + solution(numbers[1:], target - numbers[0])