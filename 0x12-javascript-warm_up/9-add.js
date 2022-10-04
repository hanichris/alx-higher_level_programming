#!/usr/bin/node
'use strict';

const args = process.argv.slice(2);

function add (a, b) {
  return a + b;
}

const result = add(+args[0], +args[1]);
console.log(result);
