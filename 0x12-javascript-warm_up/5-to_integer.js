#!/usr/bin/node
'use strict';

const value = parseInt(process.argv[2]);
if (Number.isNaN(value)) console.log('Not a number');
else console.log(`My number: ${value}`);
