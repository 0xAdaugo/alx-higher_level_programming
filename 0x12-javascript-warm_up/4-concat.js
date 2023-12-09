#!/usr/bin/node

if ((process.argv[2]) || process.argv[3]) {
  console.log(process.argv[2] + ' is ' + process.argv[3]);
  process.exit(0);
} else {
  console.log('undefined is undefined');
  process.exit(0);
}
