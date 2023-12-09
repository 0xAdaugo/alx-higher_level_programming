#!/usr/bin/node

const intArgs = parseInt(process.argv[2]);
let i, j;

if (!isNaN(intArgs)) {
  for (i = 0; i < intArgs; i++) {
    let row = '';
    for (j = 0; j < intArgs; j++) {
      row += 'X';
    }
    console.log(row);
  }
} else {
  console.log('Missing size');
}
