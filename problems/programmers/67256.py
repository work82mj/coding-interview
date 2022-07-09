"""
https://school.programmers.co.kr/learn/courses/30/lessons/67256
"""


def solution(numbers, hand):
    keypad = {
        1: [0, 0],
        2: [0, 1],
        3: [0, 2],
        4: [1, 0],
        5: [1, 1],
        6: [1, 2],
        7: [2, 0],
        8: [2, 1],
        9: [2, 2],
        "*": [3, 0],
        0: [3, 1],
        "#": [3, 2],
    }
    ret = []
    curr_l, curr_r = keypad["*"], keypad["#"]

    for num in numbers:
        if num in [1, 4, 7]:
            ret.append("L")
            curr_l = keypad[num]
        elif num in [3, 6, 9]:
            ret.append("R")
            curr_r = keypad[num]
        elif num in [2, 5, 8, 0]:
            point = keypad[num]
            dist_l = abs(curr_l[0] - point[0]) + abs(curr_l[1] - point[1])
            dist_r = abs(curr_r[0] - point[0]) + abs(curr_r[1] - point[1])

            if dist_l < dist_r:
                ret.append("L")
                curr_l = keypad[num]
            elif dist_l > dist_r:
                ret.append("R")
                curr_r = keypad[num]
            else:
                if hand == "left":
                    ret.append("L")
                    curr_l = keypad[num]
                elif hand == "right":
                    ret.append("R")
                    curr_r = keypad[num]
    return "".join(ret)
