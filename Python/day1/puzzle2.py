import heapq
from inputter import text

elves = [sum(int(food) for food in elf.split("\n")) for elf in text.split("\n\n")]

answer = sum(heapq.nlargest(3, elves))

print(answer)
