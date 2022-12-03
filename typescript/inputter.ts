export function get_input(dir: string): string {
  let fs = require("fs");
  return fs.readFileSync(`${dir}/input.txt`, "utf-8");
}
