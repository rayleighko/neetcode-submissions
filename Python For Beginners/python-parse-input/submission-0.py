from typing import List

def read_integers() -> List[int]:
    pass
    string_list = input().split(",")
    res = []
    for s in string_list:
        res.append(int(s))
    return res

# do not modify the code below
print(read_integers())
print(read_integers())
print(read_integers())
