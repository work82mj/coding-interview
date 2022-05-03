def encryption1(s):
    strings = s.replace(" ", "")
    L = math.sqrt(len(strings))
    n_row = int(L % 10)

    n_col = n_row + 1
    ret = ['' for _ in range(n_col)]

    for idx, char in enumerate(strings):
        ret[idx % n_col] += char

    return " ".join(ret)

def encryption2(s):
    # Write your code here
    strings = s.replace(" ", "")
    L = math.sqrt(len(strings))
    n_col = int(L % 10) + 1
    ret = []
    for i in range(n_col):
        ret.append(strings[i::n_col])
    return " ".join(ret)


def encryption3(s):
    # Write your code here
    n_col = math.ceil(math.sqrt(len(s)))

    return ' '.join(map(lambda x: s[x::n_col], range(n_col)))

