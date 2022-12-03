function day1_2() {
  let text: string = require("../inputter").get_input(__dirname);

  let answer = text
    .split("\n\n")
    .map((elf) => elf.split("\n").map((food) => parseInt(food)))
    .map((elf) => elf.reduce((total, curr) => total + curr))
    .sort((a, b) => b - a)
    .slice(0, 3)
    .reduce((total, curr) => total + curr);

  console.log(answer);
}

day1_2();
