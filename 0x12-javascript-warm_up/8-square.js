#!/usr/bin/node
const number = parseInt(process.argv[2]);
let square = '';
if (Number.isInteger(number)) {
  for (let i = 0; i < number; i++) {
    for (let j = 0; j < number; j++) {
      square += 'X';
    }
    if (i < number - 1) {
      square += '\n';
    }
  }
  console.log(square);
} else {
  console.log('Missing size');
}
