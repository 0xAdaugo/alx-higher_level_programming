#!/usr/bin/node

const args = process.argv.slice(2);
const numbers = args.map(Number);
const validNumbers = numbers.filter(num => !isNaN(num));
const numValidArgs = validNumbers.length;

if (numValidArgs <= 1) {
  console.log(0);
} else {
  const sortedNumbers = validNumbers.sort((a, b) => b - a);
  const secondLargest = sortedNumbers[1];
  console.log(secondLargest);
}
