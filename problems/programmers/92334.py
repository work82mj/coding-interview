"""
https://school.programmers.co.kr/learn/courses/30/lessons/92334
"""
from collections import defaultdict


def solution(id_list, report, k):
    reported_dict = defaultdict(int)
    reporter_dict = defaultdict(list)
    for r in set(report):
        reporter, reported = r.split()
        reporter_dict[reporter].append(reported)
        reported_dict[reported] += 1

    mailed_id = [key for key, val in reported_dict.items() if val >= k]

    report_cnt = defaultdict(int)

    for reporter, reported in reporter_dict.items():
        for r_id in reported:
            if r_id in mailed_id:
                report_cnt[reporter] += 1

    return [report_cnt[key] for key in id_list]
