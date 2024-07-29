#!/usr/bin/node

let args = process.argv.slice(2);

if (args.length < 1) {
  console.log(0);
} else if (args.length < 2) {
  console.log(0);
} else {
 args.sort((a, b) => a - b);

console.log(args[args.length - 2]); 
}



