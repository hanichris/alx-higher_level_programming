#!/usr/bin/node
'use strict';

const dict = require('./101-data').dict;

const newDict = Object.entries(dict).reduce((arr, [key, value]) => {
  arr[value] = arr[value] ? [...arr[value], key] : [key];
  return arr;
}, {});

console.log(newDict);
