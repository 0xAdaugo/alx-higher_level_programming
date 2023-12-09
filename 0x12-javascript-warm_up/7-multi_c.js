#!/usr/bin/node

const intArgs = parseInt(process.argv[2]);
let i;

if (!isNaN(intArgs)) {
  for (i = 0; i < intArgs; i++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
