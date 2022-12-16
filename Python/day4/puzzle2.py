from inputter import text

list_of_pairs = [[[int(section) for section in elf.split("-")]
                  for elf in pair.split(",")]
                 for pair in text.split("\n")]


def default_min_max(func, key):
    """
    Find min or max but return -1 as default is equal‰
    :param func: min or max
    :param key: key to be used just as in min and max
    :return:
    """
    return -1 if key(0) == key(1) else func(0, 1, key=key)


def each_pair(pair):
    func = max, min
    first_max, second_min = (default_min_max(func[i], lambda num: pair[num][i]) for i in range(2))

    if min(first_max, second_min) == -1 or pair[first_max][0] <= pair[(first_max + 1) % 2][1]:
        return 1
    return 0


total = sum(each_pair(pair) for pair in list_of_pairs)

print(total)
