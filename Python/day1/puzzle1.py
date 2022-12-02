with open("input.txt", "r+") as file:
    text = file.read()

answer = max(sum(int(food) for food in elf.split("\n")) for elf in text.split("\n\n"))
print(answer)
