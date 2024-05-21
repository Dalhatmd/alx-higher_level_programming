#!/usr/bin/node

const str = 'C is fun';

if (process.argv.length < 2 || isNaN(parseInt(process.argv[2]))) {
  console.log('Missing number of occurrences');
}
const num = parseInt(process.argv[2]);

for (let i = 0; i < num; i++) {
  console.log(str);
}
