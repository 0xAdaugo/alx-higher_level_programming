#!/usr/bin/node

const argsLength = (process.argv.length - 2);

if (argsLength === 0) {
  console.log('No argument');
  process.exit(0);
} else if (argsLength === 1) {
  console.log('Argument found');
  process.exit(0);
} else {
  console.log('Arguments found');
  process.exit(0);
}
