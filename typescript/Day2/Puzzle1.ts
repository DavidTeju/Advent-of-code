function day2_1() {
  let text: string = require("../inputter").get_input(__dirname);

  //   txt = `A Y
  // B X
  // C Z`;

  let key: { [index: string]: number } = {
    A: 1,
    B: 2,
    C: 3,
    X: 1,
    Y: 2,
    Z: 3,
  };

  //A Y

  // @ts-ignore
  Number.prototype.mod = function (b: number) {
    // @ts-ignore
    return ((this % b) + b) % b;
  };

  let answer = text.split("\n").reduce((score, game) => {
    let [elf, me] = game.split(" ");
    if (key[elf] === key[me]) return score + 3 + key[me];
    // @ts-ignore
    else if ((key[elf] - 2).mod(3) + 1 === key[me]) return score + key[me];
    else return score + 6 + key[me];
  }, 0);

  console.log(answer);
}

day2_1();
