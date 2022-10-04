#!/usr/bin/node
'use strict';

const args = process.argv.slice(2);
let largest = -Infinity;
let secondLargest = -Infinity;

if (args.length === 0 || args.length === 1) console.log(0);
else {
  for (let i = 0; i < args.length; i++) {
    const num = +args[i];
    if (num >= largest) {
      secondLargest = largest;
      largest = num;
    } else if (num > secondLargest && num !== largest) {
      secondLargest = num;
    }
  }
  console.log(secondLargest);
}
