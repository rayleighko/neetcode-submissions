from typing import Dict # this adds type hinting for Dict

def count_characters(word: str) -> Dict[str, int]:
    pass

    res = {}
    for w in word:
        if w in res:
            res[w] += 1
        else:
            res[w] = 1

    return res



# don't modify below this line
print(count_characters("hello"))
print(count_characters("world"))
print(count_characters("hello world"))
print(count_characters("this is a longer sentence"))
