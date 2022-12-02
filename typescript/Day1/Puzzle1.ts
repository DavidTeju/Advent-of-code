let fs = require("fs")

const text: string = fs.readFileSync("Day1/input.txt", "utf-8")

let answer = text.split("\n\n")
    .map(elf => elf.split("\n").map(food => parseInt(food)))
    .map(elf => elf.reduce((total, curr) => total + curr))
    .reduce((max, curr) => Math.max(max, curr))

console.log(answer)