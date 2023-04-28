from inputter import text

list_of_pairs = [[[int(section) for section in elf.split("-")]
                  for elf in pair.split(",")]
                 for pair in text.split("\n")]


def default_min_max(func, key):
    return -1 if key(0) == key(1) else func(0, 1, key=key)


def each_pair(pair):
    func = max, min
    first, second = (default_min_max(func[i], lambda num: pair[num][i]) for i in range(2))
    return 1 if second == first or first == -1 or second == -1 else 0


total = sum(each_pair(pair) for pair in list_of_pairs)

print(total)
