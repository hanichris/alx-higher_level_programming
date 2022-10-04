#!/usr/bin/node
'use strict';

const number = +process.argv[2];

if (isNaN(number)) console.log(1);
else console.log(factorial(number));

function factorial (n) {
  if (n === 0 || n === 1) return 1;
  return n * factorial(n - 1);
}
