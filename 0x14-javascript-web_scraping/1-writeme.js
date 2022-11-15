#!/usr/bin/node
const fs = require('fs');

const args = process.argv.slice(2);
const filePath = args[0];
const data = args[1];
fs.writeFile(filePath, data, 'utf-8', (err) => {
  if (err) console.log(err);
});
