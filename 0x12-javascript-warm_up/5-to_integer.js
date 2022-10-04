#!/usr/bin/node
'use strict';

const value = parseInt(process.argv[2]);
if (isNaN(value)) console.log('Not a Number');
else console.log(`My number: ${value}`);
