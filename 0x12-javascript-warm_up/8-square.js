#!/usr/bin/node

if (process.argv.length < 2 || isNaN(parseInt(process.argv[2]))) {
  console.log('Missing size');
}

const size = parseInt(process.argv[2]);

for (let i = 0; i < size; i++) {
  let row = '';
  for (let j = 0; j < size; j++) {
    row += 'X';
  }
  console.log(row);
}
