from inputter import text

# text = """A Y
# B X
# C Z"""

key = {"A": 1, "B": 2, "C": 3,
       "X": 1, "Y": 2, "Z": 3}

score = 0
for game in text.split("\n"):
    elf, me = game.split(" ")

    if key[elf] == key[me]:
        score += 3 + key[me]
    elif ((key[elf] - 2) % 3) + 1 == key[me]:
        score += key[me]
    else:
        score += 6 + key[me]

print(score)
