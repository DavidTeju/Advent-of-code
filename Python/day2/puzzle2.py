from inputter import text

# text = """A Y
# B X
# C Z"""


key = {"A": 1, "B": 2, "C": 3,
       "X": 1, "Y": 2, "Z": 3}

score = 0
for game in text.split("\n"):
    prev = score
    elf, result = game.split(" ")
    if result == "X":
        score += 0 + ((key[elf] - 2) % 3) + 1
    elif result == "Y":
        score += 3 + key[elf]
    else:
        score += 6 + ((key[elf]) % 3) + 1

print(score)
