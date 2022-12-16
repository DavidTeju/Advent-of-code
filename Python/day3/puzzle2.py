from inputter import text


def each_group(group: list[str, str, str]):
    first, second, third = group
    alike = set(first) & set(second) & set(third)
    return alike.pop()


pos_a = ord("a")
start = 1
factor_a = pos_a - start  # to convert priority to ord value, add this to priority
priorities = {chr(priority + factor_a): priority for priority in range(start, start + 26)}

pos_A = ord("A")
start = 27
factor_A = pos_A - start  # to convert priority to ord value, add this to priority
priorities.update({chr(priority + factor_A): priority for priority in range(start, start + 26)})

lines = text.split("\n")
groups = [lines[num:num + 3] for num in range(0, len(lines), 3)]

points = sum(priorities[each_group(group)] for group in groups)
print(points)
