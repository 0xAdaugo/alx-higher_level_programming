#!/usr/bin/node

const args = (process.argv[2]);

if (args === undefined) {
  console.log('No argument');
  process.exit(0);
} else {
  console.log(args);
  process.exit(0);
}
