#!/usr/bin/node
'use strict';

const mul = +process.argv[2];

if (!mul) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < mul; i++) console.log('C is fun');
}
