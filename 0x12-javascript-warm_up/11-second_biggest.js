#!/usr/bin/node
const len = process.argv.length;
if (len <= 2) {
  console.log(0);
} else if (len === 3) {
  console.log(0);
} else {
  secondBiggest();
}

function secondBiggest () {
  const second = process.argv.sort(function (a, b) { return b - a; });
  console.log(second[3]);
}
