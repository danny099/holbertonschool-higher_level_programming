#!/usr/bin/node
let count = 0;
process.argv.forEach((value, i) => {
  count = i;
});

if (count <= 1) {
  console.log('No argument');
} else {
  console.log(process.argv[2]);
}
