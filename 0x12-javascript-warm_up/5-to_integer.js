#!/usr/bin/node

const args = (process.argv[2]);
const intArgs = parseInt(args);

if (!isNaN(intArgs)) {
  console.log(`My number: ${intArgs}`);
} else {
  console.log('Not a number');
}
