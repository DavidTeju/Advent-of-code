let day1_1 = function () {
  let text: string = require("../inputter").get_input(__dirname);

  let answer = text
    .split("\n\n")
    .map((elf) => elf.split("\n").map((food) => parseInt(food)))
    .map((elf) => elf.reduce((total, curr) => total + curr))
    .reduce((max, curr) => Math.max(max, curr));

  console.log(answer);
};
day1_1();
