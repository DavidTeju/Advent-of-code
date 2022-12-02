import heapq

with open("input.txt", "r+") as file:
    text = file.read()

elves = [sum(int(food) for food in elf.split("\n")) for elf in text.split("\n\n")]

answer = sum(heapq.nlargest(3, elves))

print(answer)
