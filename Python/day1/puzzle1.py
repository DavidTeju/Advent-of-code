from inputter import text

answer = max(sum(int(food) for food in elf.split("\n")) for elf in text.split("\n\n"))
print(answer)
