from inputter import text


def each_line(line: str):
    middle = len(line) // 2
    first, second = line[:middle], line[middle:]
    alike = set(first).intersection(second).pop()
    return alike


pos_a = ord("a")
start = 1
factor_a = pos_a - start  # to convert priority to ord value, add this to priority
priorities = {chr(priority + factor_a): priority for priority in range(start, start + 26)}

pos_A = ord("A")
start = 27
factor_A = pos_A - start  # to convert priority to ord value, add this to priority
priorities.update({chr(priority + factor_A): priority for priority in range(start, start + 26)})

lines = text.split("\n")
points = sum(priorities[each_line(line)] for line in lines)
print(points)
